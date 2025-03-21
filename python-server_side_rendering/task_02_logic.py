from flask import Flask, render_template
import json

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


if __name__ == '__main__':
       app.run(debug=True, port=5000)