"""
    Retourne True si l'objet est une instance de la classe spécifiée,
    ou d'une sous-classe de cette classe, sinon retourne False.
"""


def is_kind_of_class(obj, a_class):
    """
    Retourne True si l'objet est une instance de la classe spécifiée,
    ou d'une sous-classe de cette classe, sinon retourne False.

    Arguments :
    obj -- L'objet à tester.
    a_class -- La classe à comparer avec l'objet.

    Retourne :
    bool -- True si obj est une instance de a_class ou d'une
    sous-classe de a_class, sinon False.
    """
    return isinstance(obj, a_class)
