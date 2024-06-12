from sql.sql_conection import DB
from sql.sql_queries import select_patients


def query_read_person(window):

    db = DB(query=select_patients)
    cursor = db.db_connect()

    rows = cursor.fetchall()
    for row in rows:
        print(row.SurName)

    db.db_disconnect()
