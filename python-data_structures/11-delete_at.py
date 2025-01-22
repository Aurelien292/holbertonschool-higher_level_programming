def delete_at(my_list=None, idx=0):
    # Si my_list est None, l'initialiser à une liste vide
    if my_list is None:
        my_list = []
    # Vérifier si l'index est valide (positif et dans la plage de la liste)
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]  # Supprimer l'élément à l'index spécifié

    return my_list
