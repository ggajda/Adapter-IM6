from PySide6.QtWidgets import QTableWidgetItem
from sql.sql_conection import DB
from sql.sql_queries import select_patients


def query_read_person(window):

    db = DB(query=select_patients)
    cursor = db.db_connect()

    rows = cursor.fetchall()
    window.tableWidget.setRowCount(len(rows) + 1)
    tablerow = 0
    for row in rows:
        window.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
        window.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
        window.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
        tablerow += 1
        print(row[0])

    db.db_disconnect()
