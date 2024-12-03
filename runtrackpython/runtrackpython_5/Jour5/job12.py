"""Écrire un programme qui trie dans l’ordre croissant une liste passée en
paramètre.
SANS UTILISER DE FONCTION SYSTÈME (len, sort, round…..)"""

print()

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

for x in L:
    print (int((x < x+1))) # comment convertir le bool en int


print()