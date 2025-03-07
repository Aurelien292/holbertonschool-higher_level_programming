#!/usr/bin/python3
"""
Script qui répertorie tous les villes avec sécurité injection SQL .
"""
import MySQLdb
import sys


def connectBDD(user, password, BDD_name):
    """
    Établit une connexion à la base de données MySQL.

    Cette fonction permet de se connecter à une base de données MySQL
    en utilisant les informations d'identification fournies (utilisateur,
    mot de passe et nom de la base de données).

    Args:
        user (str): Le nom d'utilisateur pour se connecter
        à la base de données.
        password (str): Le mot de passe associé à l'utilisateur.
        BDD_name (str): Le nom de la base de données à laquelle se connecter.
        state_name (str): Le nom de l'état à rechercher.

    Returns:
        MySQLdb.connect: Un objet de connexion à la base de données MySQL.
    """
    connect = MySQLdb.connect(
        host="localhost",
        user=user,
        password=password,
        db=BDD_name,
        port=3306,
        charset="utf8"
    )
    return connect

# Récupère les arguments passés en ligne de commande


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    BDD_name = sys.argv[3]
    state_name = sys.argv[4]

connect = connectBDD(user, password, BDD_name)
# Crée un curseur pour exécuter la requête SQL
cursor = connect.cursor()

 # Requête SQL sécurisée avec paramètre pour éviter les injections SQL
query = ("SELECT * FROM states WHERE name = %s\
    ORDER BY states.id ASC")
# Exécute la requête SQL en utilisant un paramètre sécurisé
cursor.execute(query, (state_name,))
# Récupère et affiche toutes les lignes de la requête
ligne_requete = cursor.fetchall()
for ligne in ligne_requete:
    print(ligne)
# Ferme le curseur et la connexion à la base de données
cursor.close()
connect.close()
