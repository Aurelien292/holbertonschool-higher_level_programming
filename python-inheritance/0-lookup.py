#!/usr/bin/python3
"""
    Retourne la liste des attributs et méthodes d'un objet.
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes d'un objet.

    Arguments :
    obj -- L'objet à inspecter.

    Retourne :
    list -- Liste des noms des attributs et méthodes accessibles de l'objet.
    """
    return dir(obj)
