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
        to_json(): Retourne un dictionnaire représentant l'objet Student.
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

    def to_json(self):
        """
        Retourne un dictionnaire contenant les attributs sérialisables
        de l'objet Student.

        Cette méthode fonctionne de manière similaire à la fonction
        `class_to_json`.
        Elle récupère les attributs de l'objet `Student` qui peuvent être
        sérialisés en JSON (str, int, bool, list, dict).

        Returns:
            dict: Un dictionnaire représentant l'objet Student, prêt à
            être sérialisé en JSON.
        """
        json_dict = {}

        # Liste des types sérialisables en JSON
        serializable_types = (str, int, bool, list, dict)

        # Parcourir tous les attributs de l'objet et ajouter ceux qui sont
        # sérialisables
        for attr in dir(self):
            if not attr.startswith('__'):  # Exclure les attributs spéciaux
                value = getattr(self, attr)
                if isinstance(value, serializable_types):
                    json_dict[attr] = value

        return json_dict
