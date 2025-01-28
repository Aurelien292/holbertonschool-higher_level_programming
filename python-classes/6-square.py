#!usr/bin/python3
"""
Module qui définit une classe Square représentant un carré.
"""


class Square:
    """
    Classe représentant un carré avec une taille de côté et une
    position spécifiées.

    Attributs:
        size (int): Taille du côté du carré, doit être un entier >= 0.
        position (tuple): Position du carré, tuple de 2 entiers positifs
        représentant les coordonnées (x, y).
        obj (tuple): Optionnel, un objet qui peut affecter la position
        du carré si sa structure est correcte.

    Méthodes:
        __init__(size, position=(0, 0), obj=None): Initialise un carré avec
        une taille et une position optionnelles, vérifie l'argument obj.
        size: Propriété pour obtenir la taille du carré.
        size.setter: Propriété pour définir la taille du carré avec validation.
        my_print(): Affiche le carré en utilisant des symboles '#' en
        fonction de la taille et de la position.
        area(): Retourne l'aire du carré.
    """

    def __init__(self, size, position=(0, 0), obj=None):
        """
        Initialise un carré avec une taille et une position données,
        avec une validation pour la position.

        Paramètres:
            size (int): Taille du côté du carré.
            position (tuple): Position du carré sous forme de tuple (x, y),
            valeurs par défaut (0, 0).
            obj (tuple, optional): Optionnel, un objet qui peut influencer
            la position si sa structure est correcte.

        Lève:
            TypeError: Si size n'est pas un entier, ou si position
            n'est pas un tuple de 2 entiers positifs.
            ValueError: Si size est inférieur à 0.
        """
        self.size = size
        self.position = position
        if position is not None and obj is not None:
            try:
                obj_0 = obj[0]
                obj_1 = obj[1]
                if isinstance(obj_0, int) and isinstance(obj_1, int):
                    self.position = position
                    self.obj = obj
                else:
                    raise TypeError("position must be a tuple of 2\
                                    positive integers")
            except (IndexError, TypeError):
                raise TypeError("position must be a tuple of 2\
                                positive integers")

    @property
    def size(self):
        """
        Retourne la taille du côté du carré.

        Retourne:
            int: La taille du côté du carré.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Définit la taille du côté du carré après validation.

        Paramètres:
            size (int): La nouvelle taille du côté du carré.

        Lève:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """
        Affiche le carré formé de '#' en fonction de la taille et de
        la position.

        Si la position est spécifiée, elle décalera l'affichage du
        carré en fonction des valeurs x et y.
        Si la taille est 0, aucune ligne ne sera imprimée.
        """
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(' ' * self.position[0] + '#' * self.size)

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Retourne:
            int: L'aire du carré (size ** 2).
        """
        return self.__size * self.__size
