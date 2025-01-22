#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []  # Créer une nouvelle liste vide pour stocker les résultats
    for num in my_list:  # Parcourir chaque élément de la liste
        if num % 2 == 0:  # Vérifier si l'élément est divisible par 2
            result.append(True)  # True si élément est divisible par 2
        else:
            result.append(False)  # Ajouter False sinon
    return result  # Retourner la liste des résultats
