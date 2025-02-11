#!/usr/bin/python3
"""Classe Student qui définit un étudiant avec des méthodes de
sérialisation et désérialisation"""


class Student:
    """
    Classe représentant un étudiant.

    Attributs publics:
        first_name (str): Le prénom de l'étudiant.
        last_name (str): Le nom de famille de l'étudiant.
        age (int): L'âge de l'étudiant.

    Méthodes publiques:
        to_json(attrs=None): Retourne un dictionnaire représentant l'objet
        Student.
        reload_from_json(json): Met à jour les attributs de l'objet Student
        à partir d'un dictionnaire.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialisation d'un étudiant avec son prénom, son nom et son âge.

        Args:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de famille de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant l'objet Student.

        Si `attrs` est une liste, seuls les attributs indiqués dans
        `attrs` sont inclus.
        Si `attrs` est `None`, tous les attributs sont inclus.

        Args:
            attrs (list, optionnel): Liste des noms d'attributs à inclure
            dans la sortie.

        Returns:
            dict: Dictionnaire représentant l'objet Student.
        """
        # Vérifier si attrs est une liste sans utiliser isinstance
        if attrs is not None:
            # On vérifie simplement que c'est une liste
            if type(attrs) == list:  # On vérifie que attrs est bien une liste
                # Vérifier que tous les éléments de la liste sont
                # des chaînes de caractères
                for attr in attrs:
                    if type(attr) != str:
                        # On vérifie que chaque élément est une
                        # chaîne de caractères
                        return {}
                # Construire le dictionnaire avec les attributs spécifiés
                json_dict = {}
                for attr in attrs:
                    if attr in self.__dict__:
                        json_dict[attr] = self.__dict__[attr]
                return json_dict

        # Si attrs est None ou non valide, retourner tous les attributs
        return self.__dict__

    def reload_from_json(self, json):
        """
        Met à jour l'objet Student à partir d'un dictionnaire.

        Cette méthode remplace les valeurs des attributs de l'objet par
        celles du dictionnaire `json`.

        Args:
            json (dict): Dictionnaire contenant les nouvelles valeurs
            des attributs.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
