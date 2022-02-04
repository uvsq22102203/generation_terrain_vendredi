###########################
# Auteur: Pierre Coucheney 
###########################

#######################
# import des librairies

import tkinter as tk


############################
# Définition des constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600




#######################
# fonctions

def init_terrain():
    """ Initilise le terrain de la manière suivante:
    * met à 0 la liste appelée terrain à 2D qui contient pour chaque case la 
    valeur 1 si il y a un mur, et 0 sinon
    * initialise la liste grille à 2D qui contient l'identifiant
    du carré dessiné sur le canevas pour chaque case 
    """
    pass


#######################
# programme principal

# définition des widgets
racine = tk.Tk()
racine.title("Génération de terrain")
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="blue")

# placement des widgets
canvas.grid(column=0, row=0)

init_terrain()

# boucle principale
racine.mainloop()