# 2e projet de Python - SOS GAME (Groupe de 2)
# Anaïs Depeau et Camille Lamoureux
# Bibliothèque des fonctions graphiques


# Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
import sosAlgorithms


############################################################# GRAPHISME ###########################################################
# Déclaration des couleurs
BLANC = (255, 255, 255)
MARRON_CLAIR = (168, 125, 125)
BLEU = (28, 95, 119)
VIOLET = (87, 25, 83)
BLEU_FOND = (186, 207, 214)
VIOLET_FOND = (204, 186, 203)
COULEUR_DE_FOND = (188, 174, 174)

# Déclaration des tailles
LARGEUR_CASE = 75
DEMI_CASE = 37
MARGE_GAUCHE = 40
MARGE_HAUT = 100

# Procédure qui dessine le tableau initial
def drawBoard(mySurface, n):
    # Déclaration de la police
    font = pygame.font.Font(None, 30)

    # Déclaration des lettres
    S = font.render("S", 1, MARRON_CLAIR)
    O = font.render("O", 1, MARRON_CLAIR)

    # Affichage du tableau
    x, y = 40, 100
    for i in range(n + 1):
        pygame.draw.line(mySurface, BLANC, (x, y), (x + n * LARGEUR_CASE, y), 3)
        y += LARGEUR_CASE
        pygame.display.update()

    x, y = 40, 100
    for i in range(n + 1):
        pygame.draw.line(mySurface, BLANC, (x, y), (x, y + n * LARGEUR_CASE), 3)
        x += LARGEUR_CASE
        pygame.display.update()

    x, y = 40, 100
    for ligne in range(n):
        for colonne in range(n):
            pygame.draw.line(mySurface, MARRON_CLAIR, (x + DEMI_CASE, y + 10), (x + DEMI_CASE, y + 65), 2)

            mySurface.blit(S, (x + 10, y + 35))
            mySurface.blit(O, (x + 47, y + 35))

            x += LARGEUR_CASE
        y += LARGEUR_CASE
        x = 40


# Procédure qui affiche les scores des joueurs
def displayScore(mySurface, n, scores):
    # Déclaration des polices
    font = pygame.font.Font(None, 46)
    font_joueur = pygame.font.Font(None, 33)

    # Déclaration  du titre
    affichage_scores = font.render("Scores :", 1, (MARRON_CLAIR))

    # Délcarations des points du joueur 1
    joueur1 = font_joueur.render("Joueur 1 :", 1, (BLEU))
    pts_joueur_1 = font_joueur.render(str(scores[0]), 1, (BLEU))

    # Délacarations des points du joueur 2
    joueur2 = font_joueur.render("Joueur 2 :", 1, (VIOLET))
    pts_joueur_2 = font_joueur.render(str(scores[1]), 1, (VIOLET))

    # Affichage du titre et des points des joueurs
    pygame.draw.rect(mySurface, (188, 174, 174), (MARGE_GAUCHE + n * LARGEUR_CASE + 205, 190, LARGEUR_CASE, 100))

    mySurface.blit(affichage_scores, (MARGE_GAUCHE + n * LARGEUR_CASE + 60, 140))

    mySurface.blit(joueur1, (MARGE_GAUCHE + n * LARGEUR_CASE + MARGE_HAUT, 190))
    mySurface.blit(pts_joueur_1, (MARGE_GAUCHE + n * LARGEUR_CASE + 215, 190))

    mySurface.blit(joueur2, (MARGE_GAUCHE + n * LARGEUR_CASE + MARGE_HAUT, 220))
    mySurface.blit(pts_joueur_2, (MARGE_GAUCHE + n * LARGEUR_CASE + 215, 220))


