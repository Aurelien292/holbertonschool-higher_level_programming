#!/usr/bin/python3
import json
"""
    Convertit un objet Python en chaîne JSON.
    """


def to_json_string(my_obj):
    """
    Convertit un objet Python en chaîne JSON.

    Args:
        my_obj (obj): L'objet Python à convertir en JSON.

    Returns:
        str: La chaîne JSON représentant l'objet.
    """
    return json.dumps(my_obj)
