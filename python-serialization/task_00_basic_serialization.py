#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et le sauvegarde dans un fichier JSON.

    :param data: Le dictionnaire à sérialiser.
    :param filename: Le nom du fichier où sauvegarder les données sérialisées.

    Exemple :
    >>> serialize_and_save_to_file({"name": "Alice", "age": 25}, "data.json")
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """
    Charge un fichier JSON et le désérialise en un dictionnaire Python.

    :param filename: Le nom du fichier JSON à charger.
    :return: Le dictionnaire désérialisé du fichier JSON.

    Exemple :
    >>> load_and_deserialize("data.json")
    {'name': 'Alice', 'age': 25}
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
