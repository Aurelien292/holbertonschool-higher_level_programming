#!/usr/bin/python3
"""
Affiche la liste triée en ordre croissant.
"""


class MyList(list):
    """
    Classe héritant de list, avec une méthode print_sorted
    pour afficher la liste triée.
    """
    def print_sorted(self):
        """
        Trie la liste en place et affiche la liste triée en ordre croissant.
        """
        new_list = self[:]   # Créer une copie de la liste
        new_list.sort()  # Trier la copie
        print(new_list)  # Afficher la copie triée
