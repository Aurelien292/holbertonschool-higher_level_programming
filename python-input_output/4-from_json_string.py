#!/usr/bin/python3
import json
"""
    Convertit une chaîne JSON en objet Python.
    """


def from_json_string(my_str):
    """
    Convertit une chaîne JSON en objet Python.

    Args:
        my_str (str): La chaîne JSON à convertir.

    Returns:
        obj: L'objet Python représenté par la chaîne JSON.
    """
    return json.loads(my_str)
