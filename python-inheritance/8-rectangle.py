#!/usr/bin/python3
"""
Cree une class BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):
        raise Exception("area() is not implemented")
    """
    lève une exception pour indiquer
    que la méthode n'est pas implémentée
    dans la class de base.
    """

    def integer_validator(self, name, value):
        """
        Valide si la valeur est un entier supérieur à 0.
        Si la valeur n'est pas un entier, lève une exception TypeError.
        Si la valeur est inférieure ou égale à 0, lève une exception
        ValueError.

        Arguments :
        name -- Le nom de l'attribut (toujours une chaîne de caractères).
        value -- La valeur à valider (doit être un entier supérieur à 0).
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
