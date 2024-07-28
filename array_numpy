import numpy as np 

liste = [1800, 1500, 2200, 3000, 2172, 5000, 1400, 1200, 1100, 1300]

#création d'un array numpy à partir de la liste liste

revenus =  np.array(liste)
print(revenus)

#sélectionn de  l'ensemble des revenus supérieurs ou égal à 3000€ :

haut_revenus  = revenus[revenus > 3000]

print(haut_revenus)


""" 
calculez dans un premier temps la somme des revenus annuelle. Pour rappel, les revenus listés ci dessus sont mensuels.
calculez ensuite la moyenne des revenus des 10 clients 
"""
somme = revenus.sum() * 12

print("la somme des revenus annuelle est :", somme)

moyenne = revenus.mean() * 12

print("la moyenne des revenus annuelle est :", moyenne)

# faire une augmentation de 200£ sur le salaire mensuels du client qui gagnait 1400£

augmentation = revenus[revenus == 1400] = 1600

print("le nouveau salarie est :", augmentation)