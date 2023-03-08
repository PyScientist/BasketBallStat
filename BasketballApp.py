import sys
import os
import pandas as pd


from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic

from PyQt5.QtCore import QObject, pyqtSignal, QThread

from parsing_run import perform_parse

from teams_list_import_app import parse_teams_list

from ui_tabs import TournamentTab, LastGamesTab, ModelTab


class WorkerPerformParse(QObject):
    """Worker for performing parsing"""
    finished = pyqtSignal()
    logger = pyqtSignal(str)

    def __init__(self, assignment_dict):
        super().__init__()
        self.assignment_dict = assignment_dict

    def run(self):
        perform_parse(self.assignment_dict, self.logger)
        self.finished.emit()


class Ui(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('./ui/basketball_app_main-window.ui', self)

        dirs_to_create = ['./parse_content', './parse_results']
        for directory in dirs_to_create:
            CHECK_FOLDER = os.path.isdir(directory)
            if not CHECK_FOLDER:
                os.makedirs(directory)

        self.current_assignment_df = None
        self.init_df = None

        self.showMaximized()
        self.setWindowTitle('BasketballAnalysisApp')
        self.lineEdit_file_with_parsing_assignment.setText('./Parsing_assignment.xlsx')
        self.lineEdit_file_with_parsing_results.setText('./Parsing_results.xlsx')

        self.comboBox_choose_league.setMaxVisibleItems(35)
        self.comboBox_choose_season.setMaxVisibleItems(35)
        self.comboBox_choose_team.setMaxVisibleItems(35)

        self.pushButton_choose_assignment_file.clicked.connect(self.choose_assignment_file)
        self.pushButton_choose_results_file.clicked.connect(self.choose_results_file)
        self.load_assignment_file()
        self.load_init_df()
        self.pushButton_parse_results.clicked.connect(self.launch_parsing)
        self.lineEdit_file_with_parsing_assignment.textEdited.connect(self.load_assignment_file)
        self.lineEdit_file_with_parsing_results.textEdited.connect(self.load_init_df)
        self.pushButton_Update_parsing_assignment_file.clicked.connect(self.update_parsing_assignment)
        self.tournament_tab = TournamentTab(self)
        self.last_games_tab = LastGamesTab(self)
        self.model_tab = ModelTab(self)
        self.lineEdit_league_for_parsing.setText('https://www.asia-basket.com'
                                                 '/South-Korea/basketball-League-KBL-Teams.aspx')

    def update_parsing_assignment(self):
        path_for_league = self.lineEdit_league_for_parsing.text()
        assignment_path = self.lineEdit_file_with_parsing_assignment.text()
        parse_teams_list(path_for_league, assignment_path)
        self.textEdit_parsing_information.insertPlainText('Parsing assignment file has successfully updated...')
        self.load_assignment_file()

    def update_according_leagues(self):
        self.comboBox_choose_season.clear()
        self.comboBox_choose_team.clear()
        league = self.comboBox_choose_league.currentText()
        league_df = self.current_assignment_df[self.current_assignment_df['League'] == league]
        teams = league_df['Teams'].unique()
        seasons = league_df['Season'].unique()
        del league_df
        self.comboBox_choose_season.addItem('All')
        self.comboBox_choose_season.addItems(seasons)
        self.comboBox_choose_team.addItem('All')
        self.comboBox_choose_team.addItems(teams)

    def load_init_df(self):
        file_path = self.lineEdit_file_with_parsing_results.text()
        try:
            self.init_df = pd.read_excel(io=file_path,
                                         engine='openpyxl',
                                         sheet_name='Results')

            # Добавляем производные столбцы недоступные ранее
            self.init_df['FGA #1'] = (self.init_df['2PA #1'] + self.init_df['3PA #1']).round(0)
            self.init_df['2P #1'] = (self.init_df['2PA #1'] * self.init_df['2P% #1']/100).round(0)
            self.init_df['3P #1'] = (self.init_df['3PA #1'] * self.init_df['3P% #1']/100).round(0)
            self.init_df['FT #1'] = (self.init_df['FTA #1'] * self.init_df['FT% #1']/100).round(0)
            self.init_df['FGA #2'] = (self.init_df['2PA #2'] + self.init_df['3PA #2']).round(0)
            self.init_df['2P #2'] = (self.init_df['2PA #2'] * self.init_df['2P% #2']/100).round(0)
            self.init_df['3P #2'] = (self.init_df['3PA #2'] * self.init_df['3P% #2']/100).round(0)
            self.init_df['FT #2'] = (self.init_df['FTA #2'] * self.init_df['FT% #2']/100).round(0)

            self.textEdit_parsing_information.insertPlainText(f'\nData from {file_path} was successfully loaded...')
        except:
            self.textEdit_parsing_information.insertPlainText(f'\nSome error occurred while loading {file_path}')


    def choose_assignment_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self,
                                                   'Choose parsing assignment file',
                                                   r"./",
                                                   "Excel files (*.xls *.xlsx *.xlm)")
        self.lineEdit_file_with_parsing_assignment.setText(file_path)

    def choose_results_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self,
                                                   'Choose parsing results destination',
                                                   r"./",
                                                   "Excel files (*.xls *.xlsx *.xlm)")
        self.lineEdit_file_with_parsing_results.setText(file_path)

    def load_assignment_file(self):
        file_path = self.lineEdit_file_with_parsing_assignment.text()
        try:
            self.current_assignment_df = pd.read_excel(io=file_path,
                                                       engine='openpyxl',
                                                       sheet_name='Parse')

            self.textEdit_parsing_information.clear()
            self.textEdit_parsing_information.insertPlainText('Assignment has successfully read...')

            self.comboBox_choose_league.clear()
            self.comboBox_choose_season.clear()
            self.comboBox_choose_team.clear()
            self.comboBox_choose_league.addItems(self.current_assignment_df['League'].unique())
            self.update_according_leagues()
            self.comboBox_choose_league.currentTextChanged.connect(self.adjust_assignment_combobox_seasons_teams)
        except:
            self.textEdit_parsing_information.insertPlainText(f'\nSome error occurred while '
                                                              f'read assignment file from {file_path}')

    def adjust_assignment_combobox_seasons_teams(self):
        self.update_according_leagues()

    def logger_adding_text(self, text):
        if text == 'clean_entirely':
            self.textEdit_parsing_information.clear()
        else:
            self.textEdit_parsing_information.insertPlainText(text)

    def launch_parsing(self):

        assignment_dict = dict()
        assignment_dict['assignment_file'] = self.lineEdit_file_with_parsing_assignment.text()
        assignment_dict['assignment_tab'] = 'Parse'
        assignment_dict['results_file'] = self.lineEdit_file_with_parsing_results.text()
        assignment_dict['results_tab'] = 'Results'
        assignment_dict['league'] = self.comboBox_choose_league.currentText()
        assignment_dict['season'] = self.comboBox_choose_season.currentText()
        assignment_dict['team'] = self.comboBox_choose_team.currentText()

        self.thread_perform_parse = QThread()
        self.worker_perform_parse = WorkerPerformParse(assignment_dict)
        self.worker_perform_parse.moveToThread(self.thread_perform_parse)
        self.thread_perform_parse.started.connect(self.worker_perform_parse.run)
        self.worker_perform_parse.finished.connect(self.thread_perform_parse.quit)
        self.worker_perform_parse.finished.connect(self.worker_perform_parse.deleteLater)
        self.thread_perform_parse.finished.connect(self.thread_perform_parse.deleteLater)
        self.thread_perform_parse.finished.connect(self.load_init_df)
        self.worker_perform_parse.logger.connect(self.logger_adding_text)
        self.thread_perform_parse.start()
        self.pushButton_parse_results.setEnabled(False)
        self.thread_perform_parse.finished.connect(lambda: self.pushButton_parse_results.setEnabled(True))


def main():
    app = QApplication(sys.argv)
    ui = Ui()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    pass
