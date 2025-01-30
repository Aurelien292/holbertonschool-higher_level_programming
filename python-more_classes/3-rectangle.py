#!/usr/bin/python3
"""
    Représente un rectangle avec une largeur et une hauteur spécifiées.
"""


class Rectangle:
    """
    Représente un rectangle avec une largeur et une hauteur spécifiées.

    La classe Rectangle permet de créer un rectangle en spécifiant sa
    largeur et sa hauteur,
    d'effectuer des calculs d'aire et de périmètre, et d'afficher une
    représentation visuelle
    du rectangle à l'aide de caractères '#' ainsi que la représentation
    classique de l'objet.

    Attributs:
        width (int): La largeur du rectangle.
        height (int): La hauteur du rectangle.

    Méthodes:
        __init__(self, width=0, height=0):
            Initialise un nouvel objet Rectangle avec une largeur et
            une hauteur données.

        width (getter, setter):
            Accède à la largeur du rectangle. Définit la largeur en vérifiant
            qu'elle est un entier et >= 0.

        height (getter, setter):
            Accède à la hauteur du rectangle. Définit la hauteur en vérifiant
            qu'elle est un entier et >= 0.

        __str__(self):
            Retourne une représentation visuelle du rectangle à l'aide
            de caractères '#'.
            Si la largeur ou la hauteur est 0, renvoie une chaîne vide.

        __repr__(self):
            Retourne la représentation classique de l'objet sous la forme:
            <3-rectangle.Rectangle object at 0x...>

        area(self):
            Calcule et retourne l'aire du rectangle (largeur * hauteur).

        perimeter(self):
            Calcule et retourne le périmètre du rectangle
            (2 * (largeur + hauteur)).

        my_print(self):
            Affiche la représentation visuelle du rectangle à l'aide
            de caractères '#'
            et ensuite la représentation classique de l'objet.
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
        Définit la largeur du rectangle. Vérifie que la largeur
        est un entier et >= 0.

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
        Définit la hauteur du rectangle. Vérifie que la hauteur est
        un entier et >= 0.

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
        Retourne une représentation visuelle du rectangle à
        l'aide de caractères '#'.

        Si la largeur ou la hauteur est 0, renvoie une chaîne vide.

        Retour:
            str: La représentation visuelle du rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """
        Retourne la représentation classique de l'objet sous la forme:
        <3-rectangle.Rectangle object at 0x...>

        Retour:
            str: La représentation classique de l'objet.
        """
        return ("<3-rectangle." +
                f"{self.__class__.__name__} object at {hex(id(self))}>")

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
        if self.width < 0 or self.height < 0:
            return 0
        return 2 * (self.width + self.height)

    def my_print(self):
        """
        Affiche la représentation visuelle du rectangle à l'aide
        de caractères '#',
        puis la représentation classique de l'objet.

        Si la largeur ou la hauteur est 0, n'affiche rien.
        """
        if self.width == 0 or self.height == 0:
            print("")
        else:
            print(self.__str__())  # Afficher les # pour le rectangle
            print(self)  # Afficher la représentation classique de l'objet
