from flask import request, jsonify, Flask


app = Flask(__name__)

users = {}


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
        return jsonify({"error": "Username is required"}), 400

    users[data['username']] = {
        "username": data['username'], "name": data['name'],
        "age": data['age'], "city": data['city']
    }

    return jsonify({"message": "User added", "user": users[data['username']]})


if __name__ == "__main__":
    app.run(debug=True)
