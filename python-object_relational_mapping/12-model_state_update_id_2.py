#!/usr/bin/python3
"""
    Script that changes the name of a State object in the database.
    This script will change the name of the state with id=2 to 'New Mexico'.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) < 4:
        print("Usage: ./change_state.py <mysql_user> <mysql_password> <database_name>")
        sys.exit(1)

    # Récupération des arguments depuis la ligne de commande
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Création de la chaîne de connexion à la base de données
    engine = create_engine(
        f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{database_name}',  # Chaîne de connexion dynamique
        pool_pre_ping=True  # Vérifie la validité de la connexion avant chaque requête
    )

    # Crée les tables si elles n'existent pas
    Base.metadata.create_all(engine)

    # Création de la session pour interagir avec la base de données
    session = Session(engine)

    # Recherche de l'état avec l'ID 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Si l'état existe, on modifie son nom
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()  # Applique la modification dans la base de données
        print("State with id 2 has been renamed to 'New Mexico'")
    else:
        print("State with id 2 not found.")

    # Fermeture de la session
    session.close()
