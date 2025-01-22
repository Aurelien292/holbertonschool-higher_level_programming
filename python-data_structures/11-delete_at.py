def delete_at(my_list=[], idx=0):
    # Vérifier si l'index est valide (positif et dans la plage de la liste)
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
