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

HEIGHT = 100
WIDTH = 200
l=WIDTH/8
h=HEIGHT/8

####################
# fonctions


# Presets


#########################
# partie principale

# création des widgets

list=[[],[],[],[],[],[],[],[],[],[]]
racine = tk.Tk()
for i in range (8):
    for j in range (8):
        list[i].append(tk.Button(racine,padx=l,pady=h ))
        list[i][j].grid(column=i, row=j)


racine.mainloop()

# Presets
