#!/usr/bin/python3
"""
Cree une class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    Classe Rectangle qui hérite de BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui hérite de BaseGeometry.

    Cette classe représente un rectangle et utilise la validation des entiers
    pour la largeur et la hauteur via la méthode `integer_validator`
    de la classe de base.

    Attributs :
    - __width (int): Largeur du rectangle, validée comme étant un entier
    positif.
    - __height (int): Hauteur du rectangle, validée comme étant un entier
    positif.

    Méthodes :
    - __init__(width, height) : Initialise un rectangle avec une largeur
    et une hauteur valides.
    """

    def __init__(self, width, height):
        """
        Initialise un objet Rectangle avec la largeur et la hauteur valides.

        Cette méthode valide la largeur et la hauteur à l'aide de
        `integer_validator`
        avant de les assigner aux attributs privés `__width` et `__height`.

        Arguments :
        - width (int): La largeur du rectangle.
        - height (int): La hauteur du rectangle.

        Lève :
        - TypeError: Si `width` ou `height` ne sont pas des entiers.
        - ValueError: Si `width` ou `height` sont inférieurs ou égaux à zéro.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
