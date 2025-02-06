#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.

    Cette classe définit les méthodes abstraites `area()` et `perimeter()`,
    qui doivent être implémentées dans toute sous-classe.

    Méthodes abstraites :
        area() : Méthode qui doit être définie dans les sous-classes pour
                 calculer l'aire de la forme.
        perimeter() : Méthode qui doit être définie dans les sous-classes
                      pour calculer le périmètre de la forme.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Classe représentant un cercle.

    Hérite de la classe `Shape` et implémente les méthodes `area()` et
    `perimeter()` pour calculer l'aire et le périmètre d'un cercle.

    Attributs :
        radius (float) : Le rayon du cercle.

    Méthodes :
        area() : Calcule l'aire du cercle (π * rayon^2).
        perimeter() : Calcule le périmètre du cercle (2 * π * rayon).
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Classe représentant un rectangle.

    Hérite de la classe `Shape` et implémente les méthodes `area()` et
    `perimeter()` pour calculer l'aire et le périmètre d'un rectangle.

    Attributs :
        width (float) : La largeur du rectangle.
        height (float) : La hauteur du rectangle.

    Méthodes :
        area() : Calcule l'aire du rectangle (largeur * hauteur).
        perimeter() : Calcule le périmètre du rectangle
        (2 * (largeur + hauteur)).
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Affiche l'aire et le périmètre d'une forme donnée.

    Cette fonction prend un objet shape en entrée, et utilise le duck typing
    pour appeler ses méthodes `area()` et `perimeter()`. Si ces méthodes
    sont présentes, leurs résultats seront imprimés. En cas d'absence de ces
    méthodes, une exception `AttributeError` est levée et ignorée.

    Arguments :
        shape : Un objet ayant les méthodes `area()` et `perimeter()`.
    """
    try:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")

    except AttributeError:
        None
