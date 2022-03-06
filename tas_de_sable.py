########################
# MITD-03
# Frédéric Li Combeau
# Lisa Vauvert
# Victor Combemorel
# Manel Mokrab
# https://github.com/uvsq-info/l1-python
########################

# import des librairies

import tkinter as tk
import random as rd
import os


########################

# constantes

HEIGHT = 600
WIDTH = 600
N = 5

########################

# fonctions

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width = 500)

def init_affichage(grille):
    global HAUTEUR, LARGEUR, N
    couleurs = ["green", "yellow", "goldenrod1", "orange2", "chocolate1", "red", "red3", "darkred"]    
    hauteur_case = HAUTEUR // N
    largeur_case = LARGEUR // N
    color = "gray"

    for i in range(len(grille)):
        for j in range(len(grille[i])):

            if grille[i][j] == 0:
                color = couleurs[0]
            elif grille[i][j] == 1:
                color = couleurs[1]
            elif grille[i][j] == 2:
                color = couleurs[2]
            elif grille[i][j] == 3:
                color = couleurs[3]
            elif grille[i][j] == 4:
                color = couleurs[4]
            elif grille[i][j] == 5:
                color = couleurs[5]
            elif grille[i][j] == 6:
                color = couleurs[6]
            elif grille[i][j] == '#':
                color="gray"
            else:
                color = couleurs[7]


            canvas.create_rectangle((j * largeur_case), (i * hauteur_case), (j * largeur_case + largeur_case), (i * hauteur_case + hauteur_case), fill=color)
            canvas.create_text(((j * largeur_case) + (largeur_case // 2)), ((i * hauteur_case) + (hauteur_case // 2)), text=str(grille[i][j]))

def initialisation():
    grid = []
    
    for i in range(N-2):
        grid.append(["#"])
        for j in range(N-2):
            grid[i].append(0)
        grid[i].append("#")
    grid.insert(0, ["#"]*N)
    grid.append(["#"]*N)

    return affichage(grid)

def affichage(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            canvas.create_text(15*j, 15*i, text = str(grid[i][j]), anchor="nw")

def Initialisation_bouton():
    pass

def Aleatoire_bouton():
    pass

#creation d'un fichier txt 
def fichier():
    f = open("saves.txt","w")

def Sauvegarder_bouton():
    pass

def Charge_bouton():
    pass

def Additionner_bouton():
    pass

def Soustraire_bouton():
    pass

def Stabiliser_bouton():
    pass
    #Je ne peux rien mettre sinon ça marque qu'il y a un problème
            

def Interrompre_bouton():
    pass
 

def Reprendre_bouton():
    pass

# fonctions presets

def Random_bouton():
    pass

def Pile_centree_bouton():
    pass

def Max_stable_bouton():
    pass

def Double_max_stable_bouton():
    pass

def Indentify_bouton():
    pass

# bouton pour aller plus loin faits par Manel

def Edition_bouton():
    pass

def Taille_bouton():
    pass


########################

# affichage


root = tk.Tk()

canvas = tk.Canvas(root, height=500, width = 500)
canvas.grid(column = 0, row = 0)

Initialisation = tk.Button(root, text="Initialisation", fg="black", command= Initialisation_bouton)
Initialisation.grid(column=1, row=0)

Aleatoire = tk.Button(root, text="Aleatoire", fg="black", command= Aleatoire_bouton)
Aleatoire.grid(column=1, row=0)

Sauvegarder = tk.Button(root, text="Sauvergarder", fg="black", command= Sauvegarder_bouton)
Sauvegarder.grid(column=1, row=0)

Charge = tk.Button(root, text="Charge", fg="black", command= Charge_bouton)
Charge.grid(column=1, row=0)

Additionner = tk.Button(root, text="Additionner", fg="black", command= Additionner_bouton)
Additionner.grid(column=1, row=0)

Soustraire = tk.Button(root, text="Soustraire", fg="black", command= Soustraire_bouton)
Soustraire.grid(column=1, row=0)

Stabiliser = tk.Button(root, text="Stabiliser", fg="black", command= Stabiliser_bouton)
Stabiliser.grid(column=1, row=0)

Interrompre = tk.Button(root, text="Interrompre", fg="black", command=Interrompre_bouton)
Interrompre.grid(column=1, row=0)

Reprendre = tk.Button(root, text="Reprendre", fg="black", command= Reprendre_bouton)
Reprendre.grid(column=1, row=0)

# boutons presets 

Random = tk.Button(root, text="Random", fg="black", command= Random_bouton)
Random.grid(column = 1, row = 1)

Pile_centree = tk.Button(root, text="pile centrée", fg="black", command= Pile_centree_bouton)
Pile_centree.grid(column = 1, row = 1)

Max_stable = tk.Button(root, text="Max stable", fg="black", command= Max_stable_bouton)
Max_stable.grid(column = 1, row = 1)

Double_max_stable = tk.Button(root, text="Double max stable", fg="black", command= Double_max_stable_bouton)
Double_max_stable.grid(column = 1, row = 1)

Identify = tk.Button(root, text="Identity", fg="black", command= Indentify_bouton)
Identify.grid(column = 1, row = 1)

# boutons édition

Edition= tk.Button(root, text="Edition", fg="red", command=Edition_bouton)
Edition.grid(column=1, row=0)

Taille= tk.Button(root, text="Taille", fg="red", command=Taille_bouton)
Taille.grid(column=1, row=0)


initialisation()
root.mainloop()
