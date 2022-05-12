###############################
#####                     #####
#####  Projet Transverse  #####
#####      Groupe E5      #####
#####                     #####
###############################

######## IMPORTS #########

# import Screen
# from Object.Menu import Menu

####### MAIN MENU ########

# Menu().Display().main()

# début de structure de menu (martin)
import pygame
from nouvellepartie import *
from lesregles import lesregles
from credits import credits





# Initialiaser pygame
pygame.init()

# Crée la fenêtre
screen = pygame.display.set_mode((1280, 720))

# Fond du menu
background = pygame.image.load("assets/FONDS_V2.PNG")

# Titre et icone
pygame.display.set_caption("Blobs Battle")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

fleche = pygame.image.load("assets/fleche.xcf")
selection_x = 550
selection_y = 240

limite = 1

def selection_menu(x,y):
    screen.blit(fleche, (x, y))

running = True

while running:
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Si la touche est préssée verifier si c'est à gauche ou à droite
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:


                if limite == 2:
                    limite-=1
                    selection_y = 138


                elif limite == 3:
                    limite-=1
                    selection_y = 240



            if event.key == pygame.K_DOWN:

                if limite == 1:
                    limite+=1
                    selection_y = 240


                elif limite == 2:
                    limite+=1
                    selection_y = 340

            if event.key == pygame.K_RETURN:
                if limite ==1:
                    background = lancer()
                elif limite==2:
                    background = lesregles()
                elif limite==3:
                    background = credits()



    selection_menu(selection_x,selection_y)
    pygame.display.update()
