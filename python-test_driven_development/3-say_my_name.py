#!usr/bin/python3
"""
Ce module a une fonction def say_my_name.
Fonction acceptant les str pour first name et last name
si first name ou last name n'est pas un string retourn une erreur
"""


def say_my_name(first_name, last_name=""):

    """Si l'un des arguments n'est pas une chaine de charactere,
    elle lève une exception TypeError. Autrement affiche
    first name ou last name ou les deux . """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
