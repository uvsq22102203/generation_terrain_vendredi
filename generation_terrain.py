###########################
# Auteur: Pierre Coucheney 
###########################

#######################
# import des librairies

import tkinter as tk
import random as rd


############################
# Définition des constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
#taille de la grille
N = 4
#choix de couleur
COUL_MUR = "grey"
COUL_VIDE = "white"

#parametre de l'automate
#
P = 0.5



terrain = []
grille = []

#######################
# fonctions

def init_terrain():
    """ Initilise le terrain de la manière suivante:
    * met à 0 la liste appelée terrain à 2D qui contient pour chaque case la 
    valeur 1 si il y a un mur, et 0 sinon
    * initialise la liste grille à 2D qui contient l'identifiant
    du carré dessiné sur le canevas pour chaque case 
    """
    
    global terrain, grille
    grille = []
    terrain = []
    canvas.delete()
    for i in range (N):
        terrain.append([0]*N)
        grille.append([0]*N)
    if rd.uniform(0,1) < P:
        terrain[0][0] = 1
    
    for i in range (N):
        for j in range(N):
            if rd.uniform(0,1) < P:
                terrain[i][j] = 1
                couleur = COUL_MUR
            else:
                couleur = COUL_VIDE
            larguer = LARGEUR // N
            hauteur = HAUTEUR // N
            x0, y0 = i * larguer, j * hauteur 
            x1 , y1 = (i + 1) * larguer, (j + 1)* hauteur
            canvas.create_rectangle((x0, y0), (x1,y1), fill = couleur)
    return terrain, grille

    print(terrain)
    

def sauvegarde():
    """ecrit la valeur N et la variable terrain 
    dans le fichier sauvegarde.txt
    """
    fic = open("sauvegarde.txt","w")
    fic.write(str(N) + "\n")
    for i in range(N):
        for j in range(N):
            fic.write(str(terrain[i][j] + "\n"))
    fic.close()


def load():
    """lit le fichier sauvegarde.txt et met a jour les variables 
    N et terrain en consequence, et modifier l'affichage
    """
    global N
    fic = open("sauvegarde.txt", "w")
    ligne = fic.readline()
    N = int(ligne)
    init_terrain()
    i = j = 0
    for ligne in fic:
        n = int(ligne)
        terrain[i][j] = n
        j += 1
        if j == N:
            j = 0
            i += 1
    fic.close()
    print(terrain)
    for i in range(N):
        for j in range(N):
            if terrain [i][j] == 1:
                coul = COUL_MUR
            else:
                coul = COUL_VIDE
            canvas.itemconfigure(grille[i][j], fill = coul)



#######################
# programme principal

# définition des widgets
racine = tk.Tk()
racine.title("Génération de terrain")
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="blue")
bouton_sauv = tk.Button(racine, text ="sauvegarde", command=sauvegarde)
bouton_load = tk.Button(racine, text="changer terrain", command=load)

# placement des widgets
canvas.grid(column=0, row=0, rowspan= 10)
bouton_sauv.grip(row=0)
bouton_load.grip(row=1)

init_terrain()

# boucle principale
racine.mainloop()