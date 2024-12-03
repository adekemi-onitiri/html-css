

print()

def choix(type,saison):

    if type=="fruits" and saison=="hiver":
        print("orange, mandarine et kiwi", "sont des",type, "en", saison,".")
   
    elif type=="fruits" and saison=="été":
        print("poire, fraise, cassis", "sont des",type, "en", saison,".")
    
    elif type=="légumes" and saison=="hiver":
        print("carotte, topinambour, endive", "sont des",type, "en", saison,".")
    
    elif type=="légumes" and saison=="été":
        print("artichaut, aubergine,navet",  "sont des",type, "en", saison,".")
    
    else:
        print("Essayer à nouveau")
    print()
   
choix("fruits","hiver")

print()





