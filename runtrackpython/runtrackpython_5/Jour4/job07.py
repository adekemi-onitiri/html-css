"""Créez une fonction qui prend en paramètre une String nommée « langage ».
Si la valeur de « langage » est égale à « JavaScript » affichez : « tu es un
développeur web »
Sinon si la valeur de « langage » est égale à « python » affichez : « tu es un
développeur IA »
_3
Sinon si la valeur de « langage » est égale à « java » affichez : « tu es un
développeur logiciel »
Sinon, si la valeur de « langage » est égale à « reactjs » affichez : « tu es un
développeur mobile »
Sinon, affichez : « un jour, je serai le meilleur développeur… »"""

print()
def langage():
    
    x=input("Entrez votre language: ")
    print()
    if x == "JavaScript":
        print("tu es un développeur web")
    
    elif x == "python":
        print("tu es un développeur IA")
    
    elif x == "java":
        print("tu es un développeur logiciel")
    
    elif x == "reactjs":
        print("tu es un développeur développeur mobile")
    
    else:
        print("un jour, je serai le meilleur développeur…")

langage()
print()