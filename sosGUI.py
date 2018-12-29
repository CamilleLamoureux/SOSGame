# 2e projet de Python - SOS GAME (Groupe de 2)
# Anaïs Depeau et Camille Lamoureux
# Bibliothèque des fonctions graphiques

# Importation des bibliothèques nécessaire
import pygame
import sosAlgorithms
from pygame.locals import *


# Procédure qui dessine le tableau initial
def drawBoard(mySurface,n):
    BLANC = (255, 255, 255)

    x, y = 40, 100
    for i in range(n + 1):
        pygame.draw.line(mySurface, BLANC, (x, y), (x + n * 75, y), 3)
        y += 75
        pygame.display.update()

    x, y = 40, 100
    for i in range(n + 1):
        pygame.draw.line(mySurface, BLANC, (x, y), (x, y + n * 75), 3)
        x += 75
        pygame.display.update()


# Procédure qui affiche les scores des joueurs
#def displayScore(mySurface,n,scores):


# Procédure qui permet d'afficher quel joueur doit jouer
#def displayPlayer(mySurface,n,player):


# Procédure qui affiche la lettre posée par le joueur dont c'est le tour
#def drawCell(mySurface,board,i,j,player):


# Procédure qui dessine les nouvelles lignes représentant les alignements
#def drawLines(mySurface,lines,player):


# Procédure qui permet d'afficher le joueur gagnant
#def displayWinner(mySurface,n,scores):


# Fonction qui permet au joueur de choisir une case et la lettre qu'il souhaite y mettre
#def selectSquare(mySurface,board,n):


# Procédure qui gère le déroulement de la partie
#def gamePlay(mySurface,board,n,scores):


# Procédure qui initialise et lance la partie
def SOS(n):

    pygame.init()
    mySurface = pygame.display.set_mode((n*200, n*100))
    pygame.display.set_caption('SOS Game')
    inProgress = True

    drawBoard(mySurface,n)

    while inProgress:

        for event in pygame.event.get():

            #Si on clique sur le bouton "fermer de la fenêtre"
            if event.type == QUIT:
                inProgress = False
            pygame.display.update()


    pygame.quit()


# Appel de la procédure permettant de lancer le jeu
n = int(input("Choisissez la taille de votre tableau de jeu : "))
SOS(n)