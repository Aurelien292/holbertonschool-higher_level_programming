#!/usr/bin/python3
import socket
import json

def start_server(host='127.0.0.1', port=12345):
    # Créer le socket du serveur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Lier le socket à l'adresse et au port spécifiés
    server_socket.bind((host, port))
    
    # Commencer à écouter les connexions entrantes
    server_socket.listen(1)
    print(f"Le serveur écoute sur {host}:{port}...")
    
    # Accepter une connexion entrante
    connection, address = server_socket.accept()
    print(f"Connexion établie avec {address}")
    
    # Lire les données envoyées par le client
    data = connection.recv(1024)  # Recevoir jusqu'à 1024 octets
    if data:
        # Désérialiser les données JSON pour recréer le dictionnaire
        received_dict = json.loads(data.decode())
        print("Dictionnaire reçu :", received_dict)
    
    # Fermer la connexion
    connection.close()
    
def send_data(host='127.0.0.1', port=12345):
    # Créer un dictionnaire à envoyer
    data_dict = {
        'name': 'John',
        'age': 28,
        'city': 'New York'
    }
    
    # Sérialiser le dictionnaire en JSON
    serialized_data = json.dumps(data_dict)
    
    # Créer un socket pour se connecter au serveur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Se connecter au serveur
        client_socket.connect((host, port))
        
        # Envoyer les données sérialisées
        client_socket.send(serialized_data.encode())
        
        print("Données envoyées au serveur.")
    
    except Exception as e:
        print(f"Erreur de connexion : {e}")
    
    finally:
        # Fermer la connexion
        client_socket.close()
