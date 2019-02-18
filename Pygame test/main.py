# C:\\Users\\natha\\OneDrive\\Documents\\GitHub\\Python-CESI\\Pygame test\\perso.png
import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480),RESIZABLE)

#Chargement et collage du fond
fond = pygame.image.load("C:\\Users\\natha\\OneDrive\\Documents\\GitHub\\Python-CESI\\Pygame test\\hexa.png").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("C:\\Users\\natha\\OneDrive\\Documents\\GitHub\\Python-CESI\\Pygame test\\perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:    #Si "flèche bas"
                #On descend le perso
                position_perso = position_perso.move(0,3)
            if event.key == K_UP:    #Si "flèche bas"
                #On descend le perso
                position_perso = position_perso.move(0,-3)
            if event.key == K_RIGHT:    #Si "flèche bas"
                #On descend le perso
                position_perso = position_perso.move(3,0)
            if event.key == K_LEFT:    #Si "flèche bas"
                #On descend le perso
                position_perso = position_perso.move(-3,0)

    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)
    #Rafraichissement
    pygame.display.flip()