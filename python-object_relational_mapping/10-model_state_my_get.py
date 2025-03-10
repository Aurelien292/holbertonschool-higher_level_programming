#!/usr/bin/python3
"""
    Script that prints the State object with the name passed as argument
    from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Récupération des arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db_name),
        pool_pre_ping=True
    )

    # Création d'une session pour interagir avec la base de données
    session = Session(engine)

    # Recherche de l'état dans la base de données par son nom
    state = session.query(State).filter(State.name == state_name).first()

    # Affichage de l'id de l'état trouvé, ou message "Not found" si aucun
    # état n'est trouvé
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Fermeture de la session
    session.close()
