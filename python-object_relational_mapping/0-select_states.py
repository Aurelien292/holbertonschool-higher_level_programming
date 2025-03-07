#!/usr/bin/python3
"""
Script qui répertorie tous les états de la base de données.
"""
import MySQLdb
import sys


def connectBDD(user, password, db):
    """
    Établit une connexion à la base de données MySQL.

    Cette fonction permet de se connecter à une base de données MySQL
    en utilisant les informations d'identification fournies (utilisateur,
    mot de passe et nom de la base de données).

    Args:
        user (str): Le nom d'utilisateur pour se connecter à la base
        de données.
        password (str): Le mot de passe associé à l'utilisateur.
        db (str): Le nom de la base de données à laquelle se connecter.

    Returns:
        MySQLdb.connect: Un objet de connexion à la base de données MySQL.
    """
    connect = MySQLdb.connect(
        host="localhost",
        user=user,
        password=password,
        db=db,
        port=3306,
        charset="utf8"
    )
    return connect

# Récupère les arguments passés en ligne de commande


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

connect = connectBDD(user, password, db)
# Crée un curseur pour exécuter la requête SQL
cursor = connect.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
# Récupère et affiche toutes les lignes de la requête
ligne_requete = cursor.fetchall()
for ligne in ligne_requete:
    print(ligne)
# Ferme le curseur et la connexion à la base de données
cursor.close()
connect.close()
