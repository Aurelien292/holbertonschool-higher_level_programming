#!/usr/bin/python3
"""
    Représente un rectangle avec une largeur et une hauteur spécifiées.
"""


class Rectangle:
    """
    Représente un rectangle avec une largeur et une hauteur spécifiées.

    La classe Rectangle permet de créer un rectangle avec
    une largeur et une hauteur,
    et d'effectuer des calculs d'aire et de périmètre.

    Attributs:
        width (int): La largeur du rectangle. Doit être un entier >= 0.
        height (int): La hauteur du rectangle. Doit être un entier >= 0.

    Méthodes:
        __init__(self, width=0, height=0):
            Initialise un rectangle avec une largeur et une hauteur données.

        width (getter, setter):
            Accède à la largeur du rectangle. Définit la largeur en vérifiant
            qu'elle est un entier et >= 0.

        height (getter, setter):
            Accède à la hauteur du rectangle. Définit la hauteur en vérifiant
            qu'elle est un entier et >= 0.

        __str__(self):
            Retourne une chaîne représentant visuellement
            le rectangle avec des `#`.
            Si la largeur ou la hauteur est égale à 0,
            retourne une chaîne vide.

        __repr__(self):
            Retourne une chaîne qui permet de recréer l'objet avec eval().
            La chaîne est sous la forme "Rectangle(width, height)".

        area(self):
            Calcule et retourne l'aire du rectangle (largeur * hauteur).

        perimeter(self):
            Calcule et retourne le périmètre du rectangle
            (2 * (largeur + hauteur)).
            Si la largeur ou la hauteur est égale à 0, retourne 0.

        my_print(self):
            Affiche le rectangle avec des `#` et la représentation de l'objet.
            Si la largeur ou la hauteur est égale à 0, affiche une ligne vide.
    """

    def __init__(self, width=0, height=0):
        """
        Initialise un rectangle avec la largeur et la hauteur spécifiées.

        Paramètres:
            width (int): La largeur du rectangle. Défaut à 0 si non spécifié.
            height (int): La hauteur du rectangle. Défaut à 0 si non spécifié.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retourne la largeur du rectangle.

        Retour:
            int: La largeur du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur du rectangle. Vérifie que la
        largeur est un entier et >= 0.

        Paramètres:
            value (int): La largeur du rectangle.

        Lève:
            TypeError: Si la largeur n'est pas un entier.
            ValueError: Si la largeur est inférieure à 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retourne la hauteur du rectangle.

        Retour:
            int: La hauteur du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur du rectangle. Vérifie que la hauteur
        est un entier et >= 0.

        Paramètres:
            value (int): La hauteur du rectangle.

        Lève:
            TypeError: Si la hauteur n'est pas un entier.
            ValueError: Si la hauteur est inférieure à 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant le rectangle par des #.

        Retour:
            str: La représentation visuelle du rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """
        Retourne une chaîne qui permet de recréer l'objet avec eval().

        Retour:
            str: La chaîne de représentation du rectangle sous la forme
                 "Rectangle(width, height)".
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Retour:
            int: L'aire du rectangle (largeur * hauteur).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule et retourne le périmètre du rectangle.

        Retour:
            int: Le périmètre du rectangle (2 * (largeur + hauteur)).
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def my_print(self):
        """
        Affiche le rectangle avec des # et la représentation de l'objet.

        Si la largeur ou la hauteur est égale à 0, affiche une ligne vide.
        """
        print(self.__str__())  # Afficher le rectangle avec des #
        print(self)  # Afficher la représentation classique de l'objet
