#!/usr/bin/python3
"""
    Ajoute un nouvel attribut à un objet si possible.
    """


def add_attribute(obj, attr, value):
    """
    Ajoute un nouvel attribut à un objet si possible.

    Si l'objet ne permet pas d'ajouter de nouveaux attributs,
    une exception TypeError est levée avec le message approprié.

    Arguments :
        obj : L'objet auquel ajouter un attribut.
        attr : Le nom de l'attribut à ajouter.
        value : La valeur de l'attribut.

    Lève :
        TypeError : Si l'objet ne peut pas avoir de nouveaux attributs.
    """
    # Vérification si l'objet ne permet pas d'ajouter des attributs
    if hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")

    # Vérifier si l'objet est un type immuable, comme str, int, etc.,
    # qui ne permet pas l'ajout d'attributs
    try:
        setattr(obj, attr, value)
    except AttributeError:
        raise TypeError("can't add new attribute")
