#!/usr/bin/python3
"""
Script to list all cities of a state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def connectBDD(user, password, db_name):
    """
    Function to connect to the MySQL database
    """
    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    return connect


if __name__ == "__main__":
    # Récupérer les arguments de la ligne de commande
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données MySQL
    db = connectBDD(mysql_user, mysql_password, mysql_db)

    # Créer un curseur pour exécuter la requête SQL
    cursor = db.cursor()

    # Requête SQL avec un paramètre sécurisé pour éviter l'injection SQL
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Exécution de la requête
    cursor.execute(query, (state_name,))

    # Récupérer toutes les lignes du résultat
    cities = cursor.fetchall()

    # Créer une liste des noms des villes
    city_names = [city[0] for city in cities]

    # Afficher les villes séparées par des virgules
    print(", ".join(city_names))

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    db.close()
