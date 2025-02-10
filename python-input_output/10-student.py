#!/usr/bin/python3
"""Module contenant la classe Student"""


class Student:
    """La classe Student représente un étudiant avec des informations
    personnelles.

    Attributs :
        first_name (str) : Le prénom de l'étudiant.
        last_name (str) : Le nom de famille de l'étudiant.
        age (int) : L'âge de l'étudiant.

    Méthodes :
        to_json(attrs=None) : Retourne une représentation sous forme
        de dictionnaire de l'objet Student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialise une instance de la classe Student avec le
        prénom, le nom et l'âge fournis.

        Args :
            first_name (str) : Le prénom de l'étudiant.
            last_name (str) : Le nom de famille de l'étudiant.
            age (int) : L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne une représentation sous forme de dictionnaire de
        l'objet Student.

        Si `attrs` est une liste de chaînes de caractères, seuls les
        attributs dont le nom est présent dans
        la liste `attrs` seront inclus dans le dictionnaire retourné.
        Si `attrs` n'est pas fourni, ou si ce n'est
        pas une liste de chaînes, tous les attributs de l'objet seront
        inclus dans le dictionnaire.

        Args :
            attrs (list, optionnel) : Une liste de noms d'attributs
            (chaînes de caractères) à inclure dans le
                                      dictionnaire retourné. Si `None`,
                                      tous les attributs de l'objet Student
                                      seront retournés.

        Retourne :
            dict : Un dictionnaire représentant l'objet Student, contenant
            uniquement les attributs spécifiés
                   dans `attrs`, ou tous les attributs si `attrs` est `None`.

        Exemple :
            student = Student("John", "Doe", 25)
            student.to_json() => {'first_name': 'John', 'last_name': 'Doe',
            'age': 25}
            student.to_json(["first_name", "age"]) => {'first_name': 'John',
            'age': 25}
        """
        if isinstance(attrs, list) and all(isinstance(element, str) for
                                           element in attrs):
            new_dict = dict()
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        return self.__dict__
