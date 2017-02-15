"""
    Project name: Cylindre de Jefferson
    Copyright,
    ALEV Samuel (226430@supinfo.com)
    STOCKMAN Jim (227078@supinfo.com)
    (C) 2016 - 2017
    This script was tested with Python 3.6.0 and PyGame 1.9.2b1
"""
import pygame

def displayCylinder(mySurface,cylinder,i):
    pass


def displayCylinders(mySurface,cylinder):
    pass


def enterKey(mySurface,n):
    pass


def rotateCylinder(cylinder,i,up):
    pass


def rotateCylinders(mySurface,cylinder):
    pass


def displayAll():
    pygame.init()
    pygame.font.init()

    # Titre de la fenêtre
    pygame.display.set_caption("Cylindre de Jefferson")

    # Vars font
    roboto = pygame.font.Font("fonts/Roboto.ttf", 30)

    # Var avec la clock du jeu
    clock = pygame.time.Clock()
    FPS = 60

    # On va l'init avec loadCylinder() après
    disques = {1: 'TEST', 2: 'TEST',3: 'TEST', 4: 'TEST', 5:'TEST', 6: 'TEST',7: 'TEST', 8: 'TEST'}

    # Var hauteur et largeur de la fenêtre
    display_width = 100 * len(disques)
    display_height = 900

    surface = pygame.display.set_mode((display_width, display_height), 0, 32)

    # Background de la fenêtre
    surface.fill((255, 251, 234))

    while True:
        pygame.display.update()
        clock.tick(FPS)

displayAll()
