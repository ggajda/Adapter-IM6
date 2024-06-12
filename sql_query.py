from sql_conection import connection, cursor

query = "SELECT PatientIdentifier, ForeName, SurName from Patients pa, Persons pe WHERE pa.PersonUid = pe.PersonUid"


def query_action():
    result = cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()
