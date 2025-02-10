#!/usr/bin/python3
import json
"""
    Sauvegarde un objet Python dans un fichier au format JSON.
    """


def save_to_json_file(my_obj, filename):
    """
    Sauvegarde un objet Python dans un fichier au format JSON.

    Args:
        my_obj (obj): L'objet Python à sauvegarder.
        filename (str): Le nom du fichier où sauvegarder l'objet.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
