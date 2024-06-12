from sql_query import query_action


class Btn:
    def __init__(self, window):
        self.window = window

        self.window.pushButtonTest.clicked.connect(self.handel_btn)

    def handel_btn(self):
        query_action()
