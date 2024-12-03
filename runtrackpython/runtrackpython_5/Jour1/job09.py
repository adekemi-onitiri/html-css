"""Créez un programme permettant la gestion d’un inventaire.
Créez des variables représentant un produit (nom, prix unitaire, quantité en
stock). Affichez en console les informations du produit de manière formatée.
Ajoutez des produits en stock. Demandez à l’utilisateur de saisir la quantité de
produits qu’il souhaite acheter et mettre le stock à jour.
Le prix d’un produit a subi l’inflation et a augmenté de 10%. Mettre à jour la
variable correspondante.
Affichez à nouveau toutes les informations sur le produit."""

print()
# variables représantant du produit
nom= "Pain"
prix_unitaire= 2.50
quantité= 10

# informations du produit de manière formatée
produit= f"{nom},{prix_unitaire}, {quantité}"

print(produit)

# ajoute du produits en stock
quantité2= 20

print()
# le prix du produit augment de 10%
nouveau_prix= prix_unitaire*1.1
print( "Produit =", nom)
print("Quantité =", quantité + quantité2)
print("Nouveau prix =", nouveau_prix)
print()


