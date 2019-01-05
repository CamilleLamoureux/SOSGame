# 2e projet de Python - SOS GAME (Groupe de 2)
# Anaïs Depeau et Camille Lamoureux
# Bibliothèque des fonctions graphiques


# Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
import sosAlgorithms


# Procédure qui dessine le tableau initial
def drawBoard(mySurface,n):
    BLANC = (255, 255, 255)
    GRIS = (150,150,150)

    x, y = 0,0
    for i in range(n + 1):
        pygame.draw.line(mySurface, BLANC, (x, y), (x + n * 75, y), 3)
        y += 75
        pygame.display.update()

    x, y = 0,0
    for i in range(n + 1):
        pygame.draw.line(mySurface, BLANC, (x, y), (x, y + n * 75), 3)
        x += 75
        pygame.display.update()

    x,y = 0,0
    for ligne in range(n):
        for colonne in range(n):
            pygame.draw.line(mySurface, GRIS, (x + 37, y + 10), (x + 37, y + 65), 2)

            font = pygame.font.Font(None, 30)

            S = font.render("S", 1, GRIS)
            mySurface.blit(S,(x + 10, y + 35))

            O = font.render("O", 1, GRIS)
            mySurface.blit(O,(x + 47, y + 35))

            x += 75
        y += 75
        x = 0


# Procédure qui affiche les scores des joueurs
#def displayScore(mySurface,n,scores):


# Procédure qui permet d'afficher quel joueur doit jouer
#def displayPlayer(mySurface,n,player):

# Fonction qui retourne les coordonnées du coin en haut à gauche de la case cliquée
def case(i,j):
    x = i - (i%75)
    y = j - (j%75)
    return x,y


# Fonction qui retourne la couleur dans laquelle doit être mis la lettre
def colorPlayer(board):
    nbr = 0
    for colonne in board :
        for element in colonne:
            if element != 0:
                nbr += 1

    nombre_tours = n**2 - (nbr)

    if nombre_tours%2 == 0:
        return (255,0,0)
    else:
        return (0,255,0)

# Procédure qui affiche la lettre posée par le joueur dont c'est le tour
def drawCell(mySurface,board,i,j):
    x,y = case(i, j)

    font = pygame.font.Font(None, 100)

    GRIS_FOND = (50,50,50)
    COULEUR_JOUEUR = colorPlayer(board)

    if i%75 <= 37:
        print("S")
        l = 1
        pygame.draw.rect(mySurface,GRIS_FOND,(x+2,y+2,72,72))
        S = font.render("S", 1, COULEUR_JOUEUR)
        mySurface.blit(S, (x + 15, y + 7))

    else :
        print("O")
        l = 2
        pygame.draw.rect(mySurface,GRIS_FOND, (x+2, y+2, 72, 72))
        O = font.render("O", 1, COULEUR_JOUEUR)
        mySurface.blit(O, (x + 15, y + 7))

    board[i//75][j//75] = l
    print(board)


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
    mySurface = pygame.display.set_mode((n*75, n*75))
    pygame.display.set_caption('SOS Game')
    inProgress = True

    mySurface.fill((50,50,50))
    board = sosAlgorithms.newboard(n)
    drawBoard(mySurface, n)

    while inProgress:

        for event in pygame.event.get():

            # Si on clique sur le bouton "fermer de la fenêtre"
            if event.type == QUIT:
                inProgress = False
            pygame.display.update()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                i = event.pos[0]
                j = event.pos[1]
                drawCell(mySurface,board,i,j)

    pygame.quit()


# Appel de la procédure permettant de lancer le jeu
n = int(input("Choisissez la taille de votre tableau de jeu : "))
SOS(n)