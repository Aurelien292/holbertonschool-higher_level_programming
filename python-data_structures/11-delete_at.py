#!/usr/bin/python3
def delete_at(my_list=None, idx=0):
    if my_list is None:
        my_list = []
    # Créer une copie de la liste pour ne pas modifier la liste d'origine
    my_list_copy = my_list[:]
    # Si l'index est valide, on supprime l'élément
    if idx >= 0 and idx < len(my_list_copy):
        del my_list_copy[idx]
    # Retourner la copie modifiée
    return my_list_copy
