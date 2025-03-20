# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:37:27 2025

@author: zdima
"""

from PySide6 import QtWidgets, QtSql
class Data:
    def __init__(self):
        #super(Data, self).__init__()
        self.sozd_db()
    def sozd_db(self):
        database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName('history_db.db')
        if not database.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS history (Город VARCHAR(20) primary key, Страна VARCHAR(20), Широта VARCHAR(20), Долгота VARCHAR(20))")
        return True
    def ex_quer(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(str(query_value))
        query.exec()
        return query
    def add_city(self, city, country, lat, lon):
        sql_query = "INSERT INTO history (Город, Страна, Широта, Долгота) VALUES (?, ?, ?, ?)"
        self.ex_quer(sql_query, [city, country, lat, lon])
        
    def del_city(self, city):
        sql_query = "DELETE FROM history WHERE Город = ?"
        self.ex_quer(sql_query, [city])
        
        
        