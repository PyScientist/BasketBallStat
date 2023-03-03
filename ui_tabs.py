import numpy as np
import pandas as pd

import os

from PyQt5.QtWidgets import QTableWidgetItem, QAbstractScrollArea, QSizePolicy, QVBoxLayout, QColorDialog
from PyQt5.QtGui import QFont, QColor, QBrush
from PyQt5.QtCore import QDate
from StatSmart_app import calc_time_shift, convert_date

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib import pyplot as plt

import datetime

from PredictionModels_app import prepare_data_for_prediction, make_prediction, add_grid


class MyMplCanvas(FigureCanvasQTAgg):
    def __init__(self, fig, parent=None):
        self.fig = fig
        FigureCanvasQTAgg.__init__(self, self.fig)
        FigureCanvasQTAgg.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)


class CanvasAndToolbar:
    def __init__(self, parent_widget):
        # Создание рисунка и пустых стандартных осей
        self.fig, self.axes = self.plot_single_empty_graph()

        # Создание компоновки для размещения холста и панели управления если это первая подготовка холста
        self.layout = QVBoxLayout(parent_widget)
        self.canvas = MyMplCanvas(self.fig)
        self.layout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, parent_widget)
        self.layout.addWidget(self.toolbar)

    def set_title(self, title):
        self.axes.set_title(title)

    def plot_data(self, data, x, y):
        self.axes.plot(data)
        self.axes.set_xlabel(x)
        self.axes.set_ylabel(y)


    @staticmethod
    def plot_single_empty_graph():
        """
        Создание рисунка и осей для отображения единичного графика
        """
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 7), dpi=85,
                                 facecolor='white', frameon=True, edgecolor='black', linewidth=1)
        fig.subplots_adjust(wspace=0.4, hspace=0.6, left=0.15, right=0.85, top=0.9, bottom=0.1)
        axes.grid(True, c='lightgrey', alpha=0.5)
        axes.set_title('Заголовок диаграммы', fontsize=10)
        axes.set_xlabel('X', fontsize=8)
        axes.set_ylabel('Y', fontsize=8)
        return fig, axes


