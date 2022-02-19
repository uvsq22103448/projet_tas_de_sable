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


####################
# fonctions

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
