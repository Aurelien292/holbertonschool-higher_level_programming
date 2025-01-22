#!/usr/bin/python3
# map:map() pour appliquer une fonction à chaque élément de la liste
# La fonction lambda vérifie si l'élément est égal à search.
# Si c’est le cas,il est remplacé par replace
def search_replace(my_list, search, replace):
    return list(map(lambda x: replace if x == search else x, my_list))
