#!/usr/bin/python3
"""
Fonction qui retourne un triangle pascal
"""


def pascal_triangle(n):
    # Si n <= 0, on retourne une liste vide
    if n <= 0:
        return []
    """
Retourne une liste vide si ( n )  est plus petit ou égale à 0
"""

    # Initialisation du triangle avec la première ligne
    triangle = [[1]]

    # On génère les autres lignes du triangle
    for i in range(1, n):
        # On commence chaque ligne par [1]
        row = [1]
        # On calcule les éléments du milieu de la ligne
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # On termine la ligne par [1]
        row.append(1)
        # On ajoute la ligne au triangle
        triangle.append(row)
        """
Retourne list int pour representé un triangle Pascal
"""
    return triangle
