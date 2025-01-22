def max_integer(my_list=[]):
    # Si la liste est vide, retourner None
    if not my_list:
        return None
    
    # Initialiser la variable max avec le premier élément de la liste
    max_num = my_list[0]
    
    # Parcourir la liste et comparer chaque élément avec le max actuel
    for num in my_list:
        if num > max_num:
            max_num = num
    
    return max_num