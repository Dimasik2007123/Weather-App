# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu_prog1vIyVcV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableView,
    QVBoxLayout, QWidget, QGraphicsDropShadowEffect, QCheckBox, QAbstractItemView)

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setMinimumSize(QSize(900, 650))
        MainWindow.setMaximumSize(QSize(1400, 1000))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"font-family: Comic Sans MS")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-image: url(images/fon.jpeg);\n"
"background-position: left, top;\n"
"font-family: Comic Sans MS")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.verticalLayout = QVBoxLayout(self.Page1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.Page1)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 200))
        self.frame.setStyleSheet(u"background: transparent;")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 25, 0, 115)
        self.button_locate = QPushButton(self.frame)
        self.button_locate.setObjectName(u"button_locate")
        self.button_locate.setMinimumSize(QSize(300, 0))
        self.button_locate.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        self.button_locate.setFont(font)
        self.button_locate.setStyleSheet(u"QPushButton{\n"
"	background: #3eb9ed;\n"
"	background-image: none;\n"
"   border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	color:black;\n"
"}\n"
"QPushButton:hover{\n"
"	background: #2ca1d4;\n"
"	background-image: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: #157eab;\n"
"	background-image: none;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/my_location_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_locate.setIcon(icon)

        self.verticalLayout_2.addWidget(self.button_locate)

        self.line_city = QLineEdit(self.frame)
        self.line_city.setObjectName(u"line_city")
        self.line_city.setMinimumSize(QSize(300, 0))
        self.line_city.setMaximumSize(QSize(300, 16777215))
        self.line_city.setStyleSheet(u"border-radius: 8px;\n"
"border: 2px solid black;\n"
"color: black;\n"
"")
        self.line_city.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.line_city)

        self.button_search = QPushButton(self.frame)
        self.button_search.setObjectName(u"button_search")
        self.button_search.setMinimumSize(QSize(300, 0))
        self.button_search.setMaximumSize(QSize(300, 16777215))
        self.button_search.setFont(font)
        self.button_search.setStyleSheet(u"QPushButton{\n"
"	background: #3eb9ed;\n"
"	background-image: none;\n"
"	font-weight: bold;\n"
"   border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background: #2ca1d4;\n"
"	background-image: none;\n"
"	font-weight: bold;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: #157eab;\n"
"	background-image: none;\n"
"	font-weight: bold;\n"
"	border-radius: 5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/search_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_search.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.button_search)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.label = QLabel(self.Page1)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background: #9badb0;\n"
"border: 2px solid black;\n"
"margin-bottom: 120%;\n"
"color: black;\n"
"border-radius: 50px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.Page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.Page2.setStyleSheet(u"background: transparent;")
        self.verticalLayout_5 = QVBoxLayout(self.Page2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame1 = QFrame(self.Page2)
        self.frame1.setObjectName(u"frame1")
        self.verticalLayout_4 = QVBoxLayout(self.frame1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.table_favor = QTableView(self.frame1)
        self.table_favor.setObjectName(u"table_favor")
        self.table_favor.setMinimumSize(QSize(864, 0))
        self.table_favor.setStyleSheet(u"QTableView{\n"
"	border: 2px solid black;\n"
"	border-bottom-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"   color: black;"
"}\n"
"QHeaderView::section{\n"
"	background: #79b89e;\n"
"   border: 2px solid black;\n"
"   border-bottom: 4px solid black;"
"   color: black;"
"}\n"
"QTableView::item{\n"
"   border: 1px solid black;\n"
"	background: #79b89e;\n"
"   color: black;"
"}\n"
"QTableView::item:selected{\n"
"   border: 1px solid black;\n"
"	background: #79b89e;\n"
"   color: black;"
"}\n"
"")
        self.table_favor.verticalHeader().setVisible(False)
        self.table_favor.verticalHeader().setDefaultSectionSize(70)
        self.table_favor.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table_favor.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        
        self.table_favor.horizontalHeader().setMinimumSectionSize(210)
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(14)
        self.table_favor.setFont(font)
        self.table_favor.horizontalHeader().setFont(font)
        self.table_favor.horizontalHeader().setHighlightSections(False)
        self.table_favor.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table_favor.horizontalHeader().setStretchLastSection(True)
        self.table_favor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.verticalLayout_4.addWidget(self.table_favor, 0, Qt.AlignHCenter)


        self.button_fs = QPushButton(self.frame1)
        self.button_fs.setObjectName(u"button_fs")
        self.button_fs.setStyleSheet(u"QPushButton{\n"
"	background: #3eb9ed;\n"
"	background-image: none;\n"
"	font-weight: bold;\n"
"	border-radius: 5px;\n"
"	border: 1px solid black;\n"
"	color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background: #2ca1d4;\n"
"	background-image: none;\n"
"	font-weight: bold;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: #157eab;\n"
"	background-image: none;\n"
"	font-weight: bold;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_4.addWidget(self.button_fs, 0)


        self.verticalLayout_5.addWidget(self.frame1)

        self.stackedWidget.addWidget(self.Page2)
        self.Page3 = QWidget()
        self.Page3.setObjectName(u"Page3")
        self.Page3.setStyleSheet(u"background: grey;")
        self.gridLayout_3 = QGridLayout(self.Page3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox = QCheckBox(self.Page3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(100, 0))
        self.checkBox.setStyleSheet(u"margin-bottom: 200px;")
        

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1, Qt.AlignTop)

        self.stackedWidget.addWidget(self.Page3)
        self.Page4 = QWidget()
        self.Page4.setObjectName(u"Page4")
        self.Page4.setStyleSheet(u"background: transparent;")
        self.Page4.setMinimumSize(QSize(882, 596))
        self.verticalLayout_8 = QVBoxLayout(self.Page4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame2 = QFrame(self.Page4)
        self.frame2.setObjectName(u"frame2")
        self.verticalLayout_3 = QVBoxLayout(self.frame2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_city = QLabel(self.frame2)
        self.label_city.setObjectName(u"label_city")
        self.label_city.setStyleSheet(u"border: 2px solid black;\n"
"border-right: 2px dashed black;\n"
"font-size: 20pt;\n"
"border-bottom-left-radius: 7px;\n"
"border-top-left-radius: 7px;\n"
"color: black;")
        self.label_city.setAlignment(Qt.AlignCenter)
        self.label_city.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_city)

        self.label_country = QLabel(self.frame2)
        self.label_country.setObjectName(u"label_country")
        self.label_country.setStyleSheet(u"border: 2px solid black;\n"
"border-right: 2px dashed black;\n"
"border-left: none;\n"
"font-size: 20pt;\n"
"color: black;")
        self.label_country.setAlignment(Qt.AlignCenter)
        self.label_country.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_country)

        self.label_desc = QLabel(self.frame2)
        self.label_desc.setObjectName(u"label_desc")
        self.label_desc.setStyleSheet(u"border: 2px solid black;\n"
"border-right: 2px dashed black;\n"
"border-left: none;\n"
"font-size: 20pt;\n"
"color: black;")
        self.label_desc.setAlignment(Qt.AlignCenter)
        self.label_desc.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_desc)

        self.label_temp = QLabel(self.frame2)
        self.label_temp.setObjectName(u"label_temp")
        self.label_temp.setStyleSheet(u"border: 2px solid black;\n"
"border-right: 2px dashed black;\n"
"border-left: none;\n"
"font-size: 20pt;\n"
"color: black;")
        self.label_temp.setAlignment(Qt.AlignCenter)
        self.label_temp.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_temp)

        self.label_feel = QLabel(self.frame2)
        self.label_feel.setObjectName(u"label_feel")
        self.label_feel.setStyleSheet(u"border: 2px solid black;\n"
"border-left: none;\n"
"font-size: 20pt;\n"
"border-bottom-right-radius: 7px;\n"
"border-top-right-radius: 7px;\n"
"color: black;")
        self.label_feel.setAlignment(Qt.AlignCenter)
        self.label_feel.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_feel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addWidget(self.frame2, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.Page4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"border: 2px solid black;\n"
"font-size: 12pt;\n"
"border-radius: 10px;"
"color: black;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_7)

        self.table_forecast_weather = QTableView(self.Page4)
        self.table_forecast_weather.setObjectName(u"table_forecast_weather")
        self.table_forecast_weather.setStyleSheet(u"QTableView{\n"
"	border: 2px solid black;\n"
"	border-bottom-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"   font-size: 20pt;"
"}\n"
"QTableView::item{\n"
"	background: #79b89e;\n"
"	border: 1px solid black;\n"
"	font-size: 30pt;\n"
"	color: black;\n"
"}"
"QTableView::item:selected{\n"
"	background: #79b89e;\n"
"	border: 1px solid black;\n"
"	font-size: 30pt;\n"
"	color: black;\n"
"}")
        self.table_forecast_weather.horizontalHeader().setVisible(False)
        self.table_forecast_weather.horizontalHeader().setDefaultSectionSize(250)
        #self.table_forecast_weather.horizontalHeader().setHighlightSections(False)
        self.table_forecast_weather.horizontalHeader().setStretchLastSection(True)
        self.table_forecast_weather.verticalHeader().setVisible(False)
        self.table_forecast_weather.verticalHeader().setDefaultSectionSize(95)
        #self.table_forecast_weather.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.table_forecast_weather.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_6.addWidget(self.table_forecast_weather)


        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_2)

        self.stackedWidget.addWidget(self.Page4)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.frame3 = QFrame(self.centralwidget)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setStyleSheet(u"background-image: none;\n"
"background: rgba(0, 0, 0, 80);")
        self.horizontalLayout = QHBoxLayout(self.frame3)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_home = QPushButton(self.frame3)
        self.button_home.setObjectName(u"button_home")
        font2 = QFont()
        font2.setFamily(u"Comic Sans MS")
        font2.setPointSize(22)
        self.button_home.setFont(font2)
        self.button_home.setStyleSheet(u"QPushButton{\n"
"	background: rgba(0, 0, 0, 80);\n"
"}\n"
"QPushButton:pressed{\n"
"	background:rgba(0,0,0,100);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/home_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_home.setIcon(icon2)
        self.button_home.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.button_home)

        self.button_favorites = QPushButton(self.frame3)
        self.button_favorites.setObjectName(u"button_favorites")
        self.button_favorites.setFont(font2)
        self.button_favorites.setStyleSheet(u"QPushButton{\n"
"	background: rgba(0,0,0,80);\n"
"}\n"
"QPushButton:pressed{\n"
"	background: rgba(0,0,0,100);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/history_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_favorites.setIcon(icon3)
        self.button_favorites.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.button_favorites)

        self.button_settings = QPushButton(self.frame3)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setFont(font2)
        self.button_settings.setStyleSheet(u"QPushButton{\n"
"	background: rgba(0, 0, 0, 80);\n"
"}\n"
"QPushButton:pressed{\n"
"	background: rgba(0,0,0,100);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_settings.setIcon(icon4)
        self.button_settings.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.button_settings)


        self.gridLayout.addWidget(self.frame3, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430 \u0441 \u0433\u0435\u043e\u043b\u043e\u043a\u0430\u0446\u0438\u0435\u0439", None))
        self.button_locate.setText(QCoreApplication.translate("MainWindow", u"\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.line_city.setText("")
        self.line_city.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430", None))
        self.button_search.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0438\u0441\u043a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \"\u041f\u043e\u0433\u043e\u0434\u0430 \u0441 \u0433\u0435\u043e\u043b\u043e\u043a\u0430\u0446\u0438\u0435\u0439\". \n"
"\u0427\u0442\u043e\u0431\u044b \u0443\u0432\u0438\u0434\u0435\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u043e\u0433\u043e\u0434\u0435 \u0432 \u0432\u0430\u0448\u0435\u043c \u0433\u043e\u0440\u043e\u0434\u0435,\n"
"\u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435\" \u0432 \u0432\u0435\u0440\u0445\u043d\u0435\u0439 \u0447\u0430\u0441\u0442\u0438 \u044d\u043a\u0440\u0430\u043d\u0430.\n"
"\u0415\u0441\u043b\u0438 \u0436\u0435 \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e"
                        "\u0433\u043e\u0434\u0443 \u0432 \u0434\u0440\u0443\u0433\u043e\u043c \u0433\u043e\u0440\u043e\u0434\u0435,\n"
"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0435\u0433\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u0440\u0443\u0447\u043d\u0443\u044e \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \"\u041f\u043e\u0438\u0441\u043a\". ", None))
        self.button_fs.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e\u0433\u043e\u0434\u0443", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0451\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.label_city.setText("")
        self.label_country.setText("")
        self.label_desc.setText("")
        self.label_temp.setText("")
        self.label_feel.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437 \u043f\u043e\u0433\u043e\u0434\u044b \u043d\u0430 3 \u0434\u043d\u044f", None))
        self.button_home.setText("")
        self.button_favorites.setText("")
        self.button_settings.setText("")
    # retranslateUi

