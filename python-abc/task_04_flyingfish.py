class Fish:
    def swim(self):
        print("The fish is swimming")
    
    def habitat(self):
        print("The fish lives in water")

# Classe Bird
class Bird:
    def fly(self):
        print("The bird is flying")
    
    def habitat(self):
        print("The bird lives in the sky")

# Classe FlyingFish qui hérite de Fish et Bird
class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")
    
    def swim(self):
        print("The flying fish is swimming!")
    
    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Test de la classe FlyingFish
flying_fish = FlyingFish()
flying_fish.fly()      # Affiche "The flying fish is soaring!"
flying_fish.swim()     # Affiche "The flying fish is swimming!"
flying_fish.habitat()  # Affiche "The flying fish lives both in water and the sky!"

# Vérification de l'ordre de résolution des méthodes (MRO)
print(FlyingFish.mro())  # Affiche l'ordre de résolution des méthodes
