#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sommes_des_produits = 0
    sommes_des_poids = 0

    for valeur, poids in my_list:
        sommes_des_produits += valeur * poids
        sommes_des_poids += poids

    if sommes_des_poids == 0:
        return 0
    return sommes_des_produits / sommes_des_poids
