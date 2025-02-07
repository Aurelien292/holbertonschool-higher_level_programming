#!/usr/bin/python3
class MyInt(int):
    """
    Classe MyInt qui hérite de la classe int, mais avec les opérateurs `==`
    et `!=` inversés.
    """

    def __eq__(self, other):
        """Inverser l'opérateur d'égalité"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Inverser l'opérateur d'inégalité"""
        return not super().__ne__(other)
