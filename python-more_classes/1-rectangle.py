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
        __repr__(self): Retourne une représentation textuelle du rectangle.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        return f"Rectangle(width={self.__width}, height={self.__height})"
