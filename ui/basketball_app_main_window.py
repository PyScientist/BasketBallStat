# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basketball_app_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1314, 589)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_central_layout = QVBoxLayout()
        self.verticalLayout_central_layout.setObjectName(u"verticalLayout_central_layout")
        self.CorrelationTab = QTabWidget(self.centralwidget)
        self.CorrelationTab.setObjectName(u"CorrelationTab")
        self.Parsing = QWidget()
        self.Parsing.setObjectName(u"Parsing")
        self.verticalLayout_3 = QVBoxLayout(self.Parsing)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_Update_parsing_assignment_file = QPushButton(self.Parsing)
        self.pushButton_Update_parsing_assignment_file.setObjectName(u"pushButton_Update_parsing_assignment_file")
        self.pushButton_Update_parsing_assignment_file.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0.824, y1:0.960227, x2:0.892, y2:1, stop:0.170455 rgba(117, 255, 121, 182), stop:0.869318 rgba(172, 145, 201, 142));")

        self.horizontalLayout_12.addWidget(self.pushButton_Update_parsing_assignment_file)

        self.lineEdit_league_for_parsing = QLineEdit(self.Parsing)
        self.lineEdit_league_for_parsing.setObjectName(u"lineEdit_league_for_parsing")

        self.horizontalLayout_12.addWidget(self.lineEdit_league_for_parsing)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.label_file_with_parcing_assignment = QLabel(self.Parsing)
        self.label_file_with_parcing_assignment.setObjectName(u"label_file_with_parcing_assignment")

        self.verticalLayout.addWidget(self.label_file_with_parcing_assignment)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_choose_assignment_file = QPushButton(self.Parsing)
        self.pushButton_choose_assignment_file.setObjectName(u"pushButton_choose_assignment_file")
        self.pushButton_choose_assignment_file.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0.824, y1:0.960227, x2:0.892, y2:1, stop:0.170455 rgba(117, 255, 121, 182), stop:0.869318 rgba(172, 145, 201, 142));")

        self.horizontalLayout_2.addWidget(self.pushButton_choose_assignment_file)

        self.lineEdit_file_with_parsing_assignment = QLineEdit(self.Parsing)
        self.lineEdit_file_with_parsing_assignment.setObjectName(u"lineEdit_file_with_parsing_assignment")
        self.lineEdit_file_with_parsing_assignment.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_file_with_parsing_assignment.sizePolicy().hasHeightForWidth())
        self.lineEdit_file_with_parsing_assignment.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.lineEdit_file_with_parsing_assignment)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(self.Parsing)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_choose_results_file = QPushButton(self.Parsing)
        self.pushButton_choose_results_file.setObjectName(u"pushButton_choose_results_file")
        self.pushButton_choose_results_file.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0.824, y1:0.960227, x2:0.892, y2:1, stop:0.170455 rgba(117, 255, 121, 182), stop:0.869318 rgba(172, 145, 201, 142));")

        self.horizontalLayout_3.addWidget(self.pushButton_choose_results_file)

        self.lineEdit_file_with_parsing_results = QLineEdit(self.Parsing)
        self.lineEdit_file_with_parsing_results.setObjectName(u"lineEdit_file_with_parsing_results")

        self.horizontalLayout_3.addWidget(self.lineEdit_file_with_parsing_results)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_choose_league = QLabel(self.Parsing)
        self.label_choose_league.setObjectName(u"label_choose_league")

        self.verticalLayout.addWidget(self.label_choose_league)

        self.comboBox_choose_league = QComboBox(self.Parsing)
        self.comboBox_choose_league.setObjectName(u"comboBox_choose_league")

        self.verticalLayout.addWidget(self.comboBox_choose_league)

        self.label_choose_season = QLabel(self.Parsing)
        self.label_choose_season.setObjectName(u"label_choose_season")

        self.verticalLayout.addWidget(self.label_choose_season)

        self.comboBox_choose_season = QComboBox(self.Parsing)
        self.comboBox_choose_season.setObjectName(u"comboBox_choose_season")

        self.verticalLayout.addWidget(self.comboBox_choose_season)

        self.label_choose_team = QLabel(self.Parsing)
        self.label_choose_team.setObjectName(u"label_choose_team")

        self.verticalLayout.addWidget(self.label_choose_team)

        self.comboBox_choose_team = QComboBox(self.Parsing)
        self.comboBox_choose_team.setObjectName(u"comboBox_choose_team")

        self.verticalLayout.addWidget(self.comboBox_choose_team)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_parse_results = QPushButton(self.Parsing)
        self.pushButton_parse_results.setObjectName(u"pushButton_parse_results")
        self.pushButton_parse_results.setMinimumSize(QSize(150, 0))
        self.pushButton_parse_results.setMaximumSize(QSize(150, 16777215))
        self.pushButton_parse_results.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.006, y1:0.142045, x2:0.671, y2:0.505682, stop:0.181818 rgba(26, 168, 181, 221), stop:0.448864 rgba(85, 255, 127, 238), stop:0.903409 rgba(255, 169, 169, 255))")

        self.horizontalLayout.addWidget(self.pushButton_parse_results)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit_parsing_information = QTextEdit(self.Parsing)
        self.textEdit_parsing_information.setObjectName(u"textEdit_parsing_information")

        self.verticalLayout.addWidget(self.textEdit_parsing_information)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.CorrelationTab.addTab(self.Parsing, "")
        self.LastGames = QWidget()
        self.LastGames.setObjectName(u"LastGames")
        self.verticalLayout_4 = QVBoxLayout(self.LastGames)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tableWidget_LastGamesAvg = QTableWidget(self.LastGames)
        self.tableWidget_LastGamesAvg.setObjectName(u"tableWidget_LastGamesAvg")
        self.tableWidget_LastGamesAvg.setMaximumSize(QSize(16777215, 55))
        self.tableWidget_LastGamesAvg.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_LastGamesAvg.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_LastGamesAvg.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_LastGamesAvg.setGridStyle(Qt.DashDotLine)
        self.tableWidget_LastGamesAvg.verticalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_11.addWidget(self.tableWidget_LastGamesAvg)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_font_lastGames = QLabel(self.LastGames)
        self.label_font_lastGames.setObjectName(u"label_font_lastGames")
        self.label_font_lastGames.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_font_lastGames)

        self.horizontalSlider_font_lastGames = QSlider(self.LastGames)
        self.horizontalSlider_font_lastGames.setObjectName(u"horizontalSlider_font_lastGames")
        self.horizontalSlider_font_lastGames.setMinimum(6)
        self.horizontalSlider_font_lastGames.setMaximum(20)
        self.horizontalSlider_font_lastGames.setValue(10)
        self.horizontalSlider_font_lastGames.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.horizontalSlider_font_lastGames)

        self.lcdNumber_font_lastGames = QLCDNumber(self.LastGames)
        self.lcdNumber_font_lastGames.setObjectName(u"lcdNumber_font_lastGames")
        self.lcdNumber_font_lastGames.setMaximumSize(QSize(40, 40))
        self.lcdNumber_font_lastGames.setDigitCount(2)
        self.lcdNumber_font_lastGames.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber_font_lastGames.setProperty("value", 10.000000000000000)
        self.lcdNumber_font_lastGames.setProperty("intValue", 10)

        self.horizontalLayout_10.addWidget(self.lcdNumber_font_lastGames)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.groupBox_3 = QGroupBox(self.LastGames)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(150, 0))
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_LastGames_choose_league = QLabel(self.groupBox_3)
        self.label_LastGames_choose_league.setObjectName(u"label_LastGames_choose_league")

        self.horizontalLayout_14.addWidget(self.label_LastGames_choose_league)

        self.comboBox_LastGames_choose_league = QComboBox(self.groupBox_3)
        self.comboBox_LastGames_choose_league.setObjectName(u"comboBox_LastGames_choose_league")
        self.comboBox_LastGames_choose_league.setMinimumSize(QSize(150, 0))
        self.comboBox_LastGames_choose_league.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_14.addWidget(self.comboBox_LastGames_choose_league)

        self.label_LastGames_choose_team = QLabel(self.groupBox_3)
        self.label_LastGames_choose_team.setObjectName(u"label_LastGames_choose_team")

        self.horizontalLayout_14.addWidget(self.label_LastGames_choose_team)

        self.comboBox_LastGames_choose_team = QComboBox(self.groupBox_3)
        self.comboBox_LastGames_choose_team.setObjectName(u"comboBox_LastGames_choose_team")
        self.comboBox_LastGames_choose_team.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_14.addWidget(self.comboBox_LastGames_choose_team)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_9)

        self.spinBox_games_ammount_to_show = QSpinBox(self.groupBox_3)
        self.spinBox_games_ammount_to_show.setObjectName(u"spinBox_games_ammount_to_show")

        self.horizontalLayout_14.addWidget(self.spinBox_games_ammount_to_show)

        self.pushButton_show_LastGames_details = QPushButton(self.groupBox_3)
        self.pushButton_show_LastGames_details.setObjectName(u"pushButton_show_LastGames_details")
        self.pushButton_show_LastGames_details.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0.824, y1:0.960227, x2:0.892, y2:1, stop:0.170455 rgba(117, 255, 121, 182), stop:0.869318 rgba(172, 145, 201, 142));")

        self.horizontalLayout_14.addWidget(self.pushButton_show_LastGames_details)


        self.horizontalLayout_10.addWidget(self.groupBox_3)

        self.groupBox_set_color = QGroupBox(self.LastGames)
        self.groupBox_set_color.setObjectName(u"groupBox_set_color")
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_set_color)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_save_colors = QPushButton(self.groupBox_set_color)
        self.pushButton_save_colors.setObjectName(u"pushButton_save_colors")
        self.pushButton_save_colors.setAutoFillBackground(False)
        self.pushButton_save_colors.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.horizontalLayout_13.addWidget(self.pushButton_save_colors)

        self.checkBox_use_standart_color = QCheckBox(self.groupBox_set_color)
        self.checkBox_use_standart_color.setObjectName(u"checkBox_use_standart_color")
        self.checkBox_use_standart_color.setChecked(True)

        self.horizontalLayout_13.addWidget(self.checkBox_use_standart_color)

        self.radioButton_set_color1 = QRadioButton(self.groupBox_set_color)
        self.radioButton_set_color1.setObjectName(u"radioButton_set_color1")
        self.radioButton_set_color1.setMaximumSize(QSize(14, 16777215))
        self.radioButton_set_color1.setChecked(True)

        self.horizontalLayout_13.addWidget(self.radioButton_set_color1)

        self.label_set_color1 = QLabel(self.groupBox_set_color)
        self.label_set_color1.setObjectName(u"label_set_color1")
        self.label_set_color1.setMinimumSize(QSize(20, 20))
        self.label_set_color1.setMaximumSize(QSize(20, 20))
        self.label_set_color1.setFrameShape(QFrame.Box)

        self.horizontalLayout_13.addWidget(self.label_set_color1)

        self.radioButton_set_color2 = QRadioButton(self.groupBox_set_color)
        self.radioButton_set_color2.setObjectName(u"radioButton_set_color2")

        self.horizontalLayout_13.addWidget(self.radioButton_set_color2)

        self.label_set_color2 = QLabel(self.groupBox_set_color)
        self.label_set_color2.setObjectName(u"label_set_color2")
        self.label_set_color2.setMinimumSize(QSize(20, 20))
        self.label_set_color2.setMaximumSize(QSize(20, 20))
        self.label_set_color2.setFrameShape(QFrame.Box)

        self.horizontalLayout_13.addWidget(self.label_set_color2)

        self.radioButton_set_color3 = QRadioButton(self.groupBox_set_color)
        self.radioButton_set_color3.setObjectName(u"radioButton_set_color3")

        self.horizontalLayout_13.addWidget(self.radioButton_set_color3)

        self.label_set_color3 = QLabel(self.groupBox_set_color)
        self.label_set_color3.setObjectName(u"label_set_color3")
        self.label_set_color3.setMinimumSize(QSize(20, 20))
        self.label_set_color3.setMaximumSize(QSize(20, 20))
        self.label_set_color3.setFrameShape(QFrame.Box)

        self.horizontalLayout_13.addWidget(self.label_set_color3)


        self.horizontalLayout_10.addWidget(self.groupBox_set_color)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayoutLastGames = QHBoxLayout()
        self.verticalLayoutLastGames.setObjectName(u"verticalLayoutLastGames")
        self.verticalLayoutLastGames.setSizeConstraint(QLayout.SetMaximumSize)
        self.TableWidget_LastGames = QTableWidget(self.LastGames)
        self.TableWidget_LastGames.setObjectName(u"TableWidget_LastGames")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TableWidget_LastGames.sizePolicy().hasHeightForWidth())
        self.TableWidget_LastGames.setSizePolicy(sizePolicy1)
        self.TableWidget_LastGames.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(8)
        self.TableWidget_LastGames.setFont(font)
        self.TableWidget_LastGames.setFrameShadow(QFrame.Raised)
        self.TableWidget_LastGames.setSortingEnabled(False)
        self.TableWidget_LastGames.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayoutLastGames.addWidget(self.TableWidget_LastGames)


        self.horizontalLayout_17.addLayout(self.verticalLayoutLastGames)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.CorrelationTab.addTab(self.LastGames, "")
        self.Tournament = QWidget()
        self.Tournament.setObjectName(u"Tournament")
        self.verticalLayout_2 = QVBoxLayout(self.Tournament)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_choose_league_for_turnament = QLabel(self.Tournament)
        self.label_choose_league_for_turnament.setObjectName(u"label_choose_league_for_turnament")
        self.label_choose_league_for_turnament.setMaximumSize(QSize(80, 16777215))

        self.verticalLayout_6.addWidget(self.label_choose_league_for_turnament)

        self.comboBo_choose_league_for_turnament = QComboBox(self.Tournament)
        self.comboBo_choose_league_for_turnament.setObjectName(u"comboBo_choose_league_for_turnament")
        self.comboBo_choose_league_for_turnament.setMaximumSize(QSize(190, 16777215))

        self.verticalLayout_6.addWidget(self.comboBo_choose_league_for_turnament)

        self.label_choose_season_for_turnament = QLabel(self.Tournament)
        self.label_choose_season_for_turnament.setObjectName(u"label_choose_season_for_turnament")
        self.label_choose_season_for_turnament.setMaximumSize(QSize(80, 16777215))

        self.verticalLayout_6.addWidget(self.label_choose_season_for_turnament)

        self.comboBox_choose_season_for_turnament = QComboBox(self.Tournament)
        self.comboBox_choose_season_for_turnament.setObjectName(u"comboBox_choose_season_for_turnament")
        self.comboBox_choose_season_for_turnament.setMaximumSize(QSize(190, 16777215))

        self.verticalLayout_6.addWidget(self.comboBox_choose_season_for_turnament)

        self.groupBox = QGroupBox(self.Tournament)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton_tournament_team = QRadioButton(self.groupBox)
        self.radioButton_tournament_team.setObjectName(u"radioButton_tournament_team")

        self.horizontalLayout_9.addWidget(self.radioButton_tournament_team)

        self.radioButton_tournament_oponent = QRadioButton(self.groupBox)
        self.radioButton_tournament_oponent.setObjectName(u"radioButton_tournament_oponent")

        self.horizontalLayout_9.addWidget(self.radioButton_tournament_oponent)

        self.radioButton_tournament_team_and_oponent = QRadioButton(self.groupBox)
        self.radioButton_tournament_team_and_oponent.setObjectName(u"radioButton_tournament_team_and_oponent")
        self.radioButton_tournament_team_and_oponent.setChecked(True)

        self.horizontalLayout_9.addWidget(self.radioButton_tournament_team_and_oponent)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.home_avay = QGroupBox(self.Tournament)
        self.home_avay.setObjectName(u"home_avay")
        self.home_avay.setEnabled(True)
        self.home_avay.setMinimumSize(QSize(0, 0))
        self.home_avay.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.home_avay)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton_tournament_home = QRadioButton(self.home_avay)
        self.radioButton_tournament_home.setObjectName(u"radioButton_tournament_home")

        self.horizontalLayout_8.addWidget(self.radioButton_tournament_home)

        self.radioButton_tournament_away = QRadioButton(self.home_avay)
        self.radioButton_tournament_away.setObjectName(u"radioButton_tournament_away")

        self.horizontalLayout_8.addWidget(self.radioButton_tournament_away)

        self.radioButton_tournament_home_and_away = QRadioButton(self.home_avay)
        self.radioButton_tournament_home_and_away.setObjectName(u"radioButton_tournament_home_and_away")
        self.radioButton_tournament_home_and_away.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radioButton_tournament_home_and_away)


        self.verticalLayout_6.addWidget(self.home_avay)

        self.pushButtonGetTournamentTable = QPushButton(self.Tournament)
        self.pushButtonGetTournamentTable.setObjectName(u"pushButtonGetTournamentTable")
        self.pushButtonGetTournamentTable.setMinimumSize(QSize(150, 39))
        self.pushButtonGetTournamentTable.setMaximumSize(QSize(190, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        self.pushButtonGetTournamentTable.setFont(font1)
        self.pushButtonGetTournamentTable.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.006, y1:0.142045, x2:0.671, y2:0.505682, stop:0.181818 rgba(26, 168, 181, 221), stop:0.448864 rgba(85, 255, 127, 238), stop:0.903409 rgba(255, 169, 169, 255))")

        self.verticalLayout_6.addWidget(self.pushButtonGetTournamentTable)

        self.label_font_Tournament = QLabel(self.Tournament)
        self.label_font_Tournament.setObjectName(u"label_font_Tournament")

        self.verticalLayout_6.addWidget(self.label_font_Tournament)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSlider_font_Tournament = QSlider(self.Tournament)
        self.horizontalSlider_font_Tournament.setObjectName(u"horizontalSlider_font_Tournament")
        self.horizontalSlider_font_Tournament.setMinimumSize(QSize(100, 0))
        self.horizontalSlider_font_Tournament.setMaximumSize(QSize(140, 16777215))
        self.horizontalSlider_font_Tournament.setMinimum(5)
        self.horizontalSlider_font_Tournament.setMaximum(15)
        self.horizontalSlider_font_Tournament.setValue(7)
        self.horizontalSlider_font_Tournament.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.horizontalSlider_font_Tournament)

        self.lcdNumber_font_Tournament = QLCDNumber(self.Tournament)
        self.lcdNumber_font_Tournament.setObjectName(u"lcdNumber_font_Tournament")
        self.lcdNumber_font_Tournament.setMinimumSize(QSize(40, 40))
        self.lcdNumber_font_Tournament.setMaximumSize(QSize(43, 16777215))
        font2 = QFont()
        font2.setBold(False)
        self.lcdNumber_font_Tournament.setFont(font2)
        self.lcdNumber_font_Tournament.setFrameShape(QFrame.Box)
        self.lcdNumber_font_Tournament.setFrameShadow(QFrame.Raised)
        self.lcdNumber_font_Tournament.setDigitCount(2)
        self.lcdNumber_font_Tournament.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber_font_Tournament.setProperty("value", 7.000000000000000)

        self.horizontalLayout_5.addWidget(self.lcdNumber_font_Tournament)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_18.addLayout(self.verticalLayout_6)

        self.tableWidget_tournament_table = QTableWidget(self.Tournament)
        self.tableWidget_tournament_table.setObjectName(u"tableWidget_tournament_table")
        self.tableWidget_tournament_table.setAutoScroll(False)
        self.tableWidget_tournament_table.setShowGrid(False)

        self.horizontalLayout_18.addWidget(self.tableWidget_tournament_table)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.CorrelationTab.addTab(self.Tournament, "")
        self.Model = QWidget()
        self.Model.setObjectName(u"Model")
        self.gridLayout = QGridLayout(self.Model)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_choose_prognose = QVBoxLayout()
        self.verticalLayout_choose_prognose.setObjectName(u"verticalLayout_choose_prognose")
        self.label_7 = QLabel(self.Model)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_choose_prognose.addWidget(self.label_7)

        self.comboBox_choose_league_prognose = QComboBox(self.Model)
        self.comboBox_choose_league_prognose.setObjectName(u"comboBox_choose_league_prognose")

        self.verticalLayout_choose_prognose.addWidget(self.comboBox_choose_league_prognose)

        self.label_choose_team_prognose = QLabel(self.Model)
        self.label_choose_team_prognose.setObjectName(u"label_choose_team_prognose")

        self.verticalLayout_choose_prognose.addWidget(self.label_choose_team_prognose)

        self.comboBox_choose_team_prognose = QComboBox(self.Model)
        self.comboBox_choose_team_prognose.setObjectName(u"comboBox_choose_team_prognose")

        self.verticalLayout_choose_prognose.addWidget(self.comboBox_choose_team_prognose)

        self.label_choose_opponent_prognose = QLabel(self.Model)
        self.label_choose_opponent_prognose.setObjectName(u"label_choose_opponent_prognose")

        self.verticalLayout_choose_prognose.addWidget(self.label_choose_opponent_prognose)

        self.comboBox_choose_opponent_prognose = QComboBox(self.Model)
        self.comboBox_choose_opponent_prognose.setObjectName(u"comboBox_choose_opponent_prognose")

        self.verticalLayout_choose_prognose.addWidget(self.comboBox_choose_opponent_prognose)

        self.label_4 = QLabel(self.Model)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_choose_prognose.addWidget(self.label_4)

        self.comboBox_param_to_predict = QComboBox(self.Model)
        self.comboBox_param_to_predict.setObjectName(u"comboBox_param_to_predict")

        self.verticalLayout_choose_prognose.addWidget(self.comboBox_param_to_predict)

        self.checkBox_homeflag_for_prognose = QCheckBox(self.Model)
        self.checkBox_homeflag_for_prognose.setObjectName(u"checkBox_homeflag_for_prognose")

        self.verticalLayout_choose_prognose.addWidget(self.checkBox_homeflag_for_prognose)

        self.label_next_play_date_prognose = QLabel(self.Model)
        self.label_next_play_date_prognose.setObjectName(u"label_next_play_date_prognose")

        self.verticalLayout_choose_prognose.addWidget(self.label_next_play_date_prognose)

        self.dateEdit_next_game_prognose = QDateEdit(self.Model)
        self.dateEdit_next_game_prognose.setObjectName(u"dateEdit_next_game_prognose")

        self.verticalLayout_choose_prognose.addWidget(self.dateEdit_next_game_prognose)

        self.label_2 = QLabel(self.Model)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_choose_prognose.addWidget(self.label_2)

        self.spinBox_days_backward_model = QSpinBox(self.Model)
        self.spinBox_days_backward_model.setObjectName(u"spinBox_days_backward_model")
        self.spinBox_days_backward_model.setKeyboardTracking(True)
        self.spinBox_days_backward_model.setMinimum(1)
        self.spinBox_days_backward_model.setMaximum(4000)
        self.spinBox_days_backward_model.setSingleStep(10)
        self.spinBox_days_backward_model.setValue(500)

        self.verticalLayout_choose_prognose.addWidget(self.spinBox_days_backward_model)

        self.label_3 = QLabel(self.Model)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_choose_prognose.addWidget(self.label_3)

        self.spinBox_days_backward_params = QSpinBox(self.Model)
        self.spinBox_days_backward_params.setObjectName(u"spinBox_days_backward_params")
        self.spinBox_days_backward_params.setMinimum(1)
        self.spinBox_days_backward_params.setMaximum(1000)
        self.spinBox_days_backward_params.setSingleStep(10)
        self.spinBox_days_backward_params.setValue(50)

        self.verticalLayout_choose_prognose.addWidget(self.spinBox_days_backward_params)

        self.groupBox_2 = QGroupBox(self.Model)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_predicted_param = QLabel(self.groupBox_2)
        self.label_predicted_param.setObjectName(u"label_predicted_param")

        self.verticalLayout_5.addWidget(self.label_predicted_param)

        self.lineEdit_predicted_value = QLineEdit(self.groupBox_2)
        self.lineEdit_predicted_value.setObjectName(u"lineEdit_predicted_value")

        self.verticalLayout_5.addWidget(self.lineEdit_predicted_value)


        self.verticalLayout_choose_prognose.addWidget(self.groupBox_2)

        self.pushButton_do_prognose = QPushButton(self.Model)
        self.pushButton_do_prognose.setObjectName(u"pushButton_do_prognose")
        self.pushButton_do_prognose.setMinimumSize(QSize(0, 40))
        self.pushButton_do_prognose.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.006, y1:0.142045, x2:0.671, y2:0.505682, stop:0.181818 rgba(26, 168, 181, 221), stop:0.448864 rgba(85, 255, 127, 238), stop:0.903409 rgba(255, 169, 169, 255))")

        self.verticalLayout_choose_prognose.addWidget(self.pushButton_do_prognose)

        self.verticalSpacer_choose_prognose = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_choose_prognose.addItem(self.verticalSpacer_choose_prognose)


        self.gridLayout.addLayout(self.verticalLayout_choose_prognose, 0, 0, 1, 1)

        self.verticalLayout_modeled_parameters = QVBoxLayout()
        self.verticalLayout_modeled_parameters.setObjectName(u"verticalLayout_modeled_parameters")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_for_mpl_model = QWidget(self.Model)
        self.widget_for_mpl_model.setObjectName(u"widget_for_mpl_model")
        self.widget_for_mpl_model.setMinimumSize(QSize(300, 300))
        self.widget_for_mpl_model.setMaximumSize(QSize(600, 600))

        self.horizontalLayout_4.addWidget(self.widget_for_mpl_model)

        self.widget_for_mpl_param_distrib = QWidget(self.Model)
        self.widget_for_mpl_param_distrib.setObjectName(u"widget_for_mpl_param_distrib")
        self.widget_for_mpl_param_distrib.setMinimumSize(QSize(300, 300))
        self.widget_for_mpl_param_distrib.setMaximumSize(QSize(600, 600))

        self.horizontalLayout_4.addWidget(self.widget_for_mpl_param_distrib)


        self.verticalLayout_modeled_parameters.addLayout(self.horizontalLayout_4)

        self.label_parameters_view = QLabel(self.Model)
        self.label_parameters_view.setObjectName(u"label_parameters_view")

        self.verticalLayout_modeled_parameters.addWidget(self.label_parameters_view)

        self.horizontalLayout_team_model_param = QHBoxLayout()
        self.horizontalLayout_team_model_param.setObjectName(u"horizontalLayout_team_model_param")
        self.verticalLayout_PTS1 = QVBoxLayout()
        self.verticalLayout_PTS1.setObjectName(u"verticalLayout_PTS1")
        self.label_PTS1 = QLabel(self.Model)
        self.label_PTS1.setObjectName(u"label_PTS1")
        self.label_PTS1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_PTS1.addWidget(self.label_PTS1)

        self.lineEdit_PTS1 = QLineEdit(self.Model)
        self.lineEdit_PTS1.setObjectName(u"lineEdit_PTS1")

        self.verticalLayout_PTS1.addWidget(self.lineEdit_PTS1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_PTS1)

        self.verticalLayou_3P1 = QVBoxLayout()
        self.verticalLayou_3P1.setObjectName(u"verticalLayou_3P1")
        self.label_3P1 = QLabel(self.Model)
        self.label_3P1.setObjectName(u"label_3P1")
        self.label_3P1.setAlignment(Qt.AlignCenter)

        self.verticalLayou_3P1.addWidget(self.label_3P1)

        self.lineEdit_3P1 = QLineEdit(self.Model)
        self.lineEdit_3P1.setObjectName(u"lineEdit_3P1")

        self.verticalLayou_3P1.addWidget(self.lineEdit_3P1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayou_3P1)

        self.verticalLayout_3PA1 = QVBoxLayout()
        self.verticalLayout_3PA1.setObjectName(u"verticalLayout_3PA1")
        self.label_3PA1 = QLabel(self.Model)
        self.label_3PA1.setObjectName(u"label_3PA1")
        self.label_3PA1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3PA1.addWidget(self.label_3PA1)

        self.lineEdit_3PA1 = QLineEdit(self.Model)
        self.lineEdit_3PA1.setObjectName(u"lineEdit_3PA1")

        self.verticalLayout_3PA1.addWidget(self.lineEdit_3PA1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_3PA1)

        self.verticalLayout_3PP1 = QVBoxLayout()
        self.verticalLayout_3PP1.setObjectName(u"verticalLayout_3PP1")
        self.label_3PP1 = QLabel(self.Model)
        self.label_3PP1.setObjectName(u"label_3PP1")
        self.label_3PP1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3PP1.addWidget(self.label_3PP1)

        self.lineEdit_3PP1 = QLineEdit(self.Model)
        self.lineEdit_3PP1.setObjectName(u"lineEdit_3PP1")

        self.verticalLayout_3PP1.addWidget(self.lineEdit_3PP1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_3PP1)

        self.verticalLayout_2P1 = QVBoxLayout()
        self.verticalLayout_2P1.setObjectName(u"verticalLayout_2P1")
        self.label_2P1 = QLabel(self.Model)
        self.label_2P1.setObjectName(u"label_2P1")
        self.label_2P1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2P1.addWidget(self.label_2P1)

        self.lineEdit_2P1 = QLineEdit(self.Model)
        self.lineEdit_2P1.setObjectName(u"lineEdit_2P1")

        self.verticalLayout_2P1.addWidget(self.lineEdit_2P1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_2P1)

        self.verticalLayout_2PA1 = QVBoxLayout()
        self.verticalLayout_2PA1.setObjectName(u"verticalLayout_2PA1")
        self.label_2PA1 = QLabel(self.Model)
        self.label_2PA1.setObjectName(u"label_2PA1")
        self.label_2PA1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2PA1.addWidget(self.label_2PA1)

        self.lineEdit_2PA1 = QLineEdit(self.Model)
        self.lineEdit_2PA1.setObjectName(u"lineEdit_2PA1")

        self.verticalLayout_2PA1.addWidget(self.lineEdit_2PA1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_2PA1)

        self.verticalLayout_2PP1 = QVBoxLayout()
        self.verticalLayout_2PP1.setObjectName(u"verticalLayout_2PP1")
        self.label_2PP1 = QLabel(self.Model)
        self.label_2PP1.setObjectName(u"label_2PP1")
        self.label_2PP1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2PP1.addWidget(self.label_2PP1)

        self.lineEdit_2PP1 = QLineEdit(self.Model)
        self.lineEdit_2PP1.setObjectName(u"lineEdit_2PP1")

        self.verticalLayout_2PP1.addWidget(self.lineEdit_2PP1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_2PP1)

        self.verticalLayout_FT1 = QVBoxLayout()
        self.verticalLayout_FT1.setObjectName(u"verticalLayout_FT1")
        self.label_FT1 = QLabel(self.Model)
        self.label_FT1.setObjectName(u"label_FT1")
        self.label_FT1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_FT1.addWidget(self.label_FT1)

        self.lineEdit_FT1 = QLineEdit(self.Model)
        self.lineEdit_FT1.setObjectName(u"lineEdit_FT1")

        self.verticalLayout_FT1.addWidget(self.lineEdit_FT1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_FT1)

        self.verticalLayout_FTA1 = QVBoxLayout()
        self.verticalLayout_FTA1.setObjectName(u"verticalLayout_FTA1")
        self.label_FTA1 = QLabel(self.Model)
        self.label_FTA1.setObjectName(u"label_FTA1")
        self.label_FTA1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_FTA1.addWidget(self.label_FTA1)

        self.lineEdit_FTA1 = QLineEdit(self.Model)
        self.lineEdit_FTA1.setObjectName(u"lineEdit_FTA1")

        self.verticalLayout_FTA1.addWidget(self.lineEdit_FTA1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_FTA1)

        self.verticalLayout_FTP1 = QVBoxLayout()
        self.verticalLayout_FTP1.setObjectName(u"verticalLayout_FTP1")
        self.label_FTP1 = QLabel(self.Model)
        self.label_FTP1.setObjectName(u"label_FTP1")
        self.label_FTP1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_FTP1.addWidget(self.label_FTP1)

        self.lineEdit_FTP1 = QLineEdit(self.Model)
        self.lineEdit_FTP1.setObjectName(u"lineEdit_FTP1")

        self.verticalLayout_FTP1.addWidget(self.lineEdit_FTP1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_FTP1)

        self.verticalLayout_ORB1 = QVBoxLayout()
        self.verticalLayout_ORB1.setObjectName(u"verticalLayout_ORB1")
        self.label_ORB1 = QLabel(self.Model)
        self.label_ORB1.setObjectName(u"label_ORB1")
        self.label_ORB1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_ORB1.addWidget(self.label_ORB1)

        self.lineEdit_ORB1 = QLineEdit(self.Model)
        self.lineEdit_ORB1.setObjectName(u"lineEdit_ORB1")

        self.verticalLayout_ORB1.addWidget(self.lineEdit_ORB1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_ORB1)

        self.verticalLayout_DRB1 = QVBoxLayout()
        self.verticalLayout_DRB1.setObjectName(u"verticalLayout_DRB1")
        self.label_DRB1 = QLabel(self.Model)
        self.label_DRB1.setObjectName(u"label_DRB1")
        self.label_DRB1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_DRB1.addWidget(self.label_DRB1)

        self.lineEdit_DRB1 = QLineEdit(self.Model)
        self.lineEdit_DRB1.setObjectName(u"lineEdit_DRB1")

        self.verticalLayout_DRB1.addWidget(self.lineEdit_DRB1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_DRB1)

        self.verticalLayout_TRB1 = QVBoxLayout()
        self.verticalLayout_TRB1.setObjectName(u"verticalLayout_TRB1")
        self.label_TRB1 = QLabel(self.Model)
        self.label_TRB1.setObjectName(u"label_TRB1")
        self.label_TRB1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_TRB1.addWidget(self.label_TRB1)

        self.lineEdit_TRB1 = QLineEdit(self.Model)
        self.lineEdit_TRB1.setObjectName(u"lineEdit_TRB1")

        self.verticalLayout_TRB1.addWidget(self.lineEdit_TRB1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_TRB1)

        self.verticalLayout_AST1 = QVBoxLayout()
        self.verticalLayout_AST1.setObjectName(u"verticalLayout_AST1")
        self.label_AST1 = QLabel(self.Model)
        self.label_AST1.setObjectName(u"label_AST1")
        self.label_AST1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_AST1.addWidget(self.label_AST1)

        self.lineEdit_AST1 = QLineEdit(self.Model)
        self.lineEdit_AST1.setObjectName(u"lineEdit_AST1")

        self.verticalLayout_AST1.addWidget(self.lineEdit_AST1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_AST1)

        self.verticalLayout_STL1 = QVBoxLayout()
        self.verticalLayout_STL1.setObjectName(u"verticalLayout_STL1")
        self.label_STL1 = QLabel(self.Model)
        self.label_STL1.setObjectName(u"label_STL1")
        self.label_STL1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_STL1.addWidget(self.label_STL1)

        self.lineEdit_STL1 = QLineEdit(self.Model)
        self.lineEdit_STL1.setObjectName(u"lineEdit_STL1")

        self.verticalLayout_STL1.addWidget(self.lineEdit_STL1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_STL1)

        self.verticalLayout_BLK1 = QVBoxLayout()
        self.verticalLayout_BLK1.setObjectName(u"verticalLayout_BLK1")
        self.label_BLK1 = QLabel(self.Model)
        self.label_BLK1.setObjectName(u"label_BLK1")
        self.label_BLK1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_BLK1.addWidget(self.label_BLK1)

        self.lineEdit_BLK1 = QLineEdit(self.Model)
        self.lineEdit_BLK1.setObjectName(u"lineEdit_BLK1")

        self.verticalLayout_BLK1.addWidget(self.lineEdit_BLK1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_BLK1)

        self.verticalLayout_TOV1 = QVBoxLayout()
        self.verticalLayout_TOV1.setObjectName(u"verticalLayout_TOV1")
        self.label_TOV1 = QLabel(self.Model)
        self.label_TOV1.setObjectName(u"label_TOV1")
        self.label_TOV1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_TOV1.addWidget(self.label_TOV1)

        self.lineEdit_TOV1 = QLineEdit(self.Model)
        self.lineEdit_TOV1.setObjectName(u"lineEdit_TOV1")

        self.verticalLayout_TOV1.addWidget(self.lineEdit_TOV1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_TOV1)

        self.verticalLayout_F1 = QVBoxLayout()
        self.verticalLayout_F1.setObjectName(u"verticalLayout_F1")
        self.label_F1 = QLabel(self.Model)
        self.label_F1.setObjectName(u"label_F1")
        self.label_F1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_F1.addWidget(self.label_F1)

        self.lineEdit_F1 = QLineEdit(self.Model)
        self.lineEdit_F1.setObjectName(u"lineEdit_F1")

        self.verticalLayout_F1.addWidget(self.lineEdit_F1)


        self.horizontalLayout_team_model_param.addLayout(self.verticalLayout_F1)


        self.verticalLayout_modeled_parameters.addLayout(self.horizontalLayout_team_model_param)

        self.horizontalLayout_op_team_model_param = QHBoxLayout()
        self.horizontalLayout_op_team_model_param.setObjectName(u"horizontalLayout_op_team_model_param")
        self.verticalLayout_PTS2 = QVBoxLayout()
        self.verticalLayout_PTS2.setObjectName(u"verticalLayout_PTS2")
        self.label_PTS2 = QLabel(self.Model)
        self.label_PTS2.setObjectName(u"label_PTS2")
        self.label_PTS2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_PTS2.addWidget(self.label_PTS2)

        self.lineEdit_PTS2 = QLineEdit(self.Model)
        self.lineEdit_PTS2.setObjectName(u"lineEdit_PTS2")

        self.verticalLayout_PTS2.addWidget(self.lineEdit_PTS2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_PTS2)

        self.verticalLayout_3P2 = QVBoxLayout()
        self.verticalLayout_3P2.setObjectName(u"verticalLayout_3P2")
        self.label_3P2 = QLabel(self.Model)
        self.label_3P2.setObjectName(u"label_3P2")
        self.label_3P2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3P2.addWidget(self.label_3P2)

        self.lineEdit_3P2 = QLineEdit(self.Model)
        self.lineEdit_3P2.setObjectName(u"lineEdit_3P2")

        self.verticalLayout_3P2.addWidget(self.lineEdit_3P2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_3P2)

        self.verticalLayout_3PA2 = QVBoxLayout()
        self.verticalLayout_3PA2.setObjectName(u"verticalLayout_3PA2")
        self.label_3PA2 = QLabel(self.Model)
        self.label_3PA2.setObjectName(u"label_3PA2")
        self.label_3PA2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3PA2.addWidget(self.label_3PA2)

        self.lineEdit_3PA2 = QLineEdit(self.Model)
        self.lineEdit_3PA2.setObjectName(u"lineEdit_3PA2")

        self.verticalLayout_3PA2.addWidget(self.lineEdit_3PA2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_3PA2)

        self.verticalLayout_3PP2 = QVBoxLayout()
        self.verticalLayout_3PP2.setObjectName(u"verticalLayout_3PP2")
        self.label_3PP2 = QLabel(self.Model)
        self.label_3PP2.setObjectName(u"label_3PP2")
        self.label_3PP2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3PP2.addWidget(self.label_3PP2)

        self.lineEdit_3PP2 = QLineEdit(self.Model)
        self.lineEdit_3PP2.setObjectName(u"lineEdit_3PP2")

        self.verticalLayout_3PP2.addWidget(self.lineEdit_3PP2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_3PP2)

        self.verticalLayout_2P2 = QVBoxLayout()
        self.verticalLayout_2P2.setObjectName(u"verticalLayout_2P2")
        self.label_2P2 = QLabel(self.Model)
        self.label_2P2.setObjectName(u"label_2P2")
        self.label_2P2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2P2.addWidget(self.label_2P2)

        self.lineEdit_2P2 = QLineEdit(self.Model)
        self.lineEdit_2P2.setObjectName(u"lineEdit_2P2")

        self.verticalLayout_2P2.addWidget(self.lineEdit_2P2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_2P2)

        self.verticalLayout_2PA2 = QVBoxLayout()
        self.verticalLayout_2PA2.setObjectName(u"verticalLayout_2PA2")
        self.label_2PA2 = QLabel(self.Model)
        self.label_2PA2.setObjectName(u"label_2PA2")
        self.label_2PA2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2PA2.addWidget(self.label_2PA2)

        self.lineEdit_2PA2 = QLineEdit(self.Model)
        self.lineEdit_2PA2.setObjectName(u"lineEdit_2PA2")

        self.verticalLayout_2PA2.addWidget(self.lineEdit_2PA2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_2PA2)

        self.verticalLayout_2PP2 = QVBoxLayout()
        self.verticalLayout_2PP2.setObjectName(u"verticalLayout_2PP2")
        self.label_2PP2 = QLabel(self.Model)
        self.label_2PP2.setObjectName(u"label_2PP2")
        self.label_2PP2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2PP2.addWidget(self.label_2PP2)

        self.lineEdit_2PP2 = QLineEdit(self.Model)
        self.lineEdit_2PP2.setObjectName(u"lineEdit_2PP2")

        self.verticalLayout_2PP2.addWidget(self.lineEdit_2PP2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_2PP2)

        self.verticalLayout_FT2 = QVBoxLayout()
        self.verticalLayout_FT2.setObjectName(u"verticalLayout_FT2")
        self.label_FT2 = QLabel(self.Model)
        self.label_FT2.setObjectName(u"label_FT2")
        self.label_FT2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_FT2.addWidget(self.label_FT2)

        self.lineEdit_FT2 = QLineEdit(self.Model)
        self.lineEdit_FT2.setObjectName(u"lineEdit_FT2")

        self.verticalLayout_FT2.addWidget(self.lineEdit_FT2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_FT2)

        self.verticalLayout_FTA2 = QVBoxLayout()
        self.verticalLayout_FTA2.setObjectName(u"verticalLayout_FTA2")
        self.label_FTA2 = QLabel(self.Model)
        self.label_FTA2.setObjectName(u"label_FTA2")
        self.label_FTA2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_FTA2.addWidget(self.label_FTA2)

        self.lineEdit_FTA2 = QLineEdit(self.Model)
        self.lineEdit_FTA2.setObjectName(u"lineEdit_FTA2")

        self.verticalLayout_FTA2.addWidget(self.lineEdit_FTA2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_FTA2)

        self.verticalLayout_FTP2 = QVBoxLayout()
        self.verticalLayout_FTP2.setObjectName(u"verticalLayout_FTP2")
        self.label_FTP2 = QLabel(self.Model)
        self.label_FTP2.setObjectName(u"label_FTP2")
        self.label_FTP2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_FTP2.addWidget(self.label_FTP2)

        self.lineEdit_FTP2 = QLineEdit(self.Model)
        self.lineEdit_FTP2.setObjectName(u"lineEdit_FTP2")

        self.verticalLayout_FTP2.addWidget(self.lineEdit_FTP2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_FTP2)

        self.verticalLayout_DRB2 = QVBoxLayout()
        self.verticalLayout_DRB2.setObjectName(u"verticalLayout_DRB2")
        self.label_DRB2 = QLabel(self.Model)
        self.label_DRB2.setObjectName(u"label_DRB2")
        self.label_DRB2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_DRB2.addWidget(self.label_DRB2)

        self.lineEdit_DRB2 = QLineEdit(self.Model)
        self.lineEdit_DRB2.setObjectName(u"lineEdit_DRB2")

        self.verticalLayout_DRB2.addWidget(self.lineEdit_DRB2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_DRB2)

        self.verticalLayout_ORB2 = QVBoxLayout()
        self.verticalLayout_ORB2.setObjectName(u"verticalLayout_ORB2")
        self.label_ORB2 = QLabel(self.Model)
        self.label_ORB2.setObjectName(u"label_ORB2")
        self.label_ORB2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_ORB2.addWidget(self.label_ORB2)

        self.lineEdit_ORB2 = QLineEdit(self.Model)
        self.lineEdit_ORB2.setObjectName(u"lineEdit_ORB2")

        self.verticalLayout_ORB2.addWidget(self.lineEdit_ORB2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_ORB2)

        self.verticalLayout_TRB2 = QVBoxLayout()
        self.verticalLayout_TRB2.setObjectName(u"verticalLayout_TRB2")
        self.label_TRB2 = QLabel(self.Model)
        self.label_TRB2.setObjectName(u"label_TRB2")
        self.label_TRB2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_TRB2.addWidget(self.label_TRB2)

        self.lineEdit_TRB2 = QLineEdit(self.Model)
        self.lineEdit_TRB2.setObjectName(u"lineEdit_TRB2")

        self.verticalLayout_TRB2.addWidget(self.lineEdit_TRB2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_TRB2)

        self.verticalLayout_AST2 = QVBoxLayout()
        self.verticalLayout_AST2.setObjectName(u"verticalLayout_AST2")
        self.label_AST2 = QLabel(self.Model)
        self.label_AST2.setObjectName(u"label_AST2")
        self.label_AST2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_AST2.addWidget(self.label_AST2)

        self.lineEdit_AST2 = QLineEdit(self.Model)
        self.lineEdit_AST2.setObjectName(u"lineEdit_AST2")

        self.verticalLayout_AST2.addWidget(self.lineEdit_AST2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_AST2)

        self.verticalLayout_STL2 = QVBoxLayout()
        self.verticalLayout_STL2.setObjectName(u"verticalLayout_STL2")
        self.label_STL2 = QLabel(self.Model)
        self.label_STL2.setObjectName(u"label_STL2")
        self.label_STL2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_STL2.addWidget(self.label_STL2)

        self.lineEdit_STL2 = QLineEdit(self.Model)
        self.lineEdit_STL2.setObjectName(u"lineEdit_STL2")

        self.verticalLayout_STL2.addWidget(self.lineEdit_STL2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_STL2)

        self.verticalLayout_BLK2 = QVBoxLayout()
        self.verticalLayout_BLK2.setObjectName(u"verticalLayout_BLK2")
        self.label_BLK2 = QLabel(self.Model)
        self.label_BLK2.setObjectName(u"label_BLK2")
        self.label_BLK2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_BLK2.addWidget(self.label_BLK2)

        self.lineEdit_BLK2 = QLineEdit(self.Model)
        self.lineEdit_BLK2.setObjectName(u"lineEdit_BLK2")

        self.verticalLayout_BLK2.addWidget(self.lineEdit_BLK2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_BLK2)

        self.verticalLayout_TOV2 = QVBoxLayout()
        self.verticalLayout_TOV2.setObjectName(u"verticalLayout_TOV2")
        self.label_TOV2 = QLabel(self.Model)
        self.label_TOV2.setObjectName(u"label_TOV2")
        self.label_TOV2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_TOV2.addWidget(self.label_TOV2)

        self.lineEdit_TOV2 = QLineEdit(self.Model)
        self.lineEdit_TOV2.setObjectName(u"lineEdit_TOV2")

        self.verticalLayout_TOV2.addWidget(self.lineEdit_TOV2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_TOV2)

        self.verticalLayout_F2 = QVBoxLayout()
        self.verticalLayout_F2.setObjectName(u"verticalLayout_F2")
        self.label_F2 = QLabel(self.Model)
        self.label_F2.setObjectName(u"label_F2")
        self.label_F2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_F2.addWidget(self.label_F2)

        self.lineEdit_F2 = QLineEdit(self.Model)
        self.lineEdit_F2.setObjectName(u"lineEdit_F2")

        self.verticalLayout_F2.addWidget(self.lineEdit_F2)


        self.horizontalLayout_op_team_model_param.addLayout(self.verticalLayout_F2)


        self.verticalLayout_modeled_parameters.addLayout(self.horizontalLayout_op_team_model_param)

        self.horizontalLayout_generl_param = QHBoxLayout()
        self.horizontalLayout_generl_param.setObjectName(u"horizontalLayout_generl_param")
        self.verticalLayout_totalscore = QVBoxLayout()
        self.verticalLayout_totalscore.setObjectName(u"verticalLayout_totalscore")
        self.label_totalscore = QLabel(self.Model)
        self.label_totalscore.setObjectName(u"label_totalscore")
        self.label_totalscore.setMaximumSize(QSize(60, 16777215))
        self.label_totalscore.setAlignment(Qt.AlignCenter)

        self.verticalLayout_totalscore.addWidget(self.label_totalscore)

        self.lineEdit_totalscore = QLineEdit(self.Model)
        self.lineEdit_totalscore.setObjectName(u"lineEdit_totalscore")
        self.lineEdit_totalscore.setMaximumSize(QSize(60, 16777215))

        self.verticalLayout_totalscore.addWidget(self.lineEdit_totalscore)


        self.horizontalLayout_generl_param.addLayout(self.verticalLayout_totalscore)

        self.horizontalSpacer_3 = QSpacerItem(600, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_generl_param.addItem(self.horizontalSpacer_3)


        self.verticalLayout_modeled_parameters.addLayout(self.horizontalLayout_generl_param)


        self.gridLayout.addLayout(self.verticalLayout_modeled_parameters, 0, 1, 1, 1)

        self.CorrelationTab.addTab(self.Model, "")
        self.Correlations = QWidget()
        self.Correlations.setObjectName(u"Correlations")
        self.horizontalLayout_19 = QHBoxLayout(self.Correlations)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widget_for_statistics = QWidget(self.Correlations)
        self.widget_for_statistics.setObjectName(u"widget_for_statistics")
        self.widget_for_statistics.setMinimumSize(QSize(300, 300))
        self.widget_for_statistics.setMaximumSize(QSize(100000, 100000))

        self.horizontalLayout_19.addWidget(self.widget_for_statistics)

        self.CorrelationTab.addTab(self.Correlations, "")

        self.verticalLayout_central_layout.addWidget(self.CorrelationTab)


        self.horizontalLayout_6.addLayout(self.verticalLayout_central_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1314, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.CorrelationTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Update_parsing_assignment_file.setText(QCoreApplication.translate("MainWindow", u"Update Parsing Assignment file", None))
        self.label_file_with_parcing_assignment.setText(QCoreApplication.translate("MainWindow", u"Choose file with parsing assignment", None))
        self.pushButton_choose_assignment_file.setText(QCoreApplication.translate("MainWindow", u"Choose assignment file", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Choose file with parsing results (it used for database for farther analysis)", None))
        self.pushButton_choose_results_file.setText(QCoreApplication.translate("MainWindow", u"Choose results file", None))
        self.label_choose_league.setText(QCoreApplication.translate("MainWindow", u"Choose League", None))
        self.label_choose_season.setText(QCoreApplication.translate("MainWindow", u"Choose Season", None))
        self.label_choose_team.setText(QCoreApplication.translate("MainWindow", u"Choose Team", None))
        self.pushButton_parse_results.setText(QCoreApplication.translate("MainWindow", u"Parse selected categories", None))
        self.CorrelationTab.setTabText(self.CorrelationTab.indexOf(self.Parsing), QCoreApplication.translate("MainWindow", u"Parsing", None))
        self.label_font_lastGames.setText(QCoreApplication.translate("MainWindow", u"Fontsize", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Choose team and quantity of previous games", None))
        self.label_LastGames_choose_league.setText(QCoreApplication.translate("MainWindow", u"Choose league", None))
        self.label_LastGames_choose_team.setText(QCoreApplication.translate("MainWindow", u"Choose team", None))
        self.pushButton_show_LastGames_details.setText(QCoreApplication.translate("MainWindow", u"Show games", None))
        self.groupBox_set_color.setTitle(QCoreApplication.translate("MainWindow", u"Choose color", None))
        self.pushButton_save_colors.setText(QCoreApplication.translate("MainWindow", u"Save colors", None))
        self.checkBox_use_standart_color.setText(QCoreApplication.translate("MainWindow", u"use standart color", None))
        self.radioButton_set_color1.setText("")
        self.label_set_color1.setText("")
        self.radioButton_set_color2.setText("")
        self.label_set_color2.setText("")
        self.radioButton_set_color3.setText("")
        self.label_set_color3.setText("")
        self.CorrelationTab.setTabText(self.CorrelationTab.indexOf(self.LastGames), QCoreApplication.translate("MainWindow", u"LastGames", None))
        self.label_choose_league_for_turnament.setText(QCoreApplication.translate("MainWindow", u"Choose league", None))
        self.label_choose_season_for_turnament.setText(QCoreApplication.translate("MainWindow", u"Choose season", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Choose show type", None))
        self.radioButton_tournament_team.setText(QCoreApplication.translate("MainWindow", u"Team", None))
        self.radioButton_tournament_oponent.setText(QCoreApplication.translate("MainWindow", u"Opponent", None))
        self.radioButton_tournament_team_and_oponent.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.home_avay.setTitle(QCoreApplication.translate("MainWindow", u"Choose field type", None))
        self.radioButton_tournament_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.radioButton_tournament_away.setText(QCoreApplication.translate("MainWindow", u"Away", None))
        self.radioButton_tournament_home_and_away.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.pushButtonGetTournamentTable.setText(QCoreApplication.translate("MainWindow", u"Get tournament", None))
        self.label_font_Tournament.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.CorrelationTab.setTabText(self.CorrelationTab.indexOf(self.Tournament), QCoreApplication.translate("MainWindow", u"Tournament", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Choose League", None))
        self.label_choose_team_prognose.setText(QCoreApplication.translate("MainWindow", u"Choose Team", None))
        self.label_choose_opponent_prognose.setText(QCoreApplication.translate("MainWindow", u"Choose opponent", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Choose param to predict", None))
        self.checkBox_homeflag_for_prognose.setText(QCoreApplication.translate("MainWindow", u"Home falg", None))
        self.label_next_play_date_prognose.setText(QCoreApplication.translate("MainWindow", u"Next play date", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Days backward for model", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Days backward for parameters", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Results of prediction", None))
        self.label_predicted_param.setText("")
        self.pushButton_do_prognose.setText(QCoreApplication.translate("MainWindow", u"Make prediction", None))
        self.label_parameters_view.setText(QCoreApplication.translate("MainWindow", u"Parameters of next play acepted for prediction", None))
        self.label_PTS1.setText(QCoreApplication.translate("MainWindow", u"PTS #1", None))
        self.label_3P1.setText(QCoreApplication.translate("MainWindow", u"3P #1", None))
        self.label_3PA1.setText(QCoreApplication.translate("MainWindow", u"3PA #1", None))
        self.label_3PP1.setText(QCoreApplication.translate("MainWindow", u"3P% #1", None))
        self.label_2P1.setText(QCoreApplication.translate("MainWindow", u"2P #1", None))
        self.label_2PA1.setText(QCoreApplication.translate("MainWindow", u"2PA #1", None))
        self.label_2PP1.setText(QCoreApplication.translate("MainWindow", u"2P% #1", None))
        self.label_FT1.setText(QCoreApplication.translate("MainWindow", u"FT #1", None))
        self.label_FTA1.setText(QCoreApplication.translate("MainWindow", u"FTA #1", None))
        self.label_FTP1.setText(QCoreApplication.translate("MainWindow", u"FT% #1", None))
        self.label_ORB1.setText(QCoreApplication.translate("MainWindow", u"ORB #1", None))
        self.label_DRB1.setText(QCoreApplication.translate("MainWindow", u"DRB #1", None))
        self.label_TRB1.setText(QCoreApplication.translate("MainWindow", u"TRB #1", None))
        self.label_AST1.setText(QCoreApplication.translate("MainWindow", u"AST #1", None))
        self.label_STL1.setText(QCoreApplication.translate("MainWindow", u"STL #1", None))
        self.label_BLK1.setText(QCoreApplication.translate("MainWindow", u"BLK #1", None))
        self.label_TOV1.setText(QCoreApplication.translate("MainWindow", u"TOV #1", None))
        self.label_F1.setText(QCoreApplication.translate("MainWindow", u"F #1", None))
        self.label_PTS2.setText(QCoreApplication.translate("MainWindow", u"PTS #2", None))
        self.label_3P2.setText(QCoreApplication.translate("MainWindow", u"3P #2", None))
        self.label_3PA2.setText(QCoreApplication.translate("MainWindow", u"3PA #2", None))
        self.label_3PP2.setText(QCoreApplication.translate("MainWindow", u"3P% #2", None))
        self.label_2P2.setText(QCoreApplication.translate("MainWindow", u"2P #2", None))
        self.label_2PA2.setText(QCoreApplication.translate("MainWindow", u"2PA #2", None))
        self.label_2PP2.setText(QCoreApplication.translate("MainWindow", u"2P% #2", None))
        self.label_FT2.setText(QCoreApplication.translate("MainWindow", u"FT #2", None))
        self.label_FTA2.setText(QCoreApplication.translate("MainWindow", u"FTA #2", None))
        self.label_FTP2.setText(QCoreApplication.translate("MainWindow", u"FT% #2", None))
        self.label_DRB2.setText(QCoreApplication.translate("MainWindow", u"DRB #2", None))
        self.label_ORB2.setText(QCoreApplication.translate("MainWindow", u"ORB #2", None))
        self.label_TRB2.setText(QCoreApplication.translate("MainWindow", u"TRB #2", None))
        self.label_AST2.setText(QCoreApplication.translate("MainWindow", u"AST #2", None))
        self.label_STL2.setText(QCoreApplication.translate("MainWindow", u"STL #2", None))
        self.label_BLK2.setText(QCoreApplication.translate("MainWindow", u"BLK #2", None))
        self.label_TOV2.setText(QCoreApplication.translate("MainWindow", u"TOV #2", None))
        self.label_F2.setText(QCoreApplication.translate("MainWindow", u"F #2", None))
        self.label_totalscore.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.CorrelationTab.setTabText(self.CorrelationTab.indexOf(self.Model), QCoreApplication.translate("MainWindow", u"Model", None))
        self.CorrelationTab.setTabText(self.CorrelationTab.indexOf(self.Correlations), QCoreApplication.translate("MainWindow", u"Correlations", None))
    # retranslateUi

