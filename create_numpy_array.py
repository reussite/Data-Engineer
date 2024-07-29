import numpy as np

"""
Pour cette seconde tâche, nous travaillons toujours sur les mêmes 10 clients, mais nous avons cette fois trois informations à disposition sur chacun d’eux :

    le revenu mensuel
    l'âge du client
    le nombre d’enfants à charge

L’objectif va être de créer un tableau NumPy à partir de ces informations et de répondre aux différentes demandes formulées par notre service prêt en manipulant ce tableau avec les différentes techniques présentées tout au long de ce chapitre.
"""
hugo = [1800, 21, 0]
richard = [1500, 54, 2]
emilie = [2200, 28, 3]
pierre = [3000, 37, 1]
paul = [2172, 37, 2]
deborah = [5000, 32, 0]
yohann = [1400, 23, 0]
anne = [1200, 25, 1]
thibault = [1100, 19, 0]
emmanuel = [1300, 31, 2]

tableau = [hugo, richard, emilie, pierre, paul, deborah,
           yohann, anne, thibault, emmanuel]

# création d'une array numpy

data  = np.array(tableau)

print(" la liste convertie en array numpy est :", data)

#affichage des informations sur Paul

paul_info = data[4, :]
print("Les informations sur Paul sont :", paul_info)

""" calculons ses mensualités maximale , en sachant que le taux d'endettement maximum est de 35% (il ne pourra donc pas rembourser par mois plus de 35% de son revenu). """

mensulalite_maximal = round(data[4,0]*0.35, 2)

print("Ses mensualités maximales sont de :", mensulalite_maximal ,"€")

#Ajout d'un nouveau client à la l'array : louise = [1900, 31, 1]

louise = [1900, 31, 1]

data  = np.vstack((data, louise))

print(data)

#Stockage de l'ensemble des informations de salaire de notre clientèle dans une variable revenus :

revenus = data[:, 0]

print("Les revenus sont :", revenus)