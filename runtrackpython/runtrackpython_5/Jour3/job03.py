"""Créez un programme qui affiche dans le terminal tous les nombres de 0 à 100 compris SAUF 26, 37, 88."""


# pourquoi ca ne marche pas, je voulais écrire moin de code
"""for x in range(101):
    a,b,c= 26,37,88
    z= a,b,c
    if x == z:
        continue
    print(x)"""

for x in range (101):
    if x == 26:
        continue
    if x == 37:
        continue
    if x == 88:
        continue
    print(x)