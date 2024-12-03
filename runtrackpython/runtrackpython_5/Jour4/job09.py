"""Demandez à l'utilisateur de saisir trois notes, puis enregistrez le résultat de la
fonction « moyenne » dans une variable appelée « moyenne_etudiant ».
Afficher ensuite la phrase suivante en fonction de la moyenne de l’étudiant :
➔ Très bon élève si la moyenne est comprise entre 20 et 15.
➔ Bon élève si la moyenne est comprise entre 14 et 11.
➔ Élève moyen si la moyenne est comprise entre 10 et 8.
➔ Élève devant faire des efforts si la moyenne est comprise entre 0 et 7."""

print()
def moyenne():
    note1= int(input("Tapez votre 1ère note en nombre entier: "))
    note2= int(input("Tapez votre 2ème note en nombre entier: "))
    note3= int(input("Tapez votre 3ème note en nombre entier: "))

    moyenne_étudiant= (note1 + note2 + note3)/3
    print()
    if moyenne_étudiant >=15 and moyenne_étudiant<=20:
        print("Très bon élève")
    
    elif moyenne_étudiant >=11 and moyenne_étudiant<=14:
        print("Bon élève")
    
    elif moyenne_étudiant >=8 and moyenne_étudiant<=10:
        print("Elève moyen")
    
    else:
        print("Elève dvant faire des efforts")
    
moyenne()

print()