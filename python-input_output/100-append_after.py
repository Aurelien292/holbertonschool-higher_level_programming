def append_after(filename="", search_string="", new_string=""):
    # Ouvrir le fichier en mode lecture et écriture
    with open(filename, 'r') as file:
        # Lire toutes les lignes du fichier
        lines = file.readlines()
    
    # Ouvrir le fichier en mode écriture pour le modifier
    with open(filename, 'w') as file:
        for line in lines:
            # Écrire la ligne existante dans le fichier
            file.write(line)
            
            # Si la ligne contient la chaîne recherchée, ajouter la nouvelle chaîne
            if search_string in line:
                file.write(new_string)
