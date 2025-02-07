#!/usr/bin/python3
class MyInt(int):
    """
    Classe MyInt qui hérite de la classe int et inverse les opérateurs `==`
    et `!=` de manière simple.
    """

    def __eq__(self, other):
        """Inverser l'opérateur d'égalité"""
        return False if self.real == other else True

    def __ne__(self, other):
        """Inverser l'opérateur d'inégalité"""
        return True if self.real == other else False
