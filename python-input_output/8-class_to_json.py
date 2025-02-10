#!/usr/bin/python3
"""
    Retourne un dictionnaire contenant les attributs sérialisables de l'objet.
    """


def class_to_json(obj):
    """
    Retourne un dictionnaire contenant les attributs sérialisables de l'objet.

    La fonction parcourt tous les attributs d'un objet et retourne ceux qui
    peuvent être
    sérialisés en JSON. Les types sérialisables sont : str, int, bool,
    list, dict.

    Args:
        obj (object): L'objet à convertir en dictionnaire pour
        la sérialisation JSON.

    Returns:
        dict: Un dictionnaire contenant les attributs sérialisables de l'objet.

    Exemple:
        >>> class MyClass:
        >>>     def __init__(self, name, age, active, data):
        >>>         self.name = name
        >>>         self.age = age
        >>>         self.active = active
        >>>         self.data = data
        >>>
        >>> obj = MyClass("Alice", 25, True, {"key": "value"})
        >>> class_to_json(obj)
        {'name': 'Alice', 'age': 25, 'active': True, 'data': {'key': 'value'}}
    """
    # Initialiser un dictionnaire vide
    json_dict = {}

    # Parcourir tous les attributs de l'objet
    for attr in dir(obj):
        # Ne pas inclure les attributs spéciaux (ceux qui commencent par '__')
        if not attr.startswith('__'):
            value = getattr(obj, attr)
            # Ajouter l'attribut si la valeur est sérialisable en JSON
            if isinstance(value, (str, int, bool, list, dict)):
                json_dict[attr] = value

    return json_dict
