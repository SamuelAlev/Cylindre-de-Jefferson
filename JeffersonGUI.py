"""
    Project name: Cylindre de Jefferson
    Copyright,
    ALEV Samuel (226430@supinfo.com)
    STOCKMAN Jim (227078@supinfo.com)
    (C) 2016 - 2017
    This script was tested with Python 3.6.0 and PyGame 1.9.2b1
"""
import pygame
from JeffersonShell import *

pygame.init()
pygame.font.init()

# Vars init
cylinder = loadCylinder("cylinderWiki.txt")

# Titre de la fenêtre
pygame.display.set_caption("Cylindre de Jefferson")

# Var avec la clock du jeu
clock = pygame.time.Clock()
FPS = 60

# Vars font
roboto = pygame.font.Font("fonts/Roboto.ttf", 18)

# Var hauteur et largeur de la fenêtre
display_width = 300 + 30*len(cylinder)
display_height = 900

surface = pygame.display.set_mode((display_width, display_height), 0, 32)

# Background de la fenêtre
surface.fill((255, 251, 234))

mpos = pygame.mouse.get_pos()

# Boucle pour la surface
running = True

def displayCylinder(mySurface,cylinder,i):
    for j in range(len(cylinder[i])):
        text = roboto.render(cylinder[i][j], True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = (0+(30*i),30+25*j)
        mySurface.blit(text, textRect)


def displayCylinders(mySurface,cylinder):
    for i in range(len(cylinder)):
        displayCylinder(mySurface, cylinder, i+1)


def enterKey(mySurface,n):
    clickedItems = []
    for j in range(n):
        text = roboto.render(str(j), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = (31.5+(29.9*j),710)
        mySurface.blit(text, textRect)
    # Reste à détecter les clics sur les chiffres et ajouter à "clickedItems"
    # Et également à afficher la 2ème ligne avec les chiffres qui sont inclus dans "clickedItems"


def rotateCylinder(cylinder,i,up):
    pass


def rotateCylinders(mySurface,cylinder):
    pass


def displayAll():
    while running:
        mpos = pygame.mouse.get_pos()
        surface.fill((255, 251, 234))
        # Permet de gérer les events
        for event in pygame.event.get():
            # Ajoute une action au bouton fermer
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        displayCylinders(surface, cylinder)
        enterKey(surface, len(cylinder))
        pygame.display.update()
        clock.tick(FPS)

displayAll()
