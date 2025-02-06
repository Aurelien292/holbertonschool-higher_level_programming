#!/usr/bin/python3
"""
Cree une class BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
    lève une exception pour indiquer
    que la méthode n'est pas implémentée
    dans la class de base.
    """
        raise Exception("area() is not implemented")

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
        if name is None or value is None:
            raise TypeError(f"Missing required arguments: 'name' and 'value'")
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
