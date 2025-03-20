# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:01:19 2025

@author: zdima
"""
import sys
import requests
from PySide6 import QtWidgets, QtCore, QtSql
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QGraphicsDropShadowEffect
from main_menu_prog1 import Ui_MainWindow 
from for_db import Data
from with_wait import Ui_Form
def coord(city):
    response = requests.get('https://api.geoapify.com/v1/geocode/search?&city='+city+'&format=json&apiKey=cbcf979d42da452b8ae8191884fa4aaa&lang=ru').json()
    if len(response.get("results")) == 0:
        return ['0', '0', '0']
    country = response.get("results")[0]['country']
    lat = response.get("results")[0]['lat']
    lon = response.get("results")[0]['lon']
    a = [country, lat, lon]
    return a
def get_ip():
    ip = requests.get('https://api.ipify.org').text
    return ip


def get_location():
    ip_address = get_ip()
    response = requests.get(f"http://ip-api.com/json/{ip_address}?lang=ru").json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "country": response.get("country"),
        "lat": response.get("lat"),
        "lon": response.get("lon")
        
    }
    return location_data
def forecast(lat, lon):
    url = 'https://api.openweathermap.org/data/2.5/forecast?lat='+str(lat)+'&lon='+str(lon)+'&units=metric&lang=ru&appid=ff9c29090611b9a0eaef169e87117ec2'
    fordata = requests.get(url).json()
    prognoz = [["Дата и время", "Температура", "Погода"], 
               [fordata['list'][9]['dt_txt'], str(round(fordata['list'][9]['main']['temp'])), fordata['list'][9]['weather'][0]['description']],
               [fordata['list'][17]['dt_txt'], str(round(fordata['list'][17]['main']['temp'])), fordata['list'][17]['weather'][0]['description']],
               [fordata['list'][25]['dt_txt'], str(round(fordata['list'][25]['main']['temp'])), fordata['list'][25]['weather'][0]['description']]]
    return prognoz
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignHCenter

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

class Initial(QMainWindow):
    def __init__(self):
        super(Initial, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bd = Data()
        self.viewhistory()
        shadow = QGraphicsDropShadowEffect(self)

        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0))
        shadow.setOffset(5, 5)
        self.ui.label.setGraphicsEffect(shadow)
        self.ui.button_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page1))
        self.ui.button_favorites.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page2))
        self.ui.button_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page3))
        self.ui.button_fs.clicked.connect(lambda: self.search_db())
        self.ui.button_fs.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page4))
        def dark_theme(state):
            if state == 2:  
                self.ui.centralwidget.setStyleSheet(u"background-image: url(images/fon_black1.jpg)")
                self.ui.button_locate.setStyleSheet(u"QPushButton{\n"
        "	background: #6069bd;\n"
        "	background-image: none;\n"
        "   border: 1px solid white;\n"
        "	border-radius: 5px;\n"
        "	color:white;\n"
        "}\n"
        "QPushButton:hover{\n"
        "	background: #5761ba;\n"
        "	background-image: none;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background: #4c57ba;\n"
        "	background-image: none;\n"
        "}\n"
        "")
                self.ui.line_city.setStyleSheet(u"border-radius: 8px;\n"
        "border: 2px solid white;\n"
        "color: white;\n"
        "")
                self.ui.button_search.setStyleSheet(u"QPushButton{\n"
        "	background: #6069bd;\n"
        "	background-image: none;\n"
        "	font-weight: bold;\n"
        "   border: 1px solid white;\n"
        "	border-radius: 5px;\n"
        "	color: white;\n"
        "}\n"
        "QPushButton:hover{\n"
        "	background: #5761ba;\n"
        "	background-image: none;\n"
        "	font-weight: bold;\n"
        "	border-radius: 5px;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background: #4c57ba;\n"
        "	background-image: none;\n"
        "	font-weight: bold;\n"
        "	border-radius: 5px;\n"
        "}")
                self.ui.label.setStyleSheet(u"background: #25244d;\n"
        "border: 2px solid white;\n"
        "margin-bottom: 120%;\n"
        "color: white;\n"
        "border-radius: 50px;")
                self.ui.button_fs.setStyleSheet(u"QPushButton{\n"
        "	background: #6069bd;\n"
        "	background-image: none;\n"
        "	font-weight: bold;\n"
        "   border: 1px solid white;\n"
        "	border-radius: 5px;\n"
        "	color: white;\n"
        "}\n"
        "QPushButton:hover{\n"
        "	background: #5761ba;\n"
        "	background-image: none;\n"
        "	font-weight: bold;\n"
        "	border-radius: 5px;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background: #4c57ba;\n"
        "	background-image: none;\n"
        "	font-weight: bold;\n"
        "	border-radius: 5px;\n"
        "}")
                self.ui.checkBox.setStyleSheet(u"margin-bottom: 200px; color: white;")
                self.ui.label_city.setStyleSheet(u"border: 2px solid white;\n"
        "border-right: 2px dashed white;\n"
        "font-size: 20pt;\n"
        "border-bottom-left-radius: 7px;\n"
        "border-top-left-radius: 7px;\n"
        "color: white;")
                self.ui.label_country.setStyleSheet(u"border: 2px solid white;\n"
        "border-right: 2px dashed white;\n"
        "border-left: none;\n"
        "font-size: 20pt;\n"
        "color: white;")
                self.ui.label_desc.setStyleSheet(u"border: 2px solid white;\n"
        "border-right: 2px dashed white;\n"
        "border-left: none;\n"
        "font-size: 20pt;\n"
        "color: white;")
                self.ui.label_temp.setStyleSheet(u"border: 2px solid white;\n"
        "border-right: 2px dashed white;\n"
        "border-left: none;\n"
        "font-size: 20pt;\n"
        "color: white;")
                self.ui.label_feel.setStyleSheet(u"border: 2px solid white;\n"
        "border-left: none;\n"
        "font-size: 20pt;\n"
        "border-bottom-right-radius: 7px;\n"
        "border-top-right-radius: 7px;\n"
        "color: white;")
                self.ui.label_7.setStyleSheet(u"border: 2px solid white;\n"
        "font-size: 12pt;\n"
        "border-radius: 10px;\n"
        "color: white;")
                self.ui.table_forecast_weather.setStyleSheet(u"QTableView{\n"
        "	border: 2px solid white;\n"
        "	border-bottom-right-radius: 7px;\n"
        "	border-bottom-left-radius: 7px;\n"
        "	border-top-right-radius: 7px;\n"
        "	border-top-left-radius: 7px;\n"
        "   font-size: 20pt;\n"
        "}\n"
        "QTableView::item{\n"
        "	background: #598774;\n"
        "   border: 1px solid white;\n"
        "	font-size: 30pt;\n"
        "	color: white;\n"
        "}"
        "QTableView::item:selected{\n"
        "	background: #598774;\n"
        "   border: 1px solid white;\n"
        "	font-size: 30pt;\n"
        "	color: white;\n"
        "}")
                self.ui.table_favor.setStyleSheet(u"QTableView{\n"
        "	border: 2px solid white;\n"
        "	border-bottom-right-radius: 7px;\n"
        "	border-bottom-left-radius: 7px;\n"
        "	border-top-right-radius: 7px;\n"
        "	border-top-left-radius: 7px;\n"
        "   color: white;"
        "}\n"
        "QHeaderView::section{\n"
        "	background: #598774;\n"
        "   border: 2px solid white;\n"
        "   border-bottom: 4px solid white;"
        "   color: white;"
        "}\n"
        "QTableView::item{\n"
        "   border: 1px solid white;\n"
        "	background: #598774;\n"
        "   color: white;"
        "}\n"
        "QTableView::item:selected{\n"
        "   border: 1px solid white;\n"
        "	background: #598774;\n"
        "   color: white;"
        "}\n"
        "")
            else:
                self.ui.centralwidget.setStyleSheet(u"background-image: url(images/fon.jpeg)")
                self.ui.button_locate.setStyleSheet(u"QPushButton{\n"
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
                self.ui.line_city.setStyleSheet(u"border-radius: 8px;\n"
        "border: 2px solid black;\n"
        "color: black;\n"
        "")
                self.ui.button_search.setStyleSheet(u"QPushButton{\n"
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
                self.ui.label.setStyleSheet(u"background: #9badb0;\n"
        "border: 2px solid black;\n"
        "margin-bottom: 120%;\n"
        "color: black;\n"
        "border-radius: 50px;")
                self.ui.button_fs.setStyleSheet(u"QPushButton{\n"
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
                self.ui.checkBox.setStyleSheet(u"margin-bottom: 200px; color: black;")
                self.ui.label_city.setStyleSheet(u"border: 2px solid black;\n"
        "border-right: 2px dashed black;\n"
        "font-size: 20pt;\n"
        "border-bottom-left-radius: 7px;\n"
        "border-top-left-radius: 7px;\n"
        "color: black;")
                self.ui.label_country.setStyleSheet(u"border: 2px solid black;\n"
        "border-right: 2px dashed black;\n"
        "border-left: none;\n"
        "font-size: 20pt;\n"
        "color: black;")
                self.ui.label_desc.setStyleSheet(u"border: 2px solid black;\n"
        "border-right: 2px dashed black;\n"
        "border-left: none;\n"
        "font-size: 20pt;\n"
        "color: black;")
                self.ui.label_temp.setStyleSheet(u"border: 2px solid black;\n"
        "border-right: 2px dashed black;\n"
        "border-left: none;\n"
        "font-size: 20pt;\n"
        "color: black;")
                self.ui.label_feel.setStyleSheet(u"border: 2px solid black;\n"
        "border-left: none;\n"
        "font-size: 20pt;\n"
        "border-bottom-right-radius: 7px;\n"
        "border-top-right-radius: 7px;\n"
        "color: black;")
                self.ui.label_7.setStyleSheet(u"border: 2px solid black;\n"
        "font-size: 12pt;\n"
        "border-radius: 10px;"
        "color: black;")
                self.ui.table_forecast_weather.setStyleSheet(u"QTableView{\n"
        "	border: 2px solid black;\n"
        "	border-bottom-right-radius: 7px;\n"
        "	border-bottom-left-radius: 7px;\n"
        "	border-top-right-radius: 7px;\n"
        "	border-top-left-radius: 7px;\n"
        "   font-size: 20pt;"
        "   text-align: center;"
        "}\n"
        "QTableView::item{\n"
        "	background: #79b89e;\n"
        "   border: 1px solid black;\n"
        "	font-size: 30pt;\n"
        "	color: black;\n"
        "}"
        "QTableView::item:selected{\n"
        "	background: #79b89e;\n"
        "   border: 1px solid black;\n"
        "	font-size: 30pt;\n"
        "	color: black;\n"
        "}")
                self.ui.table_favor.setStyleSheet(u"QTableView{\n"
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

        self.ui.checkBox.stateChanged.connect(dark_theme)
        
        
        self.ui.button_search.clicked.connect(lambda: self.add_city())
        self.ui.button_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page4))
        self.ui.button_locate.clicked.connect(lambda: self.add_city_loc())
        self.ui.button_locate.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page4))
    def viewhistory(self):
        self.model_h = QSqlTableModel(self)
        self.model_h.setTable('history')
        self.model_h.select()
        self.ui.table_favor.setModel(self.model_h)
        if self.ui.table_favor.verticalHeader().count() > 7:
            city = str(self.ui.table_favor.model().index(0, 0).data())
            self.bd.del_city(city)
            self.model_h = QSqlTableModel(self)
            self.model_h.setTable('history')
            self.model_h.select()
            self.ui.table_favor.setModel(self.model_h)
    def showdata(self, city, country, lat, lon):
        url = 'https://api.openweathermap.org/data/2.5/weather?lat='+str(lat)+'&lon='+str(lon)+'&units=metric&lang=ru&appid=ff9c29090611b9a0eaef169e87117ec2'
        weather_data = requests.get(url).json()
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        weat = weather_data['weather'][0]['description']
        self.ui.label_city.setText("Город\n" + city)
        self.ui.label_country.setText("Страна\n" + country)
        self.ui.label_desc.setText("Текущая погода\n" + weat)
        self.ui.label_temp.setText("Температура\n" + str(temperature))
        self.ui.label_feel.setText("Ощущается как\n" + str(temperature_feels))
        data = forecast(lat, lon)
        self.model = TableModel(data)
        self.ui.table_forecast_weather.setModel(self.model)
    def add_city(self):
        city = str(self.ui.line_city.text())
        if len(city) == 0:
            city = "notfound"
        spis = coord(city)
        country = str(spis[0])
        lat = str(spis[1])
        lon = str(spis[2])
        if country != '0':
            self.bd.add_city(city, country, lat, lon)
            self.showdata(city, country, lat, lon)
            self.viewhistory()
        else:
            self.ui.label_city.setText("Город не найден")
            self.ui.label_country.setText("-")
            self.ui.label_desc.setText("-")
            self.ui.label_temp.setText("-")
            self.ui.label_feel.setText("-")
            data = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            self.model = TableModel(data)
            self.ui.table_forecast_weather.setModel(self.model)
    def add_city_loc(self):
        self.new = QtWidgets.QWidget()
        self.neww = Ui_Form()
        self.neww.setupUi(self.new)
        self.new.show()

        city = get_location()['city'];
        country = get_location()['country']
        lat = get_location()['lat']
        lon = get_location()['lon']
        self.bd.add_city(str(city),str(country), str(lat), str(lon))
        self.showdata(city, country, lat, lon)
        self.viewhistory()
        self.new.close()
    def search_db(self):
        index = self.ui.table_favor.selectedIndexes()[0]
        stroca = index.row()
        city = str(self.ui.table_favor.model().index(stroca, 0).data())
        country = str(self.ui.table_favor.model().index(stroca, 1).data())
        lat = str(self.ui.table_favor.model().index(stroca, 2).data())
        lon = str(self.ui.table_favor.model().index(stroca, 3).data())
        self.showdata(city, country, lat, lon)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Initial()
    window.show()
    sys.exit(app.exec())