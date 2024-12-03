"""Créer une fonction nommée « time_to_text » qui prend en paramètre un «
nombre entier » de minutes et « affiche en console » une chaine de caractère
sous la forme de : « X heures et Y minutes »."""

print()
def time_to_text():
    num = int(input("Entrez votre nombre: "))
    x = int(num/60)
    y = num%60
    print()
    print(x,"heures",y,"minutes")

time_to_text()
print()