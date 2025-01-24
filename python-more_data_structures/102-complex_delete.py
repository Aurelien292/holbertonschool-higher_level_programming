#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for Key, Valeur in a_dictionary.items():
            if Valeur == value:
                del a_dictionary[Key]
                break
    return a_dictionary
