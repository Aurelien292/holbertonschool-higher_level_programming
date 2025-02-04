#!/usr/bin/python3
"""
Affiche la liste triée en ordre croissant.
"""

class MyList(list):
    """
    Classe héritant de list, avec une méthode print_sorted pour afficher la liste triée.
    """
    def print_sorted(self):
        """
        Affiche la liste triée en ordre croissant.
        """
        self.sort()  # Trie la liste en place
        print(self)
