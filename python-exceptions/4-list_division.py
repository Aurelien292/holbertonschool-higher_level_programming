#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            val_1 = my_list_1[i]  # Récupère l'élément my_list_1 à l'indice i
            val_2 = my_list_2[i]  # Récupère l'élément my_list_2 à l'indice i

            try:
                # Convertir val_1 et val_2 en float
                val_1 = float(val_1)
                val_2 = float(val_2)
            except ValueError:
                # Si la conversion échoue, on affiche "wrong type"
                print("wrong type")
                result.append(0)  # Ajouter 0 dans le résultat
                continue  # Passer à l'itération suivante

            try:
                # Diviser les deux valeurs
                result.append(val_1 / val_2)
            except ZeroDivisionError:
                # Si division par zéro, on affiche "division by 0"
                print("division by 0")
                result.append(0)  # Ajouter 0 dans le résultat

        except IndexError:
            # Si l'indice dépasse la longueur des listes
            print("out of range")
            result.append(0)  # Ajouter 0 dans le résultat

    return result  # Retourner la liste des résultats
