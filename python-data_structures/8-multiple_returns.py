def multiple_returns(sentence):
    # Vérifier si la chaîne est vide
    if sentence == "":
        return (0, None)
    else:
        # Retourner un tuple avec la longueur de la chaîne et son premier caractère
        return (len(sentence), sentence[0])