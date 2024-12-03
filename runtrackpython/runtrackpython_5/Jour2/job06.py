"""Écrire un programme qui affiche à l’aide d’une boucle de type while les
premiers résultats de la multiplication de N par 7. N étant un entier renseigné
par l’utilisateur."""

num= int(input("Veuillez entrer votre numéro entier: "))

y=0

while y <= num:
    i=7
    print(y , "x", i, "=", y*i)
    y +=1