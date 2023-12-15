import mysql.connector

# Conextion a la base  de donnée
def open_db():
    return mysql.connector.connect(host="127.0.0.1", port="3306" ,user="root", password="", database="proj_DBPY"
                                   ,buffered=True, autocommit=True)
db_connection = open_db()
print("Connection réussi")

def saved_game(pseudo, date_hour, duration, exercice, nbtrials, nbok, percent):
    query = "INSERT INTO results (pseudo, date_hour, duration, exercice, nbtrials, nbok, percent) values (%s, %s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (pseudo, date_hour, duration, exercice, nbtrials, nbok, percent))
    row = cursor.lastrowid
    cursor.close()
    return row

def display_table_result():
    query = "SELECT idResults, pseudo, date_hour, duration, exercice, nbtrials, nbok, percent FROM results"
    cursor = db_connection.cursor()
    cursor.execute(query, )
    row = cursor.fetchall()
    cursor.close()
    return row

def display_table_average():
    query = "SELECT count(pseudo), SEC_TO_TIME(TIME_TO_SEC(SUM(duration))), SUM(nbtrials), SUM(nbok), AVG(percent) FROM results"
    cursor = db_connection.cursor()
    cursor.execute(query, )
    row = cursor.fetchall()
    cursor.close()
    return row

def delete_from_id(id):
    query = "DELETE FROM results WHERE idResults = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (id, ))
    cursor.close()

def edit_result(duration, nb_ok, nb_trial, id):
    query = "UPDATE display SET temps = %s, nb_ok = %s, nb_total = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (duration, nb_ok, nb_trial, id))
    cursor.close()
