from PySide6.QtWidgets import QTableWidgetItem
from sql.sql_actions import query_read_person


class Dialog:
    def __init__(self, window):
        self.window = window

        # button
        self.window.pushButtonTest.clicked.connect(self.handler_button)

        # tabelWidget
        self.columns_name = ["ID", "First Name", "Last Name"]
        self.window.tableWidget.horizontalHeader().resizeSection(0, 50)
        self.window.tableWidget.setColumnCount(len(self.columns_name))
        self.window.tableWidget.setHorizontalHeaderLabels(self.columns_name)
        self.window.tableWidget.itemDoubleClicked.connect(
            lambda: self.handler_tableWidget_doubleClicked(
                self.window.tableWidget.currentRow()
            )
        )

    def handler_button(self):
        query_read_person(self.window)

    def handler_tableWidget_doubleClicked(self, row):
        data = self.window.tableWidget.item(row, 0)
        print(data.data(0))
