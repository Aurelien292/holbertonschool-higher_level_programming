#!/usr/bin/python3
"""
    Retourne True si l'objet est exactement une instance de
    la classe spécifiée,
    sinon retourne False.
"""


def is_same_class(obj, a_class):
    """
    Retourne True si l'objet est exactement une instance de
    la classe spécifiée,
    sinon retourne False.

    Arguments :
    obj -- L'objet à tester.
    a_class -- La classe à comparer avec l'objet.

    Retourne :
    bool -- True si obj est une instance exacte de a_class, sinon False.
    """
    return type(obj) is a_class
