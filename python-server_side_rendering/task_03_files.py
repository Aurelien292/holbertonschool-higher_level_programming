from flask import Flask, render_template, request
from read_all import read, read_csv_data, read_json_data


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
      
      file_name = "items.json"
      items = read(file_name)
      return render_template('items.html', items=items)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")
	
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
       app.run(debug=True, port=5000)