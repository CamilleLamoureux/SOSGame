# 2e projet de Python - SOS GAME (Groupe de 2)
# Anaïs Depeau et Camille Lamoureux
# Bibliothèque des fonctions graphiques


# Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
import sosAlgorithms

############################################################" GRAPHISME #######################################################
# Procédure qui dessine le tableau initial
def drawBoard(mySurface,n):
    BLANC = (255, 255, 255)
    GRIS = (150,150,150)
    font = pygame.font.Font(None, 30)
    S = font.render("S", 1, GRIS)
    O = font.render("O", 1, GRIS)

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

            mySurface.blit(S,(x + 10, y + 35))
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


# Procédure qui affiche la lettre posée par le joueur dont c'est le tour
def drawCell(mySurface,board,i,j,player):

    font = pygame.font.Font(None, 100)

    GRIS_FOND = (50,50,50)
    ROUGE = (255,0,0)
    VERT = (0,255,0)

    COULEUR_JOUEUR = ROUGE if player == 0 else VERT

    S = font.render("S", 1, COULEUR_JOUEUR)
    O = font.render("O", 1, COULEUR_JOUEUR)

    i, j = case(i, j)
    pygame.draw.rect(mySurface, GRIS_FOND, (i + 2, j + 2, 72, 72))

    l = board[i//75][j//75]

    if l == 1:
        mySurface.blit(S, (i + 15, j + 7))
    else :
        mySurface.blit(O, (i + 15, j + 7))




# Procédure qui dessine les nouvelles lignes représentant les alignements
#def drawLines(mySurface,lines,player):


# Procédure qui permet d'afficher le joueur gagnant
#def displayWinner(mySurface,n,scores):


######################################################## JEU ###########################################################

# Fonction qui permet au joueur de choisir une case et la lettre qu'il souhaite y mettre
def selectSquare(mySurface,board,n):
   print("i'm in")
   for event in pygame.event.get():
       int("here")
       if event.type == MOUSEBUTTONUP and event.button == 1:
           print("click !")
           i = event.pos[0]
           j = event.pos[1]

           i,j = case(i,j)

           if i%75 <= 37:
               l = 1
           else:
               l = 2


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
    player = 0

    while inProgress:

        for event in pygame.event.get():

            # Si on clique sur le bouton "fermer de la fenêtre"
            if event.type == QUIT:
                inProgress = False
            pygame.display.update()

            if event.type == MOUSEBUTTONUP and event.button == 1:
                print("click !")
                i = event.pos[0]
                j = event.pos[1]

                if i % 75 <= 37:
                    l = 1
                else:
                    l = 2
                board[i//75][j//75] = l

                drawCell(mySurface,board,i,j,player,l)

                if player == 1:
                    player = 0
                else:
                    player = 1

    pygame.quit()


# Appel de la procédure permettant de lancer le jeu
n = int(input("Choisissez la taille de votre tableau de jeu : "))
SOS(n)