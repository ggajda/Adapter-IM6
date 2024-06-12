import pyodbc


class DB:
    def __init__(self, query):
        self.server = "(local)"
        self.database = "IMAGEnet"
        self.username = "sa"
        self.password = "Topcon1932"
        self.connection = ""
        self.query = query

    def db_connect(self):
        self.connection = pyodbc.connect(
            f"DRIVER={'ODBC Driver 17 for SQL Server'};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
        )

        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query)
        return self.cursor

    def db_disconnect(self):
        self.connection.close()
