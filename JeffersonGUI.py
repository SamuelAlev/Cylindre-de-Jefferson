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
clickedItems = []
click = 0
row = 0
finished = False

# Titre de la fenêtre
pygame.display.set_caption("Cylindre de Jefferson")

# Var avec la clock du jeu
clock = pygame.time.Clock()
FPS = 60

# Vars font
roboto = pygame.font.Font("fonts/Roboto.ttf", 18)
arial = pygame.font.SysFont("Arial", 48)

# Var hauteur et largeur de la fenêtre
display_width = 300 + 30*len(cylinder)
display_height = 900

surface = pygame.display.set_mode((display_width, display_height), 0, 32)

# Boucle pour la surface
running = True

def displayCylinder(mySurface,cylinder,i):
    for j in range(len(cylinder[i])):
        text = roboto.render(cylinder[i][j], True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = (0 + (30 * row), 30 + 25 * j)
        mySurface.blit(text, textRect)


def displayCylinders(mySurface,cylinder):
    global row

    if len(clickedItems) != len(cylinder):
        for i in range(1, (len(cylinder) + 1)):
            row += 1
            displayCylinder(mySurface, cylinder, i)
    else:
        for i in clickedItems:
            row += 1
            displayCylinder(mySurface, cylinder, i)


def enterKey(mySurface,n):
    global clickedItems

    mpos = pygame.mouse.get_pos()

    if not len(clickedItems) == n:
        # Génère les clés et les affiche
        for j in range(1,n+1):
            if j in clickedItems:
                text = roboto.render(str(j), True, (255, 0, 0))
            else:
                text = roboto.render(str(j), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.topleft = (31.5+(29.9*(j-1)),710)
            mySurface.blit(text, textRect)
            if textRect.collidepoint(mpos):
                if pygame.mouse.get_pressed()[0]:
                    if not j in clickedItems:
                        clickedItems.append(j)

        # Affiche les clés sur lesquelles on a cliqué
        for i in range(len(clickedItems)):
            text = roboto.render(str(clickedItems[i]), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.topleft = (31.5 + (29.9 * i), 750)
            mySurface.blit(text, textRect)

    # Retourne la liste une fois toute les clés selectionnés
    else:
        return clickedItems


def rotateCylinder(cylinder,i,up):
    cylinder[clickedItems[i]] = cylinder[clickedItems[i]][1:] + cylinder[clickedItems[i]][0] if up else cylinder[clickedItems[i]][-1] + cylinder[clickedItems[i]][:-1]


def rotateCylinders(mySurface,cylinder):
    global click

    mpos = pygame.mouse.get_pos()

    # Ajoute l'action des flèches
    for i in range(len(cylinder)):
        text = arial.render("\u2191", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = (25 + (29.9 * i), 710)
        mySurface.blit(text, textRect)
        if textRect.collidepoint(mpos):
            if pygame.mouse.get_pressed()[0] and click == 1:
                rotateCylinder(cylinder, i, True)

    for i in range(len(cylinder)):
        text = arial.render("\u2193", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = (25 + (29.9 * i), 780)
        mySurface.blit(text, textRect)
        if textRect.collidepoint(mpos):
            if pygame.mouse.get_pressed()[0] and click == 1:
                rotateCylinder(cylinder, i, False)

    # Texte CLEAR
    text = roboto.render("CLEAR", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (0 + (30 * (len(cylinder) + 2)), 280)
    mySurface.blit(text, textRect)
    pygame.draw.line(mySurface, (0, 0, 0), (0, 280), (display_width, 280), 1)
    pygame.draw.line(mySurface, (0, 0, 0), (0, 305), (display_width, 305), 1)


    # Texte CIPHER
    text = roboto.render("CIPHER", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (0 + (30 * (len(cylinder) + 2)), 430)
    mySurface.blit(text, textRect)
    pygame.draw.line(mySurface, (0, 0, 0), (0, 430), (display_width, 430), 1)
    pygame.draw.line(mySurface, (0, 0, 0), (0, 455), (display_width, 455), 1)

    global finished
    # Ecriture de fichier
    if finished:
        with open("CypherText.txt", "w") as f:
            for i in range(len(cylinder)):
                f.write(cylinder[clickedItems[i]][16])

    # Texte Finished
    text = roboto.render("Finished", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (35 + (29.9 * len(cylinder)+1), 740)
    mySurface.blit(text, textRect)
    if textRect.collidepoint(mpos):
        if pygame.mouse.get_pressed()[0] and click == 1:
            finished = True



def displayAll():
    global click
    global row

    while running:
        surface.fill((255, 251, 234))
        click = 0
        row = 0
        # Permet de gérer les events
        for event in pygame.event.get():
            # Ajoute une action au bouton fermer
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = 1

        if enterKey(surface, len(cylinder)) == None:
            enterKey(surface, len(cylinder))
        else:
            rotateCylinders(surface, cylinder)
        displayCylinders(surface, cylinder)
        pygame.display.update()
        clock.tick(FPS)

displayAll()
