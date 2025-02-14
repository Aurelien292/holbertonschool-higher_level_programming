import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Sérialise un dictionnaire Python en XML et l'enregistre dans un fichier."""
    try:
        # Créer un élément racine <data>
        root = ET.Element("data")
        
        # Ajouter des éléments enfants pour chaque entrée du dictionnaire
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Convertir la valeur en chaîne de caractères
        
        # Créer un arbre XML et l'écrire dans le fichier
        tree = ET.ElementTree(root)
        tree.write(filename)
        
        print(f"Données sérialisées dans le fichier {filename}")
        return True
    except Exception as e:
        print(f"Erreur lors de la sérialisation : {e}")
        return False

def deserialize_from_xml(filename):
    """Désérialise un fichier XML et reconstruit un dictionnaire Python."""
    try:
        # Parser le fichier XML
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Créer un dictionnaire pour stocker les données
        dictionary = {}
        
        # Parcourir les éléments XML et les ajouter dans le dictionnaire
        for child in root:
            # Récupérer la clé (nom de l'élément) et la valeur (texte de l'élément)
            key = child.tag
            value = child.text
            
            # Tentative de conversion de la valeur en entier ou en booléen si possible
            if value.isdigit():
                value = int(value)
            elif value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
                
            # Ajouter au dictionnaire
            dictionary[key] = value
        
        print(f"Données désérialisées depuis le fichier {filename}")
        return dictionary
    except Exception as e:
        print(f"Erreur lors de la désérialisation : {e}")
        return None


# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple de dictionnaire à sérialiser
    data = {
        "name": "John",
        "age": 25,
        "is_student": True
    }
    
    # Sérialisation du dictionnaire en fichier XML
    if serialize_to_xml(data, "data.xml"):
        # Désérialisation du fichier XML en dictionnaire
        loaded_data = deserialize_from_xml("data.xml")
        print(loaded_data)
