import csv
import json
import sqlite3

def read_json_data():
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)  # Charger le contenu du fichier JSON
            return data['products']  # Assurez-vous de renvoyer la liste de produits
    except Exception as e:
        return None

def read_csv_data():
    """Lire les données depuis un fichier CSV."""
    try:
        products = []
        with open('products.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)  # Vérifier le contenu de chaque ligne
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except Exception as e:
        return None
            
def read(filename):
     with open(filename, "r") as file:
        data = json.load(file)
        values = data.get("items", [])
        return values
            
def get_products_from_sql():
    """Fonction pour obtenir les produits depuis la base de données SQLite."""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        products = cursor.fetchall()
        conn.close()
        
        # Convertir les résultats en format de dictionnaire pour correspondre à ce que Jinja attend
        return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]
    except Exception as e:
        print(f"Erreur lors de la récupération des données de la base de données: {e}")
        return None