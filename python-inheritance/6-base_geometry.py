#!/usr/bin/python3
"""
Cree une class BaseGeometry
"""


class BaseGeometry:
    """
lève une exception pour indiquer
que la méthode n'est pas implémentée.
"""
    def area(self):
        raise Exception("area() is not implemented")
