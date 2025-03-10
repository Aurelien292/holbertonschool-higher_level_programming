#!/usr/bin/python3
"""
    Script that adds the State object 'Louisiana' to the database
    hbtn_0e_6_usa. This version uses a function to handle the
    database connection and exception handling.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def create_session(user, password, db_name):
    """Création et gestion sécurisée de la session"""
    try:
        engine = create_engine(
            # Chaîne de connexion dynamique
            f'mysql+mysqldb://{user}:{password}@localhost/{db_name}',
            # Vérifie la validité de la connexion avant chaque requête
            pool_pre_ping=True
        )
        # Crée les tables si elles n'existent pas
        Base.metadata.create_all(engine)
        # Retourne une session pour effectuer des requêtes
        return Session(engine)
    except Exception as e:
        print(f"Error: {e}")
        return None


def add_state(session):
    """Ajoute l'état 'Louisiana' à la base de données"""
    try:
        new_state = State(name="Louisiana")  # Crée un nouvel objet State
        session.add(new_state)  # Ajoute l'objet à la session
        session.commit()  # Enregistre dans la base de données
        print(f"{new_state.id}")  # Affiche l'id du nouvel état
    except Exception as e:
        print(f"Error while adding the state: {e}")


if __name__ == "__main__":
    # Vérifie que tous les arguments sont passés
    if len(sys.argv) < 4:
        print("Usage: ./6-add_state.py <mysql_user>\
              <mysql_password> <database_name>")
        sys.exit(1)

    # Récupération des arguments depuis la ligne de commande
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Création de la session de connexion à la base de données
    session = create_session(mysql_user, mysql_password, database_name)

    # Si la session est valide, on ajoute l'état
    if session:
        add_state(session)
        session.close()  # Fermeture de la session après utilisation
