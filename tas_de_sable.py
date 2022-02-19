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


########################
# constantes

#######################

#Boutons 
    #de base

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

Interrompore = tk.Button(root, text="Interrompre", fg="black", command= Interrompre_bouton)
Interrompore.grid(column=1, row=0)

Reprendre = tk.Button(root, text="Reprendre", fg="black", command= Reprendre_bouton)
Reprendre.grid(column=1, row=0)

####################
# fonctions
    #fonctions pour les integrer dans les boutons 

def Initialisation_bouton():
    pass

def Aleatoire_bouton():
    pass

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

def Interrompre_bouton():
    pass

def Reprendre_bouton():
    pass
#Faire des listes de lite 

l = [[4, 5, 2], [4, 3, 0], [1, 5, 4]]

N = 5 

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
            canvas.create_text(50, 50, text = str(grid[i][j]))
     

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width = 500)
canvas.grid(column = 0, row = 0)




initialisation()
root.mainloop()

# Presets


#########################
# partie principale

# création des widgets


# Presets
