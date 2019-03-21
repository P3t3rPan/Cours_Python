# -*-coding:UTF-8 -*

import time #Import du package time pour pouvoir faire des pauses

#Typage des variables dynamique, la variable prend le type de la valeur qu'on lu iattribut, ex:
# variable = 'coucou' -> La variable sera de type string (str)
# variable = 6 -> la variable sera de type integer (int)

#Indentation = PRIMORDIALE

##################################
#Demander une valeur et l'afficher
##################################
valeur_demandee = input("Entrez une valeur : ")
#3 façons d'afficher une variable dans un print et 3 façons de définir une chaine de caractère, "blabla", 'blabla', """blabla"""
print("La valeur entrée est: "+valeur_demandee)
print('La valeur entrée est:',valeur_demandee)
print("""La valeur entrée est: {}""".format(valeur_demandee))

time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions

#La dernière syntaxe est utile quand on a plusieurs variables à afficher dans un print à l'intérieur d'un texte ex:
print("\n### Syntaxe utile quand beaucoup de variable ###")
mot1 = "variable"
mot2 = 'temps'
mot3 = """:)"""
print("Quand on a plusieurs {}, c'est plus simple d'utilise ce formatage et ça fait gagner du {}. {}".format(mot1, mot2, mot3))

time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions

#/!\RAPPEL/!\
#Si vous souhaitez afficher une variable de type int dans un print avec du texte il faut la convetir au préalable en str, ex:
print("\n### Afficher une variable int ###")
variable_int = 23
print(variable_int) #OK

time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions

#Mais avec du texte :
print("\n### Afficher une variable int dans du texte ###")
print("Ma variable int vaut: "+str(variable_int))

##################################
#Les Conditions/boucles
##################################
#3 types, if, for, while

##
#While et If:
##

time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions

print("\n### Exemple While et If ###")
ok = False #variable de type booléen

while ok == False: #tant que ok est égal à False
    nombre = input("Entrez un nombre/chiffre: ") #On demande un chiffre qui sera de type str, donc il faut convetir ce que l'on reçoit en int
    if int(nombre) < 0:
        print("Le chiffre "+nombre+" est inférieur à 0")
    elif int(nombre) > 0:
        print('Le chiffre {} est supérieur à 0'.format(nombre))
    else:
        print("Le chiffre est nul")

    continuer = input("Voulez-vous recommencer ? (O/N): ")

    if continuer == 'O' or continuer == 'o': #Si on entre O ou o on pass et la boucle while continue
        pass
    elif continuer == 'N' or continuer == 'n': #Si on entre N ou n ok devient True, donc while ok == False n'est plus vrai, on quitte la boucle.
        ok = True
        print("Bye !")
    else:
        ok = True #Pour éviter un crash du script si l'utilisateur entre autre chose, on fait comme si il souhaitait ne pas recommencer
#Il faudrait faire un deuxième while pour vérifier que la valeur entére soit bien un O ou un N.

##
#For, permet de naviguer dans une liste, une chaine string, un dictionnaire etc.
##
print("\n### Exemple For de 0 à 9 ###")
for machin in range(0, 10): #machin prend la valeur 0 puis 1 puis 2 etc jusqu'à 10 on inclu, utile si vous voulez fair une action 10 fois (Un for quoi)
    print(machin)
    time.sleep(0.5) #On fait une pause de 0.5 secs entre chaque tour de boucle

##########################
print("\n### Exemple For sur une chaine de caractère ###")
chaine = 'Hello les noobs'

for truc in chaine: #truc va prendre comme valeur chaque caractère de la variable chaine
    print(truc)
    time.sleep(0.5)
##########################
print("\n### Exemple For sur une liste ###")
liste = ["Coucou", "comment", "ça va ?"] #On défini une liste

for blabla in liste: #blabla va prendre comme valeur chaque élément de la liste
    print(blabla)
    time.sleep(0.5)



##################################
#Les listes
##################################
#permet de stocker des chiffres/mots/d'autres listes etc que vous pouvez ensuite récupérer :)

time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions

print("\n### Les listes ###")
ma_liste = [] #Définition d'une liste vide

ma_liste.append("cc") #ajout de cc à la liste, la liste ressemble désormais à : ma_liste = ["cc"]
ma_liste.append("blabla") #ajout de blabla à la liste, la liste ressemble désormais à : ma_liste = ["cc", "blabla"]
ma_liste.append("cool") #ajout de cool à la liste, la liste ressemble désormais à : ma_liste = ["cc", "blabla", "cool"]
print(ma_liste)

time.sleep(2) #On fait une pause de 2 secs avant la suite des instructions
print("Le premeir élément est: "+ma_liste[0])
del ma_liste[0] #On retire le premeir élément de la liste, ma_liste = ["blabla", "cool"]
ma_liste.remove("cool") #On  retire de la liste "cool", ma_liste = ["blabla"]
print(ma_liste)

#D'autres choses possibles sur les listes, chaines de caractères etc : http://apprendre-python.com/page-apprendre-listes-list-tableaux-tableaux-liste-array-python-cours-debutant
os.system("pause")