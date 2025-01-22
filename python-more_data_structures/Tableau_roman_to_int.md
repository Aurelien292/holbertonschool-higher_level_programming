# Tableau Blanc - Conversion des Nombres Romains

1. ## Exemples de symboles romains et leurs valeurs :
| Symbole | Valeur |
|---------|--------|
| I       | 1      |
| V       | 5      |
| X       | 10     |
| L       | 50     |
| C       | 100    |
| D       | 500    |
| M       | 1000   |

3. ## Règles :
   - Si le symbole suivant est plus grand => soustraction.
   - Sinon => addition.

4. ## Plan de la solution :
   - Vérifier si l'entrée est une chaîne valide.
   - Initialiser un total à 0.
   - Parcourir la chaîne :
     - Si le suivant est plus grand, soustraire.
     - Sinon, ajouter.
   - Retourner le total.

5. ## Retourner le total final !