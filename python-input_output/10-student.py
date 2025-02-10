#!/usr/bin/python3
"""
    Classe qui définit un étudiant avec son prénom, son nom et son âge.
    """


class Student:
    """
    Classe qui définit un étudiant avec son prénom, son nom et son âge.

    Attributs publics:
        first_name (str): Le prénom de l'élève.
        last_name (str): Le nom de famille de l'élève.
        age (int): L'âge de l'élève.

    Méthodes publiques:
        to_json(attrs=None): Retourne un dictionnaire représentant
        l'objet Student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialisation d'un étudiant avec son prénom, son nom et son âge.

        Args:
            first_name (str): Le prénom de l'élève.
            last_name (str): Le nom de famille de l'élève.
            age (int): L'âge de l'élève.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire contenant les attributs de l'objet Student.

        Si `attrs` est fourni, seuls les attributs mentionnés dans la liste
        `attrs` seront récupérés. Si `attrs` est `None`, tous les attributs
        de l'objet sont retournés.

        Args:
            attrs (list, optional): Liste des noms d'attributs à récupérer.
                                     Par défaut, None.

        Returns:
            dict: Un dictionnaire représentant l'objet Student
            avec les attributs
                  spécifiés dans `attrs`, ou tous les attributs
                  si `attrs` est None.
        """
        json_dict = {}

        # Si attrs est fourni, ne récupérer que les attributs demandés
        if attrs:
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
        else:
            # Sinon, récupérer tous les attributs d'instance
            json_dict = vars(self)
            # Utilisation de vars() pour accéder aux attributs d'instance

        return json_dict
