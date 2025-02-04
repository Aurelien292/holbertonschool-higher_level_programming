#!/usr/bin/python3
"""
    Classe représentant un rectangle.
"""


class Rectangle:
    """
    Classe représentant un rectangle.

    Attributs:
        width (int): La largeur du rectangle.
        height (int): La hauteur du rectangle.

    Méthodes:
        area(): Calcule et retourne l'aire du rectangle.
    """
    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur données.

        Paramètres:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Retourne:
            int: L'aire du rectangle (width * height).
        """
        return self.width * self.height


"""
    Classe représentant un carré, héritée de Rectangle.
"""


class Square(Rectangle):
    """
    Classe représentant un carré, héritée de Rectangle.

    Attributs:
        width (int): La largeur du carré (identique à la hauteur).
        height (int): La hauteur du carré (identique à la largeur).

    Méthodes:
        area(): Calcule et retourne l'aire du carré.
        integer_validator(name, value): Valide si la taille (size) est
        un entier positif.
        __str__(): Retourne une représentation sous forme de chaîne
        de caractères du carré.
    """

    def __init__(self, size):
        """
        Initialise un carré avec la taille donnée (size).

        Paramètres:
            size (int): La taille des côtés du carré.

        Lève:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur ou égal à 0.
        """
        self.integer_validator("size", size)

        super().__init__(size, size)

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Retourne:
            int: L'aire du carré (width * height), ici c'est size * size.
        """
        return self.width * self.height

    def integer_validator(self, name, value):
        """
        Valide que la valeur est un entier positif.

        Paramètres:
            name (str): Le nom de la variable (ici, "size").
            value (int): La valeur à valider.

        Lève:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur ou égal à 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be a positive integer")

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant le carré.

        Retourne:
            str: Une chaîne du type "[Square] size/size".
        """
        return f"[Rectangle] {self.width}/{self.height}"
