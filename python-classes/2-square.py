#!/usr/bin/python3
"""
Module qui définit une classe Square représentant un carré.

La classe permet de créer un carré avec une taille donnée et d'effectuer
des validations sur la taille.

Classe:
    Square: Classe représentant un carré avec un côté de taille donnée.

Attributs:
    size (int): La taille du côté du carré. Par défaut, elle est égale à 0.

Fonctions:
    __init__(size=0): Initialise un carré avec une taille donnée
    (doit être un entier >= 0).
"""


class Square:
    """
    Classe représentant un carré avec une taille de côté donnée.

    Attributs:
        __size (int): Taille du côté du carré. Par défaut, 0.

    Méthodes:
        __init__(size=0): Constructeur qui initialise la taille du
        carré et effectue les validations.
    """

    def __init__(self, size=0):
        """
        Initialise un carré avec une taille donnée.

        Paramètres:
            size (int): La taille du côté du carré. Par défaut, 0.

        Lève:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
