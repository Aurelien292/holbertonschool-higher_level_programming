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
        Trie la liste par insertion et affiche la liste triée en ordre croissant.
        """
        # On copie la liste pour ne pas modifier l'originale
        new_list = self[:]
        
        # Tri par insertion (algorithme simple)
        for i in range(1, len(new_list)):
            key = new_list[i]
            j = i - 1
            # Déplacer les éléments plus grands que key d'une position vers la droite
            while j >= 0 and key < new_list[j]:
                new_list[j + 1] = new_list[j]
                j -= 1
            new_list[j + 1] = key
        
        # Affichage de la liste triée
        print(new_list)
