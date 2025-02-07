class CountedIterator:
    def __init__(self, iterable):
        # Initialisation de l'itérateur et du compteur
        self.iterator = iter(iterable)  
        # Crée un itérateur à partir de l'itérable passé
        self.count = 0  # Initialisation du compteur
    
    def __next__(self):
        try:
            # Récupérer l'élément suivant
            item = next(self.iterator)
            self.count += 1  # Incrémenter le compteur
            return item  # Retourner l'élément
        except StopIteration:
            # Si l'itérateur est épuisé, lever l'exception StopIteration
            raise StopIteration
    
    def get_count(self):
        # Retourner le nombre d'éléments parcourus
        return self.count
