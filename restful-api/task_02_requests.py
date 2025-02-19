import requests
import csv

# Fonction pour récupérer les publications et afficher les titres


def fetch_and_print_posts():
    # Effectuer une requête GET pour récupérer les posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Afficher le code de statut
    print(f"Status Code: {response.status_code}")

    # Si la requête a réussi (code 200), traiter les données JSON
    if response.status_code == 200:
        # Convertir la réponse en objet JSON
        posts = response.json()

        # Afficher le titre de chaque publication
        for post in posts:
            print(post['title'])  # Afficher le titre de la publication


# Fonction pour récupérer les publications et les sauvegarder dans un
# fichier CSV
def fetch_and_save_posts():
    # Effectuer une requête GET pour récupérer les posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Si la requête a réussi (code 200), structurer les données dans une liste
    # de dictionnaires
    if response.status_code == 200:
        # Convertir la réponse en objet JSON
        posts = response.json()

        # Ouvrir le fichier CSV en mode écriture
        with open("posts.csv", mode="w", newline='', encoding="utf-8") as file:
            # Créer un objet DictWriter pour écrire dans le CSV
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])

            # Écrire les en-têtes dans le fichier CSV
            writer.writeheader()

            # Écrire chaque publication dans le fichier CSV
            for post in posts:
                writer.writerow({"id": post["id"],
                                 "title": post["title"],
                                 "body": post["body"]})
