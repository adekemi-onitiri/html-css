"""Créer une fonction qui vérifie que le nombre est pair ou impair. Pensez à
vérifier si le nombre est bien un chiffre entier et positif.
Appeler cette fonction plusieurs fois avec des valeurs différentes."""

print()
def num(pair):
    
   print("C'est un chiffre pair!" if int(pair %2==0 and pair >0) else "C'est un chiffre impair!")
   return pair

num(15)

print()