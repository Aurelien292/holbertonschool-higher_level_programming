#!/usr/bin/python3
"""
Ce module a une fonction def print_square.
Fonction acceptant les int pour controler une taille
"""


def print_square(size):

    """Si l'argument n'est pas un int ,
    elle lève une exception TypeError ou
    si l'argument est plus petit que 0 ValueError.
    Autrement affiche des "#" .
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    print(("#" * size + '\n') * size, end='')
    print()