# Procédure qui permet d'afficher quel joueur doit jouer
def displayPlayer(mySurface, n, player):
    pygame.draw.rect(mySurface, (188, 174, 174), (MARGE_GAUCHE + n * LARGEUR_CASE + 55, 180, 30, MARGE_HAUT))

    fleche = pygame.image.load("flechejoueur.gif")

    if player == 0:

        mySurface.blit(fleche, (MARGE_GAUCHE + n * LARGEUR_CASE + 55, 195))
    else:

        mySurface.blit(fleche, (MARGE_GAUCHE + n * LARGEUR_CASE + 55, 220))


# Fonction qui retourne les coordonnées du coin en haut à gauche de la case cliquée
def case(i, j):
    i -= MARGE_GAUCHE
    j -= MARGE_HAUT
    x = i - (i % LARGEUR_CASE)
    y = j - (j % LARGEUR_CASE)
    x = x // LARGEUR_CASE
    y = y // LARGEUR_CASE
    return x, y


# Procédure qui affiche la lettre posée par le joueur dont c'est le tour
def drawCell(mySurface, board, i, j, player):
    font = pygame.font.Font(None, 100)

    # Détermination des couleurs à utiliser
    COULEUR_JOUEUR = BLEU if player == 0 else VIOLET
    COULEUR_FOND = BLEU_FOND if player == 0 else VIOLET_FOND

    # Déclaration des lettres
    S = font.render("S", 1, COULEUR_JOUEUR)
    O = font.render("O", 1, COULEUR_JOUEUR)

    # Récupération de la lettre choisie
    l = board[i][j]

    # Affichage de la lettre choisie
    pygame.draw.rect(mySurface, COULEUR_FOND, (i * LARGEUR_CASE + 2 + MARGE_GAUCHE, j * LARGEUR_CASE + 2 + MARGE_HAUT, 72, 72))
    if l == 1:
        mySurface.blit(S, (i * LARGEUR_CASE + 15 + MARGE_GAUCHE, j * LARGEUR_CASE + 7 + MARGE_HAUT))
    elif l == 2:
        mySurface.blit(O, (i * LARGEUR_CASE + 12 + MARGE_GAUCHE, j * LARGEUR_CASE + 7 + MARGE_HAUT))


# Procédure qui dessine les nouvelles lignes représentant les alignements
def drawLines(mySurface, lines, player):

    # Détermination de la couleur à utiliser
    COULEUR_JOUEUR = BLEU if player == 0 else VIOLET

    # Affichage des lignes
    for ligne in lines:
        pygame.draw.line(mySurface, COULEUR_JOUEUR, ligne[0], ligne[1], 5)


# Procédure qui permet d'afficher le joueur gagnant
def displayWinner(mySurface, n, scores):

    # Déclaration de la police
    font = pygame.font.Font(None, 33)

    # Affichage du joueur gagnant
    gagnant = font.render(sosAlgorithms.winner(scores),1,(132,46,47))
    mySurface.blit(gagnant, (40 + n * 75 + 45, 290))






############################################################### JEU ##################################################################
# Procédure qui gère la partie
def gameplay(mySurface, board, n, scores):

    player = 0
    inProgress = True

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
# Procédure qui initialise et lance la partie
def SOS(n):
    pygame.init()

    # Déclaration du titre de la fenêtre
    font = pygame.font.Font(None, 70)
    titre = font.render("SOS GAME "*n, 1, MARRON_CLAIR)

    # Déclaration de la taille de la fenêtre
    HAUTEUR = n * 75 + 140
    LARGEUR = n * 75 + 440

    # Création de la fenêtre
    mySurface = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption('SOS Game')

    # Affichage du design choisit
    mySurface.fill(COULEUR_DE_FOND)
    mySurface.blit(titre, (0,20))

    # Création du tableau
    board = sosAlgorithms.newboard(n)

    # Afichage du tableau
    drawBoard(mySurface, n)

    # Initialisation des scores
    scores = [0, 0]

    gameplay(mySurface, board, n, scores)

# Appel de la procédure permettant de lancer le jeu
n = int(input("Choisissez la taille de votre tableau de jeu : "))
SOS(n)
