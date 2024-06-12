from sql.sql_actions import query_read_person


class Btn:
    def __init__(self, window):
        self.window = window

        self.window.pushButtonTest.clicked.connect(self.handel_btn)

    def handel_btn(self):
        query_read_person(self.window)
