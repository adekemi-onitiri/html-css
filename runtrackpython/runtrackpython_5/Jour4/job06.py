"""Créer une fonction qui prend en paramètre un nombre nommé « nombre ».
Afficher « positif » si le nombre est supérieur à 0.
Afficher « négatif » si le nombre est inférieur à 0.
Appeler cette fonction plusieurs fois en y passant des paramètres différents
pour afficher ces résultats."""

print()
def nombre():
    x=int(input("Veuillez entrez votre numéro: "))
    print()
    print("positif" if x >=1 else "négatif")
    
nombre()
print()