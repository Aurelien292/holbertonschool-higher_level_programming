#!/usr/bin/python3
"""
    Représente un carré avec une taille spécifiée et permet
    des comparaisons basées sur l'aire.
"""


class Square:
    """
    Représente un carré avec une taille spécifiée et permet
    des comparaisons basées sur l'aire.

    Attributs:
        size (int, float): Taille du côté du carré, doit être un nombre >= 0.

    Méthodes:
        __init__(size=0):
            Initialise un carré avec une taille donnée.
            Par défaut, la taille est 0.

        size:
            Propriété pour obtenir la taille du côté du carré.
            La taille doit être un nombre (entier ou flottant)
            supérieur ou égal à 0.

        size.setter:
            Propriété pour définir la taille du côté du carré.
            La taille doit être un nombre (entier ou flottant)
            supérieur ou égal à 0.
            Si ce n'est pas le cas, une erreur `TypeError`
            ou `ValueError` est levée.

        area():
            Calcule et retourne l'aire du carré (c'est-à-dire
            la taille du côté au carré).

        __eq__(other):
            Compare l'aire du carré avec celle d'un autre carré.
            Retourne `True` si les aires sont égales, sinon `False`.

        __ne__(other):
            Compare l'aire du carré avec celle d'un autre carré.
            Retourne `True` si les aires sont différentes, sinon `False`.

        __gt__(other):
            Compare l'aire du carré avec celle d'un autre carré.
            Retourne `True` si l'aire du carré est plus grande
            que celle de l'autre, sinon `False`.

        __ge__(other):
            Compare l'aire du carré avec celle d'un autre carré.
            Retourne `True` si l'aire du carré est plus grande
            ou égale à celle de l'autre, sinon `False`.

        __lt__(other):
            Compare l'aire du carré avec celle d'un autre carré.
            Retourne `True` si l'aire du carré est plus petite que
            celle de l'autre, sinon `False`.

        __le__(other):
            Compare l'aire du carré avec celle d'un autre carré.
            Retourne `True` si l'aire du carré est plus petite ou
            égale à celle de l'autre, sinon `False`.
    """

    def __init__(self, size=0):
        """
        Initialise un carré avec une taille donnée.
        Par défaut, la taille est 0.

        Paramètres:
            size (int, float): La taille du côté du carré.
            Par défaut, la taille est 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retourne la taille du côté du carré.

        Retourne:
            float: La taille du côté du carré.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Définit la taille du côté du carré. La taille doit être un nombre >= 0.

        Paramètres:
            size (int, float): La taille du côté du carré.

        Lève:
            TypeError: Si `size` n'est ni un entier ni un flottant.
            ValueError: Si `size` est inférieur à 0.
        """
        if type(size) is not int and type(size) is not float:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré (c'est-à-dire
        la taille du côté au carré).

        Retourne:
            float: L'aire du carré.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare l'aire du carré avec celle d'un autre carré.

        Paramètres:
            other (Square): L'autre carré à comparer.

        Retourne:
            bool: `True` si les aires des deux carrés sont
            égales, sinon `False`.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compare l'aire du carré avec celle d'un autre carré.

        Paramètres:
            other (Square): L'autre carré à comparer.

        Retourne:
            bool: `True` si les aires des deux carrés sont
            différentes, sinon `False`.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return False

    def __gt__(self, other):
        """
        Compare l'aire du carré avec celle d'un autre carré.

        Paramètres:
            other (Square): L'autre carré à comparer.

        Retourne:
            bool: `True` si l'aire du carré est plus grande
            que celle de l'autre carré, sinon `False`.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Compare l'aire du carré avec celle d'un autre carré.

        Paramètres:
            other (Square): L'autre carré à comparer.

        Retourne:
            bool: `True` si l'aire du carré est plus grande ou égale à
            celle de l'autre carré, sinon `False`.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Compare l'aire du carré avec celle d'un autre carré.

        Paramètres:
            other (Square): L'autre carré à comparer.

        Retourne:
            bool: `True` si l'aire du carré est plus petite que celle de
            l'autre carré, sinon `False`.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Compare l'aire du carré avec celle d'un autre carré.

        Paramètres:
            other (Square): L'autre carré à comparer.

        Retourne:
            bool: `True` si l'aire du carré est plus petite ou égale à celle de
            l'autre carré, sinon `False`.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
