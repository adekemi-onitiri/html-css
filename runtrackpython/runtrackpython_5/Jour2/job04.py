"""Créez un programme qui affiche dans le
terminal les tables de multiplications de 1 à
N. N étant un entier supérieur à zéro saisi par
l’utilisateur."""

print()
n=int(input("Entrez un entier supérieur à zéro: "))

for y in range (n+1):
    print()
    print("Table de multiplication de :", y)
    
    for i in range (11):
        print(n, "x", i, "=", n*i )
    print()
print()