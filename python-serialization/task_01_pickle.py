#!/usr/bin/python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet avec un format lisible"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Sérialise l'objet courant et le sauvegarde dans un fichier"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized to {filename}")
        except Exception as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Charge un objet sérialisé depuis un fichier et le renvoie"""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error during deserialization: {e}")
            return None

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un objet CustomObject
    person = CustomObject("John", 25, True)
    
    # Affichage des attributs de l'objet
    person.display()
    
    # Sérialisation de l'objet dans un fichier
    person.serialize("person.pkl")
    
    # Désérialisation de l'objet depuis le fichier
    loaded_person = CustomObject.deserialize("person.pkl")
    
    # Si la désérialisation a réussi, on affiche les attributs de l'objet chargé
    if loaded_person:
        loaded_person.display()
