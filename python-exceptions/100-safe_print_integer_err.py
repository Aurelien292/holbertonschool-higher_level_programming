import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))  # Essaie d'imprimer l'entier
        return True  # Si ça fonctionne, retourne True
    except (ValueError, TypeError) as e:  # Si une exception est levée, c'est probablement une erreur de type
        print(f"Exception: {e}", file=sys.stderr)  # Affiche l'erreur dans stderr
        return False  # Retourne False si une erreur se produit
