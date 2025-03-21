from flask import Flask, render_template, request
import json
from read_all import read_csv_data, read_json_data, get_products_from_sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
      return render_template('about.html')

@app.route('/contact')
def contact():
      return render_template('contact.html')
  
@app.route('/items')
def items():
    # Lire le fichier items.json
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)  # Charger le contenu du fichier JSON
        items_list = data.get('items', [])  # Récupérer la liste sous la clé 'items'
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier JSON: {e}")
        items_list = []  # Si une erreur se produit, la liste sera vide
    
    return render_template('items.html', items=items_list)


@app.route('/products')
def display_products():
    source = request.args.get('source')  # Récupérer le paramètre 'source'
    product_id = request.args.get('id', type=int)  # Récupérer le paramètre 'id', si présent

    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    elif source == 'sql':
        products = get_products_from_sql()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        # Filtrer les produits par ID
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
       app.run(debug=True, port=5000)