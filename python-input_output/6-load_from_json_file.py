#!/usr/bin/python3
import json
"""
    Charge un objet Python depuis un fichier JSON.
    """


def load_from_json_file(filename):
    """
    Charge un objet Python depuis un fichier JSON.

    Args:
        filename (str): Le nom du fichier contenant la chaîne JSON.

    Returns:
        obj: L'objet Python correspondant aux données JSON du fichier.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
