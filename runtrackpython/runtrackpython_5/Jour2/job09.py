"""Uniquement à l’aide d’une boucle, afficher les nombres pairs et impairs de 1 à 30."""


"""# ma logique: ça affiche en boolean car j'ai utilisé les operateurs conditionels pour les nombres pair et impaire. Quand je mets un int devant ça affiche des nombres binaire. Quoi dois-je faire sans utiliser les structures conditionnelles? 
print()
print("Nombre pairs")
for x in range (1,30):
    print(x %2==0)

print()
print("Nombre impairs")
for x in range (1,30):   
    print(x %2!=0)
    print()


# la logiqique qprès avoir vu la logique pour les nombres premières: toujours des booleans
print()
print("Nombre pairs")
for x in range (1,30):
    print(30 %x==2)

print()
print("Nombre impairs")
for x in range (1,30):   
    print(30 %x!=2)
    print()

# aveve la boucle while cela affiche aussi en boolean; j'ai essayé la conversion en int et la réponse est faux 
print()
while x<=30 and x%2==0:
    print (int(x))
    x +=1"""

print()
# une idée de base
print("nombre pairs:")
for x in range (1,30,2):
    print (x+1)
print()   
print("nombre impairs:")
for x in range (1,30,2):
    print(x)