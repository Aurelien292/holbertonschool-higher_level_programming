#!/usr/bin/python3
"""
    Représente un rectangle avec une largeur et une hauteur spécifiées.
"""

class Rectangle:
    """
    Représente un rectangle avec une largeur et une hauteur spécifiées.

    Attributs:
        width (int): La largeur du rectangle.
        height (int): La hauteur du rectangle.

    Méthodes:
        __init__(self, width=0, height=0): Initialise un rectangle.
        width (getter, setter): Accède et définit la largeur du rectangle.
        height (getter, setter): Accède et définit la hauteur du rectangle.
        area(self): Retourne l'aire du rectangle.
        perimeter(self): Retourne le périmètre du rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec une largeur et une hauteur spécifiées."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retourne la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retourne la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

