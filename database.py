'''
Auteur : Nussbaum Théo
Date : 15.12.2023
Version : 0.2
'''

import mysql.connector

# Connexion à la base de données
def open_db():
    return mysql.connector.connect(host="127.0.0.1", port="3306", user="root", password="", database="proj_DBPY", buffered=True, autocommit=True)

db_connection = open_db()  # Établissement de la connexion
print("Connexion réussie")

# Fonction pour sauvegarder une partie
def saved_game(pseudo, date_hour, duration, exercice, nbtrials, nbok, percent):
    query = "INSERT INTO results (pseudo, date_hour, duration, exercice, nbtrials, nbok, percent) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (pseudo, date_hour, duration, exercice, nbtrials, nbok, percent))
    row = cursor.lastrowid  # Récupération de l'ID de la dernière ligne insérée
    cursor.close()
    return row

# Fonction pour afficher la table des résultats
def display_table_result():
    query = "SELECT idResults, pseudo, date_hour, duration, exercice, nbtrials, nbok, percent FROM results"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()  # Récupération de toutes les lignes de résultats
    cursor.close()
    return rows

def sql_filter(sql_add):
    sql_base="SELECT * from results"
    query = sql_base + sql_dynamic2(sql_add, )
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()  # Récupération de toutes les lignes de résultats
    cursor.close()
    return rows

# Fonction pour afficher la table des moyennes
def display_table_average():
    query = "SELECT COUNT(pseudo), SEC_TO_TIME(SUM(TIME_TO_SEC(duration))), SUM(nbtrials), SUM(nbok), AVG(percent) FROM results"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()  # Récupération de toutes les lignes de résultats
    cursor.close()
    return rows

# Fonction pour supprimer une entrée en fonction de son ID
def delete_from_id(id):
    query = "DELETE FROM results WHERE idResults = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    cursor.close()

# Fonction pour éditer les résultats en fonction de l'ID
def edit_result(duration, nbok, nbtrials, percent, id):
    query = "UPDATE results SET duration = %s, nbok = %s, nbtrials = %s, percent = %s WHERE idResults = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (duration, nbok, nbtrials, percent, id))
    cursor.close()

# Fonction pour insérer des données à partir d'un ID
def insert_from_id(pseudo, date_hour, duration, exercice, nbtrials, nbok, percent):
    query = "INSERT INTO results (pseudo, date_hour, duration, exercice, nbtrials, nbok, percent) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (pseudo, date_hour, duration, exercice, nbtrials, nbok, percent))
    cursor.close()