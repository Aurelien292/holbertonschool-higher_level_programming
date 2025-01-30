#!/usr/bin/python3
"""
    Représente un rectangle avec une largeur et une hauteur spécifiées.
"""


class Rectangle:

    """
    Représente un rectangle avec une largeur et une hauteur spécifiées.

    Cette classe permet de créer un rectangle avec une largeur et une hauteur,
    de calculer l'aire et le périmètre, et de manipuler diverses
    propriétés du rectangle.

    Attributs de classe:
        number_of_instances (int): Le nombre d'instances créées
        de la classe Rectangle.
        print_symbol (str): Le symbole utilisé pour afficher le
        rectangle. Par défaut, c'est '#'.

    Attributs d'instance:
        width (int): La largeur du rectangle. Doit être un entier >= 0.
        height (int): La hauteur du rectangle. Doit être un entier >= 0.

    Méthodes:
        __init__(self, width=0, height=0):
            Initialise un rectangle avec la largeur et la hauteur spécifiées.

        width (getter, setter):
            Accède à la largeur du rectangle. Définit la largeur en vérifiant
            qu'elle est un entier et >= 0.

        height (getter, setter):
            Accède à la hauteur du rectangle. Définit la hauteur en vérifiant
            qu'elle est un entier et >= 0.

        area(self):
            Calcule et retourne l'aire du rectangle (largeur * hauteur).

        perimeter(self):
            Calcule et retourne le périmètre du rectangle
            (2 * (largeur + hauteur)).
            Si la largeur ou la hauteur est égale à 0, retourne 0.

        __str__(self):
            Retourne une chaîne représentant visuellement le rectangle avec
            le symbole `print_symbol`. Si la largeur ou la hauteur est
            égale à 0, retourne une chaîne vide.

        __repr__(self):
            Retourne une chaîne permettant de recréer l'objet à l'aide
            de `eval()`.
            Représentation sous la forme "Rectangle(width, height)".

        __del__(self):
            Cette méthode est appelée lorsqu'une instance de Rectangle
            est supprimée.
            Décrémente le compteur d'instances et affiche un message
            de suppression.

        bigger_or_equal(rect_1, rect_2):
            Méthode statique qui compare deux rectangles et retourne
            celui ayant la plus grande aire.
            Si les deux rectangles ont la même aire, retourne rect_1.

        square(cls, size=0):
            Méthode de classe qui retourne un nouveau Rectangle avec
            une largeur et une hauteur égales à `size`.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return (str(self.print_symbol) * self.width + '\n') * self.height

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
