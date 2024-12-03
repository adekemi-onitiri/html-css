"""Initialiser une variable contenant un chiffre entier représentant l’age d’une
personne. Si la personne au moins 18 ans afficher “Tu peux voter” “Tu ne peux
pas voter”."""


print()
age= int(input("Quelle est votre âge? "))

print()
vote= "Tu peux voter" if age >= 18 else "Tu ne peux pas voter"

print (vote)
print()