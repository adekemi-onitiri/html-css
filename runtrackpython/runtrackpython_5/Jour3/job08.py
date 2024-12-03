"""Créez un programme qui demande à l’utilisateur trois longueurs, a, b, c. À
l’aide de ces trois longueurs, déterminez s’il est possible de construire un
triangle. Déterminez ensuite si ce triangle est rectangle, isocèle, équilatéral ou
quelconque.
Attention : un triangle rectangle peut être isocèle."""


print()
a=int(input("Entrez votre première valeur: "))
b=int(input("Entrez votre deuxième valeur: "))
c=int(input("Entrez votre troisième valeur: "))

print()
if a==b and a==c and b==c:
    print("C'est un traingle")
else:
    print("Ce n'est pas un triangle")
print()