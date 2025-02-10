#!/usr/bin/python3
"""
Ajoute les arguments de la ligne de commande dans un fichier JSON.
"""
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
"""
Ajoute les arguments de la ligne de commande dans un fichier JSON.

1. Charge la liste existante depuis un fichier JSON (si disponible).
2. Ajoute les nouveaux arguments à la liste.
3. Sauvegarde la liste mise à jour dans le fichier JSON.

Le fichier JSON est créé s'il n'existe pas.

Aucun argument externe n'est passé à la fonction
(les arguments sont récupérés via sys.argv).
"""
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
