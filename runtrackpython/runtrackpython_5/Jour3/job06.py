"""Écrire un programme qui vérifie si un nombre renseigné par l’utilisateur est
pair. Si le nombre est pair, afficher le message “Le nombre X est pair”.
Ajouter ensuite a votre programme un message lorsque le nombre est
impair."""

print()
num= int(input("Entrez votre numéro : "))
print()
print( "Le nombre", num, "est pair" if num %2==0 else "Le nombre est impair")
print()