class LastGamesTab:
    def __init__(self, host):
        try:
            self.host = host
            self.color_file_path = './colors_list.csv'
            self.fill_league_and_team()
            self.host.lineEdit_file_with_parsing_results.textEdited.connect(self.fill_league_and_team)
            self.host.comboBox_LastGames_choose_league.currentTextChanged.connect(self.change_teams)
            self.host.pushButton_show_LastGames_details.clicked.connect(self.fill_table)
            self.host.spinBox_games_ammount_to_show.setValue(10)
            self.host.spinBox_games_ammount_to_show.valueChanged.connect(self.fill_table)
            self.host.TableWidget_LastGames.itemDoubleClicked.connect(self.choose_color)
            self.host.pushButton_save_colors.clicked.connect(self.save_color_scheme)

            self.host.label_set_color1.setStyleSheet("background-color: #90EE90;")
            self.host.label_set_color2.setStyleSheet("background-color: #FFB6C1;")
            self.host.label_set_color3.setStyleSheet("background-color: #0078D7;")

        except Exception:
            self.host.textEdit_parsing_information.insertPlainText(f'\nSome error occurred '
                                                                   f'while loading LastGames tab')
    def choose_color(self, item):
        if self.host.checkBox_use_standart_color.isChecked():
            if self.host.radioButton_set_color1.isChecked():
                color = QColor(144, 238, 144)
            elif self.host.radioButton_set_color2.isChecked():
                color = QColor(255, 182, 193)
            elif self.host.radioButton_set_color3.isChecked():
                color = QColor(0, 120, 215)
            else:
                color = QColorDialog.getColor()
        else:
            color = QColorDialog.getColor()
        row = item.row()
        columns = self.host.TableWidget_LastGames.columnCount()
        for col in range(columns):
            self.host.TableWidget_LastGames.item(row, col).setBackground(QBrush(color))

    def save_color_scheme(self):
        try:
            colors_to_save = []
            for row in range(self.host.TableWidget_LastGames.rowCount()):
                list_row = []
                for col in range(3):
                    list_row.append(self.host.TableWidget_LastGames.item(row, col).text())
                rgb_color = self.host.TableWidget_LastGames.item(row, col).background().color().getRgb()
                list_row.append(rgb_color)
                colors_to_save.append(list_row)
            headers = ['Date', 'Team at home', 'Team away', 'color']
            colors_df = pd.DataFrame(colors_to_save, columns=[headers])

            if os.path.exists(self.color_file_path):
                df = pd.read_csv(self.color_file_path, sep=';')
                df_data = list(df[headers].values)
                colors_df_data = list(colors_df[headers].values)

                indexes_to_delete = []
                for x in range(len(df_data)):
                    for y in range(len(colors_df_data)):
                        if ((df_data[x][0] == colors_df_data[y][0])
                                & (df_data[x][1] == colors_df_data[y][1])
                                & (df_data[x][2] == colors_df_data[y][2])):
                            indexes_to_delete.append(x)

                indexes_to_delete.sort(reverse=True)
                for index in indexes_to_delete:
                    df_data.pop(index)

                df_data.extend(colors_df_data)
                df_to_export = pd.DataFrame(df_data, columns=[headers])
                df_to_export .to_csv(path_or_buf=self.color_file_path, sep=';', index=False)

            else:
                colors_df.to_csv(path_or_buf=self.color_file_path, sep=';', index=False)
        except:
            pass

    def load_colors(self):
        headers = ['Date', 'Team at home', 'Team away', 'color']
        df = pd.read_csv(self.color_file_path, sep=';')
        return [list(x) for x in df[headers].values]

    def fill_league_and_team(self):
        self.host.comboBox_LastGames_choose_league.clear()
        self.host.comboBox_LastGames_choose_league.addItems(self.host.init_df['League'].unique())
        self.change_teams()

    def change_teams(self):
        self.host.comboBox_LastGames_choose_team.clear()
        league = self.host.comboBox_LastGames_choose_league.currentText()
        self.host.comboBox_LastGames_choose_team.addItems
        league_df = self.host.init_df[self.host.init_df['League'] == league].copy()
        teams = league_df['Team #1'].unique()
        self.host.comboBox_LastGames_choose_team.addItems(teams)

    def fill_table(self):

        def is_integer(n):
            """Return True if argument is a whole number, False if argument has a fractional part."""
            if n % 2 == 0 or (n + 1) % 2 == 0:
                return True
            return False

        def smart_round(n, digits):
            if is_integer(float(n)):
                return int(float(n))
            else:
                return round(float(n), digits)

        def round_row(row_in, digits):
            def value_is_digit(value):
                try:
                    float(value)
                    return True
                except ValueError:
                    return False
            return [smart_round(value, digits) if value_is_digit(value) else value for value in row_in]

        league = self.host.comboBox_LastGames_choose_league.currentText()
        team = self.host.comboBox_LastGames_choose_team.currentText()

        df_main_selection = self.host.init_df[(self.host.init_df['League'] == league)
                                              & (self.host.init_df['Team #1'] == team)].copy()

        df_main_selection['Date'] = [convert_date(x) for x in df_main_selection['Date']]
        df_main_selection = df_main_selection.sort_values('Date')

        games_to_show = int(self.host.spinBox_games_ammount_to_show.value())

        df_main_selection['2P% #1'] = (df_main_selection['2P% #1'] / 100).round(3)
        df_main_selection['3P% #1'] = (df_main_selection['3P% #1'] / 100).round(3)
        df_main_selection['FT% #1'] = (df_main_selection['FT% #1'] / 100).round(3)
        df_main_selection.insert(7, 'FGA #1', (df_main_selection['2PA #1'] + df_main_selection['3PA #1']).round(1))
        df_main_selection.insert(7, '2P #1', (df_main_selection['2PA #1'] * df_main_selection['2P% #1']).round(1))
        df_main_selection.insert(10, '3P #1', (df_main_selection['3PA #1'] * df_main_selection['3P% #1']).round(1))
        df_main_selection.insert(15, 'FT #1', (df_main_selection['FTA #1'] * df_main_selection['FT% #1']).round(1))

        df_main_selection.rename(columns={'Home team score': 'HTS',
                                          'Outside team score': 'OTS',
                                          'Total points': 'TOTAL',
                                          'Victory flag': 'VF',}, inplace=True)

        df_show = df_main_selection.tail(games_to_show)[[
                                                          'Date',
                                                          'Team at home',
                                                          'Team away',
                                                          'HTS',
                                                          'OTS',
                                                          'TOTAL',
                                                          'FGA #1',
                                                          '2P #1',
                                                          '2PA #1',
                                                          '2P% #1',
                                                          '3P #1',
                                                          '3PA #1',
                                                          '3P% #1',
                                                          'FT #1',
                                                          'FTA #1',
                                                          'FT% #1',
                                                          'ORB #1',
                                                          'DRB #1',
                                                          'TRB #1',
                                                          'AST #1',
                                                          'F #1',
                                                          'STL #1',
                                                          'BLK #1',
                                                          'TOV #1',
                                                          'VF',
                                                          ]]



        columns_header = list(df_show.columns.values)
        columns = len(columns_header)
        results = [list(x) for x in df_show.values]
        rows = len(results)
        rows_header = [str(x) for x in range(1, rows+1)]

        self.host.TableWidget_LastGames.setRowCount(rows)
        self.host.TableWidget_LastGames.setColumnCount(columns)
        self.host.TableWidget_LastGames.setHorizontalHeaderLabels(columns_header)
        self.host.TableWidget_LastGames.setVerticalHeaderLabels(rows_header)

        colors_list = self.load_colors()

        colors_dict = {}
        for x in range(len(results)):
            for y in range(len(colors_list)):
                if ((str(results[x][0]) == str(colors_list[y][0]))
                        & (results[x][1] == colors_list[y][1])
                        & (results[x][2] == colors_list[y][2])):
                    colors_dict[x] = colors_list[y][3]

        for j in range(rows):
            for i in range(columns):
                item = QTableWidgetItem()
                item.setText(str(results[j][i]))
                item.setBackground(QColor(235, 235, 235))
                if j in colors_dict:
                    r, g, b, _ = colors_dict[j].replace('(', '').replace(')', '').split(',')
                    item.setBackground(QColor(int(r), int(g), int(b)))

                self.host.TableWidget_LastGames.setItem(j, i, item)

        self.host.TableWidget_LastGames.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.host.TableWidget_LastGames.resizeColumnsToContents()

        df_for_median = df_show.copy()
        df_for_median.drop(columns=['Date', 'Team at home', 'Team away', 'VF'], axis=1, inplace=True)
        df_median_stat = df_for_median.agg([np.median])
        median_data = [list(x) for x in df_median_stat.values]

        for i, column in enumerate(median_data):
            median_data[i] = round_row(column, 1)

        median_rows_headers = [team]
        median_rows = len(median_rows_headers)
        median_columns_header = list(df_median_stat.columns.values)
        median_columns = len(median_columns_header)

        self.host.tableWidget_LastGamesAvg.setRowCount(median_rows)
        self.host.tableWidget_LastGamesAvg.setColumnCount(median_columns)
        self.host.tableWidget_LastGamesAvg.setHorizontalHeaderLabels(median_columns_header)
        self.host.tableWidget_LastGamesAvg.setVerticalHeaderLabels(median_rows_headers)

        for j in range(median_rows):
            for i in range(median_columns):
                item = QTableWidgetItem()
                item.setText(str(median_data[j][i]))
                self.host.tableWidget_LastGamesAvg.setItem(j, i, item)

        self.host.tableWidget_LastGamesAvg.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.host.tableWidget_LastGamesAvg.resizeColumnsToContents()


