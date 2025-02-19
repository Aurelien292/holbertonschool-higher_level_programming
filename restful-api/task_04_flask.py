from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route('/')
def home():
    return"Welcome to the Flask API!"

@app.route('/data')
def get_users():
    return jsonify(users)

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/status')
def status():
    return "OK"

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    
    if not data or not data.get('username'):
        return jsonify ({"error": "Username is required"}), 400
    
    users[data['username']] ={
		"name": data['name'],
        "age": data['age'],
        "city": data['city']
	}
    
    return jsonify({"message": "User added", "user": users[data['username']]})

if __name__ == "__main__":
    app.run(debug=True)

