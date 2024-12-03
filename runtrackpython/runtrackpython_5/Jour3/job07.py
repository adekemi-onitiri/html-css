"""À partir de la chaîne «
abcdefghijklmnopqrstuvwxyz » * 10, écrivez un
programme qui récupère et affiche autant de
caractères que possible de cette chaîne sous
forme de suite pyramidale."""

#ma logique : il me manque quelque chose
alphabet= "abcdefghijklmnopqrstuvwxyz"

for x in range (10):
    for y in alphabet:
        x+=1
        print(y, end="")


# ça ne marche pas--- source: https://pynative.com/print-pattern-python-examples/#h-alphabets-and-letters-pattern
"""ascii_number = 97
rows= 10

for x in range (0, rows):
    for y in range(0, x+1):
        alphabet=chr(ascii_number)
        print(alphabet, end=" ")
        ascii_number += 1"""