class ModelTab:
    def __init__(self, host):
        self.host = host
        self.prediction_assignment = None
        self.prediction_results = None
        try:
            # Атрибут method показывает перерисовываем re_draw либо рисуем изначально initial (c нуля)
            self.model_mpl_canvas = CanvasAndToolbar(self.host.widget_for_mpl_model)
            self.model_mpl_canvas.set_title('Results of model adjustment')
            self.distribution_mpl_canvas = CanvasAndToolbar(self.host.widget_for_mpl_param_distrib)
            self.distribution_mpl_canvas.set_title('Distribution of parameter')
            self.set_league_list()
            self.set_teams_lists()
            self.set_params_to_predict()
            self.host.comboBox_choose_league_prognose.currentTextChanged.connect(self.set_teams_lists)
            self.host.dateEdit_next_game_prognose.setDate(QDate(datetime.datetime.today()))
            self.host.pushButton_do_prognose.clicked.connect(self.do_prediction)
        except:
            pass

    def do_prediction(self):
        try:
            # Готовим задание для прогнозирования
            if self.host.checkBox_homeflag_for_prognose.isChecked():
                home_flag = 1
            else:
                home_flag = 0
            self.prediction_assignment = prepare_data_for_prediction(
                target=self.host.comboBox_param_to_predict.currentText(),
                league=self.host.comboBox_choose_league_prognose.currentText(),
                team=self.host.comboBox_choose_team_prognose.currentText(),
                op_team=self.host.comboBox_choose_opponent_prognose.currentText(),
                home_flag=home_flag,
                next_play_date=self.host.dateEdit_next_game_prognose.date().toPyDate(),
                days_for_model=int(self.host.spinBox_days_backward_model.value()),
                days_for_param=int(self.host.spinBox_days_backward_params.value()))

            # Осуществляем прогноз
            self.prediction_results = make_prediction(self.host.init_df, self.prediction_assignment)
            # Показываем принятые параметры с учетом которых осуществлен прогноз
            self.show_parameters_for_prediction(self.prediction_results['dfp'])
            # Устанавливаем имя прогнозируемого параметра на лэйбл
            self.host.label_predicted_param.setText(self.prediction_assignment['target'])
            # Устанавливаем результат прогнозирования параметра в соответствующую графу
            self.host.lineEdit_predicted_value.setText(str(np.round(self.prediction_results['y_calc'], 3)))
            # Выводим данные использованные для обучения и тестовые данные на график
            # сопоставления прогнозного и фактического параметра
            self.prediction_results['model'].plot_knr_training_results(self.model_mpl_canvas.axes)
            self.model_mpl_canvas.fig.canvas.draw()  # Перерисовываем холст рисунка matplotlib
            # Выводим распределения параметра в заданном промежутке времени
            # 1. За все время /
            # 2. За выбранный промежуток для прогноза (промежуток для параметров) /
            # 3. За выбранный промежуток для прогноза (только домашние матчи) /
            # 4. Наносим на распределение прогнозное значение параметра.
            self.make_distributions()
        except:
            pass

    def show_parameters_for_prediction(self, dfp):
        self.host.lineEdit_2PA1.setText(str(np.round(dfp.data_for_prediction['2PA #1'].values[0], 1)))
        self.host.lineEdit_2PP1.setText(str(np.round(dfp.data_for_prediction['2P% #1'].values[0]/100, 3)))
        self.host.lineEdit_3PA1.setText(str(np.round(dfp.data_for_prediction['3PA #1'].values[0], 1)))
        self.host.lineEdit_3PP1.setText(str(np.round(dfp.data_for_prediction['3P% #1'].values[0]/100, 3)))
        self.host.lineEdit_FTA1.setText(str(np.round(dfp.data_for_prediction['FTA #1'].values[0], 1)))
        self.host.lineEdit_FTP1.setText(str(np.round(dfp.data_for_prediction['FT% #1'].values[0]/100, 3)))
        self.host.lineEdit_ORB1.setText(str(np.round(dfp.data_for_prediction['ORB #1'].values[0], 1)))
        self.host.lineEdit_TRB1.setText(str(np.round(dfp.data_for_prediction['TRB #1'].values[0], 1)))
        self.host.lineEdit_AST1.setText(str(np.round(dfp.data_for_prediction['AST #1'].values[0], 1)))
        self.host.lineEdit_F1.setText(str(np.round(dfp.data_for_prediction['F #1'].values[0], 1)))
        self.host.lineEdit_STL1.setText(str(np.round(dfp.data_for_prediction['STL #1'].values[0], 1)))
        self.host.lineEdit_BLK1.setText(str(np.round(dfp.data_for_prediction['BLK #1'].values[0], 1)))
        self.host.lineEdit_TOV1.setText(str(np.round(dfp.data_for_prediction['TOV #1'].values[0], 1)))
        self.host.lineEdit_PTS1.setText(str(np.round(dfp.data_for_prediction['PTS #1'].values[0], 1)))
        self.host.lineEdit_2PA2.setText(str(np.round(dfp.data_for_prediction['2PA #2'].values[0], 1)))
        self.host.lineEdit_2PP2.setText(str(np.round(dfp.data_for_prediction['2P% #2'].values[0]/100, 3)))
        self.host.lineEdit_3PA2.setText(str(np.round(dfp.data_for_prediction['3PA #2'].values[0], 1)))
        self.host.lineEdit_3PP2.setText(str(np.round(dfp.data_for_prediction['3P% #2'].values[0]/100, 3)))
        self.host.lineEdit_FTA2.setText(str(np.round(dfp.data_for_prediction['FTA #2'].values[0], 1)))
        self.host.lineEdit_FTP2.setText(str(np.round(dfp.data_for_prediction['FT% #2'].values[0]/100, 3)))
        self.host.lineEdit_ORB2.setText(str(np.round(dfp.data_for_prediction['ORB #2'].values[0], 1)))
        self.host.lineEdit_TRB2.setText(str(np.round(dfp.data_for_prediction['TRB #2'].values[0], 1)))
        self.host.lineEdit_AST2.setText(str(np.round(dfp.data_for_prediction['AST #2'].values[0], 1)))
        self.host.lineEdit_F2.setText(str(np.round(dfp.data_for_prediction['F #2'].values[0], 1)))
        self.host.lineEdit_STL2.setText(str(np.round(dfp.data_for_prediction['STL #2'].values[0], 1)))
        self.host.lineEdit_BLK2.setText(str(np.round(dfp.data_for_prediction['BLK #2'].values[0], 1)))
        self.host.lineEdit_TOV2.setText(str(np.round(dfp.data_for_prediction['TOV #2'].values[0], 1)))
        self.host.lineEdit_PTS2.setText(str(np.round(dfp.data_for_prediction['PTS #2'].values[0], 1)))
        self.host.lineEdit_totalscore.setText(str(np.round(dfp.data_for_prediction['Total points'].values[0], 1)))

    def make_distributions(self):
        self.distribution_mpl_canvas.axes.clear()
        df_all = self.host.init_df[self.host.init_df['Team #1'] == self.prediction_assignment['team']].copy()
        self.distribution_mpl_canvas.axes.hist(df_all[self.prediction_assignment['target']],
                                               bins=25,
                                               label=f'all data n={df_all.shape[0]}')

        start_counter = self.prediction_assignment['time_frames_median_model'][0]
        end_counter = -self.prediction_assignment['time_frames_median_model'][1]

        df_all['TimeShift'] = [calc_time_shift(date, self.prediction_assignment['next_play_date']) for date in df_all['Date']]

        df_all_time_limited = df_all[(df_all['TimeShift'] >= end_counter) & (df_all['TimeShift'] < start_counter)].copy()
        self.distribution_mpl_canvas.axes.hist(df_all_time_limited[self.prediction_assignment['target']],
                                               bins=25,
                                               label=f'timeframe n={df_all_time_limited.shape[0]}', color='red')

        df_all_time_limited_st = df_all_time_limited[df_all_time_limited['Team #2'] == self.prediction_assignment['op_team']].copy()
        self.distribution_mpl_canvas.axes.hist(df_all_time_limited_st[self.prediction_assignment['target']],
                                               bins=5,
                                               label=f'timeframe same team n={df_all_time_limited_st.shape[0]}', color='grey')

        df_all_time_limited_hf = df_all_time_limited[df_all_time_limited['Home flag'] == self.prediction_assignment['home_flag']].copy()
        self.distribution_mpl_canvas.axes.hist(df_all_time_limited_hf[self.prediction_assignment['target']],
                                               bins=10,
                                               label=f'timeframe same field n={df_all_time_limited_hf.shape[0]}', color='green')

        df_all_time_limited_hf_st = df_all_time_limited_hf[df_all_time_limited_hf['Team #2'] == self.prediction_assignment['op_team']].copy()
        self.distribution_mpl_canvas.axes.hist(df_all_time_limited_hf_st[self.prediction_assignment['target']],
                                               bins=5,
                                               label=f'timeframe same field same team n={df_all_time_limited_hf_st.shape[0]}', color='pink')

        x_accepted = [self.prediction_results['y_calc'], self.prediction_results['y_calc']]
        y_accepted = [0, 25]
        self.distribution_mpl_canvas.axes.plot(x_accepted,
                                               y_accepted,
                                               label='predicted val.',
                                               color='red',
                                               linestyle='dashed',
                                               )

        accepted_val = str(np.round(self.prediction_results['y_calc'], 3))

        self.distribution_mpl_canvas.axes.annotate(f'Accepted value={accepted_val}',
                                              xy=(x_accepted[0], 10),
                                              xytext=(x_accepted[0]+x_accepted[0]*0.05, 15),
                                              arrowprops=dict(facecolor='black', shrink=0.05),
                                              )

        self.distribution_mpl_canvas.axes.set_title(f"Distribution of {self.prediction_assignment['target']}")
        self.distribution_mpl_canvas.axes.set_xlabel(f"{self.prediction_assignment['target']}")
        self.distribution_mpl_canvas.axes.set_ylabel('frequency')
        self.distribution_mpl_canvas.axes.legend(loc='upper right', fontsize=7)
        add_grid(self.distribution_mpl_canvas.axes)
        self.distribution_mpl_canvas.fig.canvas.draw()

    def set_league_list(self):
        self.host.comboBox_choose_league_prognose.clear()
        self.host.comboBox_choose_league_prognose.addItems(self.host.init_df['League'].unique())

    def set_teams_lists(self):
        self.host.comboBox_choose_team_prognose.clear()
        self.host.comboBox_choose_opponent_prognose.clear()
        league = self.host.comboBox_choose_league_prognose.currentText()
        league_df = self.host.init_df[self.host.init_df['League'] == league]
        teams = league_df['Team #1'].unique()
        self.host.comboBox_choose_team_prognose.addItems(teams)
        self.host.comboBox_choose_opponent_prognose.addItems(teams)

    def set_params_to_predict(self):
        params = list(self.host.init_df.columns.values)
        items_to_remove = ['main_team', 'League', 'Round', 'Date', 'Team #1', 'RNK #1',
                           'Team #2', 'RNK #2', 'Team at home', 'Team away', 'Home flag',
                           'Home team score', 'Outside team score', 'Victory flag', 'Local path', 'Url', 'season']
        [params.remove(x) for x in items_to_remove]
        self.host.comboBox_param_to_predict.clear()
        self.host.comboBox_param_to_predict.addItems(params)


