#!/usr/bin/python3
"""
Module qui définit une classe Square représentant un carré.
"""


class Square:
    """
    Classe représentant un carré avec une taille de côté et une
    position spécifiées.

    Attributs:
        size (int): Taille du côté du carré, doit être un entier >= 0.
        position (tuple): Position du carré, tuple de 2 entiers positifs
        représentant les coordonnées (x, y).

    Méthodes:
        __init__(size, position=(0, 0)): Initialise un carré avec
        une taille et une position optionnelles.
        size: Propriété pour obtenir la taille du carré.
        size.setter: Propriété pour définir la taille du carré avec validation.
        position: Propriété pour obtenir la position du carré.
        position.setter: Propriété pour définir la position du carré avec
        validation.
        my_print(): Affiche le carré en utilisant des symboles '#' en
        fonction de la taille et de la position.
        area(): Retourne l'aire du carré.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un carré avec une taille et une position données.

        Paramètres:
            size (int): Taille du côté du carré.
            position (tuple): Position du carré sous forme de tuple (x, y),
            valeurs par défaut (0, 0).

        Lève:
            TypeError: Si size n'est pas un entier, ou si position
            n'est pas un tuple de 2 entiers positifs.
            ValueError: Si size est inférieur à 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retourne la taille du côté du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du côté du carré après validation.

        Lève:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retourne la position du carré.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Définit la position du carré après validation.

        Lève:
            TypeError: Si position n'est pas un tuple de 2 entiers positifs.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Affiche le carré formé de '#' en fonction de la taille et de
        la position.

        Si la position est spécifiée, elle décalera l'affichage du
        carré en fonction des valeurs x et y.
        Si la taille est 0, une ligne vide sera imprimée.
        """
        if self.size == 0:
            print()
            return

        # Imprimer les lignes vides selon le décalage vertical
        for _ in range(self.position[1]):
            print()

        # Générer et imprimer chaque ligne du carré
        row = ' ' * self.position[0] + '#' * self.size
        for _ in range(self.size):
            print(row)

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Retourne:
            int: L'aire du carré (self.__size * self.__size).
        """
        return self.__size * self.__size
