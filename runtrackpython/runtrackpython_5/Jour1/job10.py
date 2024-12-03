"""Créez un programme permettant la simulation financière pour un
investissement. Initialiser deux variables, une pour le montant initial de
l’investissement et une pour le taux de rendement annuel en pourcentage.
_4
Affichez en console le gain annuel en fonction du taux de rendement.
L’investisseur augmente son capital de 5 000 euros, le taux augmente alors
de 2%.
Calculez à nouveau le gain de l’investisseur et affichez en console le résultat.
L’investisseur retire 10% du montant total, suite à ce retrait, le rendement
diminue de 1%. Calculez le montant final de l’investissement et affichez le
nouveau gain."""

print()
# gain annuel en fonction du rendement
montant_initial= 10000
taux1= 0.05
gain1= montant_initial*taux1
print("Le gain annuel en fonction du taux de rendement est de : ", gain1)
print()

# l'augmentation du capital
capital= 5000
taux2= 0.02
gain2= capital*taux2
print("Le gain de l'investisseur est de: ", gain2)
print()

# montant final
montant_total= (montant_initial+gain1)+(capital+gain2)
taux3= 0.01
retrait= montant_total*taux3
montant_final = montant_total - retrait
print(montant_final)
print()