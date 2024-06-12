import pyodbc

server = "(local)"
database = "IMAGEnet"
username = "sa"
password = "Topcon1932"

connection = pyodbc.connect(
    f"DRIVER={'ODBC Driver 17 for SQL Server'};SERVER={server};DATABASE={database};UID={username};PWD={password}"
)

cursor = connection.cursor()

# connection.close()
