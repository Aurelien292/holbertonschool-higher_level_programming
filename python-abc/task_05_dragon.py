# Mixin SwimMixin qui ajoute la capacité de nager
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Mixin FlyMixin qui ajoute la capacité de voler
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Classe Dragon qui hérite de SwimMixin et FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Test de la classe Dragon
draco = Dragon()

# Le dragon peut nager, voler et rugir
draco.swim()   # Affiche "The creature swims!"
draco.fly()    # Affiche "The creature flies!"
draco.roar()   # Affiche "The dragon roars!"