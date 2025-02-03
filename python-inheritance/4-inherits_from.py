#!/usr/bin/python3
"""
    Retourne True si l'objet est une instance d'une classe qui hérite
    (directement ou indirectement)
    de la classe spécifiée, mais pas une instance directe de cette classe.
"""


def inherits_from(obj, a_class):
    """
    Retourne True si l'objet est une instance d'une classe qui hérite
    (directement ou indirectement)
    de la classe spécifiée, mais pas une instance directe de cette classe.

    Arguments :
    obj -- L'objet à tester.
    a_class -- La classe à comparer avec l'objet.

    Retourne :
    bool -- True si obj est une instance d'une sous-classe de a_class
    (mais pas une instance directe), sinon False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
