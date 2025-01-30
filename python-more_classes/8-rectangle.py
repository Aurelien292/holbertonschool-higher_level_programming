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
    # Déclare un attribut de classe pour suivre le nombre d'instances
    number_of_instances = 0
    # Déclare un attribut de classe pour afficher differents symbols
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise un rectangle avec la largeur et la hauteur spécifiées.

        Paramètres:
            width (int): La largeur du rectangle. Défaut à 0 si non spécifié.
            height (int): La hauteur du rectangle. Défaut à 0 si non spécifié.
        """
        self.__width = width
        self.__height = height
        """
        Incrémente le compteur d'instances lors de la création
        d'une nouvelle instance
        """
        Rectangle.number_of_instances += 1

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
        Retourne une chaîne représentant le rectangle avec le symbole
        `print_symbol`.

        Retour:
            str: Représentation du rectangle sous forme de
            `print_symbol` ou une
            chaîne vide si les dimensions sont nulles.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width
                          for _ in range(self.height)])

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

    def __del__(self):
        """
        Cette méthode est appelée lorsqu'une instance de Rectangle
        est supprimée.
        """
        print("Bye rectangle...")

        """Décrémenter le compteur d'instances lors
         de la suppression d'une instance
        """
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Retourne le rectangle ayant la plus grande aire.
        Si les deux rectangles ont la même aire, retourne rect_1.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_3 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
