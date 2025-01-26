#!/usr/bin/python3
"""Ce module contient une fonction appelée text_indentation.
Elle permet de diviser un texte en plusieurs lignes à chaque fois
qu'un des caractères de ponctuation ., ?, ou : est rencontré.
Il supprime également les espaces inutiles avant et après chaque ligne. """


def text_indentation(text):
    """La fonction text_indentation prend une chaîne de texte en entrée et
    sépare cette chaîne en lignes. Elle recherche les caractères de ponctuation
    ., ? et : pour déterminer où diviser le texte. Si des espaces superflus
    existent avant ou après ces divisions, ils sont supprimés."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    for c in range(len(text)):
        line += text[c]
        if text[c] in ".?:":
            # supprimer les espaces (ou autres caractères spécifiés) au
            # début d'une chaîne de caractères.
            print((line + '\n').lstrip(' '))
            line = ""
    print(line.lstrip(' '), end='')
