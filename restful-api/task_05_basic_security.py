from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Clé secrète utilisée pour signer les tokens JWT
app.config['JWT_SECRET_KEY'] = 'votre_clé_secrète'

# Initialisation de JWTManager
jwt = JWTManager(app)

# Liste des utilisateurs avec mots de passe hachés et rôles
users = {
    "admin": {"password": generate_password_hash("admin123"), "role": "admin"},
    "user": {"password": generate_password_hash("user123"), "role": "user"}
}

# Route protégée par authentification de base
@app.route('/basic-protected', methods=['GET'])
def basic_protected():
    # Récupérer les informations d'authentification dans l'en-tête de la requête
    auth = request.authorization
    if not auth or not check_password_hash(users.get(auth.username, {}).get('password', ''), auth.password):
        return jsonify({"message": "401 Unauthorized"}), 401
    return jsonify({"message": "Basic Auth: Access Granted"})


# Route pour générer un token JWT
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Vérifier les identifiants de l'utilisateur
    if username in users and check_password_hash(users[username]["password"], password):
        # Créer un token JWT avec l'identité de l'utilisateur
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Bad credentials"}), 401


# Route protégée par JWT
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"})


# Route protégée par rôle d'administrateur
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()  # Récupérer l'identité de l'utilisateur depuis le token JWT
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


if __name__ == '__main__':
    app.run(debug=True)
