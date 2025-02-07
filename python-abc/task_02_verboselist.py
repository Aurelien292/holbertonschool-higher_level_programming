#!/usr/bin/python3
class VerboseList(list):
    def append(self, item):
        print(f"Added {item} to the list.")
        super().append(item)  # Appel de la méthode append de la classe list
    
    def extend(self, iterable):
        print(f"Extended the list with {len(iterable)} items.")
        super().extend(iterable)  # Appel de la méthode extend de la classe list
    
    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)  # Appel de la méthode remove de la classe list
    
    def pop(self, index=-1):
        # Si un index est spécifié, le message indiquera cet index
        item = super().pop(index)  # Appel de la méthode pop de la classe list
        print(f"Popped {item} from the list.")
        return item  # Retourne l'élément poppé
