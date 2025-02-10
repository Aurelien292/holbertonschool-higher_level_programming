#!/usr/bin/python3
"""
    Ajoute une chaîne de caractères à la fin d'un fichier texte (UTF-8).
    """


def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d'un fichier texte (UTF-8).

    Args:
        filename (str): Le nom du fichier où ajouter la chaîne. Si le fichier
        n'existe pas, il sera créé.
        text (str): La chaîne à ajouter dans le fichier.

    Returns:
        int: Le nombre de caractères ajoutés dans le fichier.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
