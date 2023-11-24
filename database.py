import mysql.connector

# Conextion a la base  de donnée
def open_db():
    return mysql.connector.connect(host="127.0.0.1", port="3306" ,user="root", password="", database="proj_DBPY"
                                   ,buffered=True, autocommit=True)
db_connection = open_db()
print("Connection réussi")

def save_game_geo01(pseudo, date_hour, duration, exercice, nbtrials, nbok, percent):
    query = "INSERT INTO results (pseudo, date_hour, duration, exercice, nbtrials, nbok, percent) values (%s, %s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (pseudo, date_hour, duration, exercice, nbtrials, nbok, percent))
    row = cursor.lastrowid
    cursor.close()
    return row
