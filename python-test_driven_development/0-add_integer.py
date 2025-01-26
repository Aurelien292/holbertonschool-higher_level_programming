#!/usr/bin/python3
"""Ce module a une fonction def add_integer """


def add_integer(a, b=98):

    """Fonction acceptant des int et des float ,retourne la somme
    de a et b une fois convertie en int """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
