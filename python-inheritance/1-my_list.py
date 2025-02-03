#!/usr/bin/python3
"""
        Affiche la liste triée en ordre croissant.
        """


class MyList(list):
    def print_sorted(self):
        """
        Affiche la liste triée en ordre croissant.
        """
        print(sorted(self))
