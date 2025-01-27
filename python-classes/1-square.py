#!/usr/bin/python3
"""
Module qui définit une classe Square pour gérer un carré.

La classe Square permet de définir un carré, de calculer son aire
et de contrôler la taille de son côté.

Classe:
    Square: Représente un carré avec une taille de côté et calcule son aire.

"""


class Square:
    """
    Représente un carré avec une taille de côté donnée.

    Attributs:
        __size (int): Taille du côté du carré. Doit être un entier positif.

    Méthodes:
        __init__(size): Initialise le carré avec la taille spécifiée.
        area(): Calcule et retourne l'aire du carré (côté^2).
    """

    def __init__(self, size):
        """
        Initialise un carré avec la taille donnée.

        Args:
            size (int): Taille du côté du carré. Doit être un entier positif.

        Lève:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré (côté^2).
        """
        return self.__size ** 2