class TournamentTab:
    def __init__(self, host):
        self.host = host
        self.team_to_highlight = None
        self.param_to_filter = 'WINS'
        try:
            self.host.comboBox_choose_season_for_turnament.clear()
            self.host.comboBo_choose_league_for_turnament.addItems(self.host.init_df['League'].unique())
            self.update_according_leagues_tournament_tab(self.host.init_df)
            self.host.comboBo_choose_league_for_turnament.currentTextChanged.connect(self.change_seasons)
            self.host.pushButtonGetTournamentTable.clicked.connect(self.get_tournament_table)
            self.host.lineEdit_file_with_parsing_results.textEdited.connect(self.refresh_seasons_leagues)
        except Exception:
            self.host.textEdit_parsing_information.insertPlainText(f'\nSome error occurred '
                                                                   f'while loading Tournament tab')

    def update_according_leagues_tournament_tab(self, df):
        self.host.comboBox_choose_season_for_turnament.clear()
        league = self.host.comboBo_choose_league_for_turnament.currentText()
        league_df = df[df['League'] == league]
        seasons = league_df['season'].unique()
        self.host.comboBox_choose_season_for_turnament.addItems(seasons)

    def change_seasons(self):
        self.update_according_leagues_tournament_tab(self.host.init_df)

    def refresh_seasons_leagues(self):
        self.host.comboBo_choose_league_for_turnament.clear()
        self.host.comboBo_choose_league_for_turnament.addItems(self.host.init_df['League'].unique())
        self.update_according_leagues_tournament_tab(self.host.init_df)

    def set_sorting_and_higlighting(self, item):
        try:
            self.param_to_filter = self.host.tableWidget_tournament_table.horizontalHeaderItem(item.column()).text()
            _, self.team_to_highlight = (self.host.tableWidget_tournament_table.verticalHeaderItem(item.row()).text()).split(') ')
        except:
            pass

    def get_tournament_table(self):
        league = self.host.comboBo_choose_league_for_turnament.currentText()
        season = self.host.comboBox_choose_season_for_turnament.currentText()

        params_values_array, params = self.prepare_tournament_data(league, season, self.param_to_filter)

        params_values_array = [list(column) for column in params_values_array]

        if self.host.radioButton_tournament_team_and_oponent.isChecked():
            collorification = True
        elif self.host.radioButton_tournament_team.isChecked():
            collorification = False
            [params_values_array.pop(20) for x in range(19)]
            [params.pop(20) for x in range(19)]
        elif self.host.radioButton_tournament_oponent.isChecked():
            collorification = False
            [params_values_array.pop(1) for x in range(19)]
            [params.pop(1) for x in range(19)]
        else:
            self.host.textEdit_parsing_information.insertPlainText('some Other cases of team/opposite-all plotting')
            collorification = True

        params_values_array = np.array(params_values_array)

        # Initially adjustments of table to show tournament results
        rows = len(params_values_array[0])
        rows_header = params_values_array[0]
        rows_header_num = [f'{i+1}) {x}' for i, x in enumerate(rows_header)]
        columns = len(params[1:])
        columns_header = params[1:]
        self.host.tableWidget_tournament_table.clearContents()
        self.host.tableWidget_tournament_table.setRowCount(rows)
        self.host.tableWidget_tournament_table.setColumnCount(columns)
        self.host.tableWidget_tournament_table.setHorizontalHeaderLabels(columns_header)
        self.host.tableWidget_tournament_table.setVerticalHeaderLabels(rows_header_num)

        self.host.tableWidget_tournament_table.horizontalHeader().setStyleSheet("color: rgb(153, 0, 0); "
                                                                                "background-color: rgb(238, 238, 238)")
        self.host.tableWidget_tournament_table.verticalHeader().setStyleSheet("color: rgb(153, 0, 0); "
                                                                                "background-color: rgb(238, 238, 238)")

        header_font = QFont()
        header_font.setPointSize(8)
        self.host.tableWidget_tournament_table.horizontalHeader().setFont(header_font)
        self.host.tableWidget_tournament_table.verticalHeader().setFont(header_font)

        self.host.tableWidget_tournament_table.itemClicked.connect(self.set_sorting_and_higlighting)

        if self.param_to_filter in columns_header:
            column_to_highlight = columns_header.index(self.param_to_filter)
        else:
            column_to_highlight = 1

        if self.team_to_highlight is None:
            row_to_highlight = 1
        else:
            row_to_highlight = list(rows_header).index(self.team_to_highlight)

        for j in range(rows):
            for i in range(columns):
                item = QTableWidgetItem()
                if collorification == True:
                    if (i >= 0) and (i <= 18):
                        item.setBackground(QColor(176, 224, 230))
                    if (i > 18) and (i <= 37):
                        item.setBackground(QColor(152, 251, 152))
                    if i > 37:
                        item.setBackground(QColor(224, 255, 255))
                if i == column_to_highlight:
                    item.setBackground(QColor(255, 255, 170))
                if j == row_to_highlight:
                    item.setBackground(QColor(255, 204, 102))
                if (i == column_to_highlight) & (j == row_to_highlight):
                    item.setBackground(QColor(250, 128, 114))

                # The first argument of array slice is column and the second the row
                item.setText(str(params_values_array[i+1, j]))
                # The first argument of seItem is row, the second is column
                self.host.tableWidget_tournament_table.setItem(j, i, item)

        self.host.tableWidget_tournament_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.host.tableWidget_tournament_table.resizeColumnsToContents()

        self.team_to_highlight = None
        self.param_to_filter = 'WINS'


    def prepare_tournament_data(self, league, season, param_for_filter):

        def return_stat_list(stat_in, param_in, type_val):
            if type_val == 'median':
                return list(stat_in[(param_in, 'median')])
            elif type_val == 'mean':
                return list(stat_in[(param_in, 'mean')])
            elif type_val == 'sum':
                return list(stat_in[(param_in, 'sum')])
            elif type_val == 'count':
                return list(stat_in[(param_in, 'count')])
            else:
                return None

        def is_integer(n):
            """Return True if argument is a whole number, False if argument has a fractional part."""
            if n % 2 == 0 or (n + 1) % 2 == 0:
                return True
            return False

        def smart_round(n, digits):
            if is_integer(float(n)):
                return int(float(n))
            else:
                return round(float(n), digits)

        def round_row(row_in, digits):
            def value_is_digit(value):
                try:
                    float(value)
                    return True
                except ValueError:
                    return False
            return [smart_round(value, digits) if value_is_digit(value) else value for value in row_in]

        if self.host.radioButton_tournament_home_and_away.isChecked():
            df_main_selection = self.host.init_df[(self.host.init_df['League'] == league)
                                                  & (self.host.init_df['season'] == season)].copy()
        elif self.host.radioButton_tournament_home.isChecked():
            df_main_selection = self.host.init_df[(self.host.init_df['Home flag'] == 1)
                                                  & (self.host.init_df['League'] == league)
                                                  & (self.host.init_df['season'] == season)].copy()
            if df_main_selection.shape[0] < 1:
                df_main_selection = self.host.init_df[(self.host.init_df['League'] == league)
                                                      & (self.host.init_df['season'] == season)].copy()

        elif self.host.radioButton_tournament_away.isChecked():
            df_main_selection = self.host.init_df[(self.host.init_df['Home flag'] == 0)
                                                  & (self.host.init_df['League'] == league)
                                                  & (self.host.init_df['season'] == season)].copy()
            if df_main_selection.shape[0] < 1:
                df_main_selection = self.host.init_df[(self.host.init_df['League'] == league)
                                                      & (self.host.init_df['season'] == season)].copy()
        else:
            df_main_selection = self.host.init_df[(self.host.init_df['League'] == league)
                                                  & (self.host.init_df['season'] == season)].copy()
            self.host.textEdit_parsing_information.insertPlainText('some Error happened while data obtaining')

        df_main_selection['2P% #1'] = df_main_selection['2P% #1']/100
        df_main_selection['3P% #1'] = df_main_selection['3P% #1']/100
        df_main_selection['FT% #1'] = df_main_selection['FT% #1']/100
        df_main_selection.insert(4, 'FGA #1', df_main_selection['2PA #1'] + df_main_selection['3PA #1'])
        df_main_selection.insert(6, '2P #1', df_main_selection['2PA #1']*df_main_selection['2P% #1'])
        df_main_selection.insert(9, '3P #1', df_main_selection['3PA #1']*df_main_selection['3P% #1'])
        df_main_selection.insert(12, 'FT #1', df_main_selection['FTA #1']*df_main_selection['FT% #1'])
        df_main_selection['2P% #2'] = df_main_selection['2P% #2']/100
        df_main_selection['3P% #2'] = df_main_selection['3P% #2']/100
        df_main_selection['FT% #2'] = df_main_selection['FT% #2']/100
        df_main_selection.insert(24, 'FGA #2', df_main_selection['2PA #2'] + df_main_selection['3PA #2'])
        df_main_selection.insert(25, '2P #2', df_main_selection['2PA #2']*df_main_selection['2P% #2'])
        df_main_selection.insert(30, '3P #2', df_main_selection['3PA #2']*df_main_selection['3P% #2'])
        df_main_selection.insert(34, 'FT #2', df_main_selection['FTA #2']*df_main_selection['FT% #2'])
        df_main_selection.rename(columns={'Home team score': 'HTS',
                                          'Outside team score': 'OTS',
                                          'Total points': 'TOTAL',
                                          'Victory flag': 'VF'}, inplace=True)

        df_main_selection.drop(columns=['RNK #1', 'RNK #2', 'Home flag', 'main_team',
                                        'League', 'Round', 'Date',
                                        'Team #2', 'Team at home',
                                        'Team away', 'Local path',
                                        'Url', 'season'], inplace=True)

        params = list(df_main_selection.columns.values)

        params.remove('Team #1')
        params.remove('VF')
        stat = df_main_selection.reset_index(drop=True).groupby('Team #1').agg([np.median, 'mean', 'sum', 'count'])
        del df_main_selection

        params_values_array = [list(stat.index)]

        for param in params:
            params_values_array.append(return_stat_list(stat, param, 'median'))

        params_values_array.append(return_stat_list(stat, 'VF', 'mean'))
        params.append('VF')
        params_values_array.append(return_stat_list(stat, 'VF', 'sum'))
        params.append('WINS')
        params_values_array.append(return_stat_list(stat, 'VF', 'count'))
        params.append('PLAY')
        params.insert(0, 'Team')

        # Round according to vocabulary values in numpy array
        round_dict = {
            '2P% #1': 3, '3P% #1': 3, 'FT% #1': 3, '2P% #2': 3, '3P% #2': 3, 'FT% #2': 3,
            'VF': 3,
                      }

        for i, column in enumerate(params_values_array):
            try:
                params_values_array[i] = round_row(column, round_dict[params[i]])
            except KeyError:
                params_values_array[i] = round_row(column, 1)

        params_values_array_transposed = [list(i) for i in zip(*params_values_array)]
        index_to_sort = params.index(param_for_filter)
        params_values_array_transposed.sort(key=lambda x: x[index_to_sort],
                                            reverse=True)
        params_values_array = np.array([list(i) for i in zip(*params_values_array_transposed)])

        if len(params) == len(params_values_array):
            return params_values_array, params
        else:
            return None
