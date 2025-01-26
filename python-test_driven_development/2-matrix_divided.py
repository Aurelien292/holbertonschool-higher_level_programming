#!/usr/bin/python3
"""
    Retourne une nouvelle matrice où chaque élément a été divisé par div.

    Args:
        matrix (list): Liste de listes d'entiers ou de flottants.
        div (int, float): Le diviseur, doit être >= 0.
    """


def matrix_divided(matrix, div):
    """
    Retourne une nouvelle matrice où chaque élément a été divisé par div.

    Args:
        matrix (list): Liste de listes d'entiers ou de flottants.
        div (int, float): Le diviseur, doit être >= 0.
    """
    # Vérifie si 'matrix' est bien une liste
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    # Vérifie si chaque ligne de 'matrix' est une liste
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
                            of integers/floats")

        # Vérifie si chaque élément de la ligne est un int ou un float
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
                                of integers/floats")

    # Vérifie que 'div' est un nombre (int ou float)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    # Vérifie que 'div' n'est pas égal à zéro
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divise chaque élément de la matrice par div et arrondit
    # le résultat à 2 décimales
    return [[round(i / div, 2) for i in row] for row in matrix]
