# 2e projet de Python - SOS GAME (Groupe de 2)
# Anaïs Depeau et Camille Lamoureux
# Bibliothèque des fonctions graphiques


# Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
import sosAlgorithms


############################################################# GRAPHISME ###########################################################
# Procédure qui dessine le tableau initial
def drawBoard(mySurface, n):
    BLANC = (255, 255, 255)
    MARRON_CLAIR = (168, 125, 125)

    font = pygame.font.Font(None, 30)

    S = font.render("S", 1, MARRON_CLAIR)
    O = font.render("O", 1, MARRON_CLAIR)

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

    x, y = 40, 100
    for ligne in range(n):
        for colonne in range(n):
            pygame.draw.line(mySurface, MARRON_CLAIR, (x + 37, y + 10), (x + 37, y + 65), 2)

            mySurface.blit(S, (x + 10, y + 35))
            mySurface.blit(O, (x + 47, y + 35))

            x += 75
        y += 75
        x = 40


# Procédure qui affiche les scores des joueurs
def displayScore(mySurface, n, scores):
    BLEU = (28, 95, 119)
    VIOLET = (87, 25, 83)
    MARRON_CLAIR = (168, 125, 125)

    font = pygame.font.Font(None, 46)
    font_joueur = pygame.font.Font(None, 33)
    affichage_scores = font.render("Scores :", 1, (MARRON_CLAIR))
    joueur1 = font_joueur.render("Joueur 1 :", 1, (BLEU))
    joueur2 = font_joueur.render("Joueur 2 :", 1, (VIOLET))
    pts_joueur_1 = font_joueur.render(str(scores[0]), 1, (BLEU))
    pts_joueur_2 = font_joueur.render(str(scores[1]), 1, (VIOLET))

    pygame.draw.rect(mySurface, (188, 174, 174), (40 + n * 75 + 205, 190, 75, 100))

    mySurface.blit(affichage_scores, (40 + n * 75 + 60, 140))
    mySurface.blit(joueur1, (40 + n * 75 + 100, 190))
    mySurface.blit(pts_joueur_1, (40 + n * 75 + 215, 190))
    mySurface.blit(joueur2, (40 + n * 75 + 100, 220))
    mySurface.blit(pts_joueur_2, (40 + n * 75 + 215, 220))


# Procédure qui permet d'afficher quel joueur doit jouer
def displayPlayer(mySurface, n, player):
    pygame.draw.rect(mySurface, (188, 174, 174), (40 + n * 75 + 55, 180, 30, 100))

    fleche = pygame.image.load("flechejoueur.gif")

    if player == 0:

        mySurface.blit(fleche, (40 + n * 75 + 55, 195))
    else:

        mySurface.blit(fleche, (40 + n * 75 + 55, 220))


# Fonction qui retourne les coordonnées du coin en haut à gauche de la case cliquée
def case(i, j):
    i -= 40
    j -= 100
    x = i - (i % 75)
    y = j - (j % 75)
    x = x // 75
    y = y // 75
    return x, y


# Procédure qui affiche la lettre posée par le joueur dont c'est le tour
def drawCell(mySurface, board, i, j, player):
    font = pygame.font.Font(None, 100)

    BLEU = (28, 95, 119)
    VIOLET = (87, 25, 83)
    BLEU_FOND = (186, 207, 214)
    VIOLET_FOND = (204, 186, 203)

    COULEUR_JOUEUR = BLEU if player == 0 else VIOLET
    COULEUR_FOND = BLEU_FOND if player == 0 else VIOLET_FOND

    S = font.render("S", 1, COULEUR_JOUEUR)
    O = font.render("O", 1, COULEUR_JOUEUR)

    l = board[i][j]

    pygame.draw.rect(mySurface, COULEUR_FOND, (i * 75 + 2 + 40, j * 75 + 2 + 100, 72, 72))

    if l == 1:
        mySurface.blit(S, (i * 75 + 15 + 40, j * 75 + 7 + 100))
    elif l == 2:
        mySurface.blit(O, (i * 75 + 15 + 40, j * 75 + 7 + 100))


# Procédure qui dessine les nouvelles lignes représentant les alignements
def drawLines(mySurface, lines, player):
    BLEU = (8, 75, 99)
    VIOLET = (67, 5, 63)

    COULEUR_JOUEUR = BLEU if player == 0 else VIOLET

    for ligne in lines:
        pygame.draw.line(mySurface, COULEUR_JOUEUR, ligne[0], ligne[1], 5)


# Procédure qui permet d'afficher le joueur gagnant
"""def displayWinner(mySurface, n, scores):
    player = 0
    player0 = player
    player1 = 1
    font = pygame.font.Font(None, 33)
    
    if scores[player0] > scores[player1]:
        gagnant = font.render("Le  joueur 1  a gagné la partie !", 1, (132,46,27))
        mySurface.blit(gagnant, (40 + n * 75 + 45, 290))
    else:
        gagnant = font.render("Le  joueur 2  a gagné la partie !", 1, (157,62,12))
        mySurface.blit(gagnant, (40 + n * 75 + 45, 290))"""


def displayWinner(mySurface, n, scores):
    font = pygame.font.Font(None, 33)
    sosAlgorithms.winner(scores)
    gagnant = font.render(winner(scores),1,(132,46,47))
    mySurface.blit(gagnant, (40 + n * 75 + 45, 290))


############################################################### JEU ##################################################################

# Procédure qui initialise et lance la partie
def SOS(n):
    pygame.init()
    HAUTEUR = n * 75 + 140
    LARGEUR = n * 75 + 440
    MARRON_CLAIR = (168, 125, 125)

    font = pygame.font.Font(None, 100)
    titre = font.render("SOS Game!", 1, MARRON_CLAIR)

    mySurface = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption('SOS Game')
    inProgress = True

    mySurface.fill((188, 174, 174))
    mySurface.blit(titre, ((LARGEUR // 4), 20))
    board = sosAlgorithms.newboard(n)
    drawBoard(mySurface, n)

    player = 0
    scores = [0, 0]

    while inProgress:
        for event in pygame.event.get():
            # Si on clique sur le bouton "fermer de la fenêtre"
            if event.type == QUIT:
                inProgress = False

            displayScore(mySurface, n, scores)
            displayPlayer(mySurface, n, player)
            pygame.display.update()

            if event.type == MOUSEBUTTONUP and event.button == 1 and \
                    40 <= event.pos[0] <= (n + 1) * 75 and 100 <= event.pos[1 <= (n + 1) * 75]:

                i = event.pos[0]
                j = event.pos[1]

                if (i + 40) % 75 <= 37:
                    l = 1
                else:
                    l = 2

                i, j = case(i, j)

                if sosAlgorithms.possibleSquare(board, n, i, j):
                    lines = []
                    sosAlgorithms.update(board, n, i, j, l, scores, player, lines)
                    drawCell(mySurface, board, i, j, player)
                    drawLines(mySurface, lines, player)

                    if player == 1:
                        player = 0
                    else:
                        player = 1

        # Test pour savoir si c'est la fin de la partie
        nbr = 0
        for colonne in board:
            for element in colonne:
                if element == 0:
                    break
                else:
                    nbr += 1
        if nbr == n ** 2:
            sosAlgorithms.winner(scores)
            displayWinner(mySurface, n, scores)

    pygame.quit()


# Appel de la procédure permettant de lancer le jeu
n = int(input("Choisissez la taille de votre tableau de jeu : "))
SOS(n)
