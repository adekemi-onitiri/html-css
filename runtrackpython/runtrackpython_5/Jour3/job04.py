"""Écrire un programme qui itère les nombres entiers de 1 à 100.
Pour les multiples de trois, affichez « Fizz » au lieu du nombre
et pour les multiples de cinq, affichez « Buzz ». Pour les
nombres qui sont des multiples de trois et de cinq, affichez «
FizzBuzz »."""


# c'est presque ca
"""for x in range (1,101):
    print(x)

    if x %3==0:
     print("Fizz")

    elif x %5==0:
        print("Buzz")
    
    elif x %5*3==0:
     print("FizzBuzz")"""

# celci n'affiche pas et n'indique aucune erreur
num1= 3
num2= 5
num3= num1*num2

x=0

while x >=1 and x<=100:
    for x in range (1,100): 
        x +=1
        if x == num1:
            print("Fizz")
        elif x == num2: #est ce que je peux utiliser le pas avec index?
            print("Buzz")
        elif x == num3:
            print("FizzBuzz")