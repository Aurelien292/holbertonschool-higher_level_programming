import xml.etree.ElementTree as ET
from xml.dom import minidom

def serialize_to_xml(dictionary, filename):
    """Sérialise un dictionnaire Python en XML et l'enregistre dans un fichier."""
    try:
        # Créer un élément racine <data>
        root = ET.Element("data")
        
        # Ajouter des éléments enfants pour chaque entrée du dictionnaire
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Convertir la valeur en chaîne de caractères
        
        # Créer un arbre XML
        tree = ET.ElementTree(root)
        
        # Utiliser la méthode write avec un joli format (indentation)
        # Pour ajouter des indentations et des sauts de ligne dans le fichier
        with open(filename, "wb") as xml_file:
            tree.write(xml_file)
        
        # Lire le fichier pour ajouter une indentation
        with open(filename, "r") as file:
            xml_string = file.read()

        # Utiliser un processus manuel pour appliquer l'indentation
        # Transformer l'arbre XML en chaîne de caractères avec un joli format
        formatted_xml = minidom.parseString(xml_string).toprettyxml(indent="    ")

        # Réécrire le fichier avec un joli format
        with open(filename, "w") as xml_file:
            xml_file.write(formatted_xml)

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
