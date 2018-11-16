# -*-coding:UTF-8 -*

##################################
#Les package
##################################

#Pour importer un package il suffit d'utiliser le mot clé "import" suivi du nom du package
#Si vous n'utilisez qu'une fonction du package il est préférable de l'importer plutot que d'importer tout le package, ex:
from os import system #importe uniquement la fonction system contenue dans os
import os #importe toutes les fonctions contenues dans os

import time #Import du package time pour pouvoir faire des pauses


##################################
#Les tuples
##################################

#Un tuple est une liste qui ne peut plus être modifiée, exemple de définition d'un tuple:
mon_tuple = (0, 6, 9)

#Comme pour les listes vous pouvez accdéder à la première valeur du tuple comme ceci:
premiere_valeur = mon_tuple[0]

#Le tuple permet de faire des affectations multiples :
variable1, variable2 = 11, 22

#Permet aussi de renvoyer plusieurs valeurs lors d'un appel de fonction:
def mafonction():
    return "coucou", "cmoi"




print("\n### Exemple renvoie plusieurs valeurs lors d'un appel de fonction ###")

result = mafonction()
print("La variable result est de type: "+str(type(result))) #type() retourne le type de la variable, str() converti la variable en String
time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions


##################################
#Les Dictionnaires
##################################

#Un dictionnaire est une sorte de liste qui n'utilise pas les indexs comme les tuples
#et les listes mais des clés, on peut y stocker des objets (listes, tuple, d'autres dictionnaires etc)
#exemple de définition d'un dictionnaire:

liste_hobbies_jason = ["Boire", "Boire", "Modération"]

mon_dictionnaire = {"Nom": "Jason",
                    "Age": 10,
                    "QI": 200,
                    "Hobbies": liste_hobbies_jason
                    }

#Pour récupérer la valeur contenue dans "Age" :
la_valeur = mon_dictionnaire["Age"]

#Comme les listes et les tuples vous pouvez naviguer dans les dictionnaires via une boucle for
#Pour récupérer les valeurs du dictionnaire :
print("\n### Affichage des valeurs du dictionnaire ###")
for valeurs_dictionnaire in mon_dictionnaire.values(): #utilisation de la méthode .values() pour préciser que l'on souhaite récupérer les valeurs
    print(valeurs_dictionnaire)

time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions

#De la même manière pour récupérer les clés:
print("\n### Affichage des clés du dictionnaire ###")
for cles_dictionnaire in mon_dictionnaire.keys(): #utilisation de la méthode .keys() pour préciser que l'on récupère les clés
    print(cles_dictionnaire)

time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions

#On peut également récupérer le couple clé/valeur:
print("\n### Affichage des couples clés/valeurs du dictionnaire sous forme de tuple ###")
for couple_cles_valeurs in mon_dictionnaire.items(): #ici on récupère le couple clé/valeur sous forme de tuple
    print(couple_cles_valeurs)
    print("\ncouple_cles_valeurs est de type: "+str(type(couple_cles_valeurs)))

time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions

print("\n### Affichage des clés/valeurs du dictionnaire dans deux variables distinctes ###")
for cles_dict, valeurs_dict in mon_dictionnaire.items(): #ici on récupère le couple clé/valeur dans deux variables distinctes
    print("Clé: "+cles_dict+" Valeur: "+str(valeurs_dict))
    print("\ncles_dict et valeurs_dict sont du type {} et {} ".format(str(type(cles_dict)), str(type(valeurs_dict))))

time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions

#Pour ajouter un élément à un dictionnaire:
mon_dictionnaire["La_Nouvelle_cle"] = "La nouvelle valeur"


#D'autres trucs cools à savoir sur les dictionnaires: http://apprendre-python.com/page-apprendre-dictionnaire-python


##################################
#Les Fonctions
##################################

#Une fonction est un morceau de code que l'on va utiliser plusieurs fois, plutot que de le réécrire on défini ce code
#dans une fonction et on l'appelle dès que nécessaire, si la fonction ne retounr rien (genre si elle fait juste un print) on appelle ça une procédure
#définition d'une fonction (Ne pas oublier l'indentation, c'est ce qui délimite):

def fonction1(variable1, variable2):
    ok = variable1 + variable2
    return ok


a = 5
b = 8

print("\n### Calcul a+b via fonction ###")
result = fonction1(a, b) #On envoie les valeurs de a et de b dans la fonction1(), variable1 vaut la valeur de a et variable2 la valeur de b, puis on return le résultat ok
#que l'on récupère dans la variable result
print("Le résultat est: "+str(result))

#On peut également envoyer des listes/dicitonnaires/tuples dans la fonction, on peut définir des valeurs par défauts, récupérer un nombre de variables indéfinis etc
#Plus d'infos: http://apprendre-python.com/page-apprendre-creer-fonction-en-python

os.system("pause")
