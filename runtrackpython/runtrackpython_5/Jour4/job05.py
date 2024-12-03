"""Créer une fonction nommée « calcule » qui prend 3 paramètres :
➔ Le premier, « num1 », est un nombre,
➔ Le deuxième, « operator », est un caractère (string) contenant le type
d’opération(+, -, *, /, %),
➔ Le troisième, « num2 », est un nombre.
La fonction doit retourner le résultat de l’opération."""

# à revoir

def calcule():
     num1= 3
     operateur= "+"
     num2= 6
print(num1,operateur,num2, "=", num1+num2)
    
calcule()

# 2nd essai
# def calcule(num1, operateur, num2):
    # print (num1+ operateur+ num2)

# calcule(5,int("+"),9)


#3rd essai
def calcule(num1, operator,num2):
     return int(num1,operator,num2)

calcule(3+12)