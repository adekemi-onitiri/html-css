"""Écrire un programme qui calcule la somme de toutes les valeurs paires de la
liste : L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]."""


print()

L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

del L[2]
del L[5:7]
del L[-1]

print(sum(L))

print