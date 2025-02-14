#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """Convertit un fichier CSV en un fichier JSON."""
    try:
        # Ouvrir le fichier CSV
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            # Lire les données du fichier CSV
            csv_reader = csv.DictReader(csv_file)
            # Convertir chaque ligne en dictionnaire et les ajouter à une liste
            data = [row for row in csv_reader]
        
        # Sérialiser la liste de dictionnaires en JSON et l'écrire dans un fichier
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        # Retourner True si la conversion est réussie
        return True

    except FileNotFoundError:
        # Si le fichier CSV n'est pas trouvé
        print(f"Erreur : Le fichier {csv_filename} est introuvable.")
        return False
    except Exception as e:
        # Si une autre erreur se produit
        print(f"Erreur lors de la conversion : {e}")
        return False

# Exemple d'utilisation
if __name__ == "__main__":
    result = convert_csv_to_json("data.csv")
    if result:
        print("La conversion a réussi et les données ont été enregistrées dans 'data.json'.")
    else:
        print("La conversion a échoué.")
