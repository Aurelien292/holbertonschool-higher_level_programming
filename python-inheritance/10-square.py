#!/usr/bin/python3


"""
    Classe représentant un rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle
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
