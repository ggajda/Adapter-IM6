from sql.sql_actions import query_read_person


class Dialog:
    def __init__(self, window):
        self.window = window

        self.window.pushButtonTest.clicked.connect(self.handel_btn)
        self.window.tableWidget.setHorizontalHeaderLabels(
            ["ID", "First Name", "Last Name"]
        )

    def handel_btn(self):
        query_read_person(self.window)
