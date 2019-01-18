# 2e projet de Python - SOS GAME (Groupe de 2)
# Anaïs Depeau et Camille Lamoureux
# Bibliothèque des fonctions graphiques


# Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
import sosAlgorithms

#################################################### GRAPHISME #########################################################
# Déclaration des couleurs
BLANC = (255, 255, 255)
MARRON_CLAIR = (168, 125, 125)
BLEU = (28, 95, 119)
VIOLET = (87, 25, 83)
BLEU_FOND = (186, 207, 214)
VIOLET_FOND = (204, 186, 203)
COULEUR_DE_FOND = (188, 174, 174)
ROUGE = (231, 62, 1)

# Déclaration des tailles
LARGEUR_CASE = 75
DEMI_CASE = 37
MARGE_GAUCHE = 40
MARGE_HAUT = 100
MARGE_DROITE = 400
MARGE_BAS = 40


# Procédure qui dessine le tableau initial
def drawBoard(mySurface, n):
    """
    :param mySurface: fenetre de jeu pygame
    :param n: taille du tableau de jeu
    :return: nothing
    """
    # Déclaration de la police
    font = pygame.font.Font(None, 30)                                                                                   # On déclare la police et la taille d'écriture

    # Déclaration des lettres
    S = font.render("S", 1, MARRON_CLAIR)                                                                               # On créé une variable "S" qui permettra d'afficher un S dans le police définie précédement, dans le couleur "Marron Clair"
    O = font.render("O", 1, MARRON_CLAIR)                                                                               # On fait de même pour le O

    # Affichage du tableau
    x, y = MARGE_GAUCHE, MARGE_HAUT                                                                                     # Le début du tableau est à 40px de la gauche et 100px du haut, qui sont les marges
    for i in range(n + 1):                                                                                              # On trace n+1 lignes, car il faut "fermer" le tableau, et il y a donc une ligne de plus qu'il n'y a de cases
        pygame.draw.line(mySurface, BLANC, (x, y), (x + n * LARGEUR_CASE, y), 3)                                        # On trace une ligne de n cases de long et de 3px d'épaisseur
        y += LARGEUR_CASE                                                                                               # On implémente l'ordonnée de la taille d'une case pour tracer la ligne en dessous

    x, y = MARGE_GAUCHE, MARGE_HAUT                                                                                     # On revient au point de départ du tableau pour tracer les lignes verticales
    for i in range(n + 1):                                                                                              # On trace une nouvelle fois n+1 lignes
        pygame.draw.line(mySurface, BLANC, (x, y), (x, y + n * LARGEUR_CASE), 3)                                        # On trace une ligne de n cases de long et de 3px d'épaisseur
        x += LARGEUR_CASE                                                                                               # On implémente l'abscisse de la taille d'une case pour tracer la ligne à droite

    x, y = MARGE_GAUCHE, MARGE_HAUT                                                                                     # On revient au point de départ du tableau pour mettre les "S|0" dans les cases qui sont au départ toutes vides
    for ligne in range(n):                                                                                              # Pour toutes les lignes du tableau (de taille n)
        for colonne in range(n):                                                                                        # Pour toutes les colonnes de cette ligne
            pygame.draw.line(mySurface, MARRON_CLAIR, (x + DEMI_CASE, y + 10), (x + DEMI_CASE, y + 65), 2)              # On trace une ligne au milieu pour marquer la séparation entre les deux lettres

            mySurface.blit(S, (x + 10, y + 35))                                                                         # On met un S à gauche de la ligne
            mySurface.blit(O, (x + 47, y + 35))                                                                         # On met un O à droite de la ligne

            x += LARGEUR_CASE                                                                                           # On passe à la colonne suivante en incrémentant l'abscisse
        y += LARGEUR_CASE                                                                                               # Quand on a finit une colonne, on passe à la ligne suivante en incrémentant l'ordonnée
        x = MARGE_GAUCHE                                                                                                # On revient à la première colonne
    pygame.display.update()                                                                                             # On met à jour l'affichage

# Procédure qui affiche les scores des joueurs
def displayScore(mySurface, n, scores):
    """
    :param mySurface: fenetre de jeu pygame
    :param n: taille du tableau
    :param scores: liste contenant les scores des joueurs
    :return: nothing
    """
    # Déclaration des polices
    font = pygame.font.Font(None, 46)                                                                                   # On déclare la police et la taille d'écriture dans laquelle on écrira le mot "Scores"
    font_joueur = pygame.font.Font(None, 33)                                                                            # On déclare la police et la taille d'écriture dans laquelle on écrira le numéro du joueur et les points

    # Déclaration  du titre
    affichage_scores = font.render("Scores :", 1, (MARRON_CLAIR))                                                       # On déclare une variable pour le mot "Scores" qui utilisera la police définie plus haut et la couleur Marron Clair

    # Délcarations des points du joueur 1
    joueur1 = font_joueur.render("Joueur 1 :", 1, (BLEU))                                                               # On déclare une variable pour afficher le nom du joueur dans sa couleur
    pts_joueur_1 = font_joueur.render(str(scores[0]), 1, (BLEU))                                                        # Et son nombre de points, toujours dans sa couleur

    # Délacarations des points du joueur 2
    joueur2 = font_joueur.render("Joueur 2 :", 1, (VIOLET))                                                             # On fait de même avec le deuxième joueur
    pts_joueur_2 = font_joueur.render(str(scores[1]), 1, (VIOLET))

    # Affichage du titre et des points des joueurs
    pygame.draw.rect(mySurface, (188, 174, 174), (MARGE_GAUCHE + n * LARGEUR_CASE + 205, 190, LARGEUR_CASE, 100))       # On place un rectangle de la couleur du fond pour "effacer" les anciens points

    mySurface.blit(affichage_scores, (MARGE_GAUCHE + n * LARGEUR_CASE + 60, 140))                                       # On place le mot "scores"

    mySurface.blit(joueur1, (MARGE_GAUCHE + n * LARGEUR_CASE + MARGE_HAUT, 190))                                        # On place le mot "joueur 1"
    mySurface.blit(pts_joueur_1, (MARGE_GAUCHE + n * LARGEUR_CASE + 215, 190))                                          # Et son nombre de points en se servant du tableau "scores"

    mySurface.blit(joueur2, (MARGE_GAUCHE + n * LARGEUR_CASE + MARGE_HAUT, 220))                                        # On fait de même pour le deuxième joueur
    mySurface.blit(pts_joueur_2, (MARGE_GAUCHE + n * LARGEUR_CASE + 215, 220))

    pygame.display.update()                                                                                             # On met à jour l'affichage
                                                                                                                        # Vous avez lu ça ?

# Procédure qui permet d'afficher quel joueur doit jouer
def displayPlayer(mySurface, n, player):
    """
    :param mySurface: fenetre de jeu pygame
    :param n: taille du plateau
    :param player: (0 ou 1) numéro du joueur actuel
    :return: nothing
    """
    pygame.draw.rect(mySurface, (188, 174, 174), (MARGE_GAUCHE + n * LARGEUR_CASE + 55, 180, 30, MARGE_HAUT))           # On place un rectangle de la couleur du fond pour effacer l'ancienne flèche qui indiquait le tour du joueur

    fleche = pygame.image.load("flechejoueur.gif")                                                                      # On charge l'image dans une variable

    if player == 0:                                                                                                     # Si c'est le tour du joueur 1...
        mySurface.blit(fleche, (MARGE_GAUCHE + n * LARGEUR_CASE + 55, 195))                                             # On place la flèche devant son "nom"
    else:                                                                                                               # Sinon
        mySurface.blit(fleche, (MARGE_GAUCHE + n * LARGEUR_CASE + 55, 220))                                             # On place la flèche devant le "nom" du joueur 2

    pygame.display.update()                                                                                             # On met à jour l'affichage


# Fonction qui retourne les coordonnées du coin en haut à gauche de la case cliquée
def case(i, j):
    """
    :param i: distance entre le clic et le bord gauche de la fenetre en px
    :param j: distance entre le clic et le bord supérieur de la fenetre en px
    :return: coordonnées de la case (entre 0 et n)
    """
    i -= MARGE_GAUCHE                                                                                                   # On enlève la marge aux coordonnées du pixel auquelles le joueur à cliqué
    j -= MARGE_HAUT                                                                                                     # On enlève de même la marge du haut
    x = i - (i % LARGEUR_CASE)                                                                                          # On "ramène" au pixel le plus en haut à gauche de la case en enlevant ce qu'il y a "en trop" par rapport à la largeur simple de la case
    y = j - (j % LARGEUR_CASE)                                                                                          # De même avec l'ordonnée
    x = x // LARGEUR_CASE                                                                                               # Puis on divise par la taille d'une case pour avoir des nombre utilisables en tant que tel dans le tableau "théorique" (la liste à double dimension représentant toutes les cases)
    y = y // LARGEUR_CASE                                                                                               # De même avec l'ordonnée
    return x, y                                                                                                         # On retourne les nouvelles valeures (comprises entre 0 et n)


# Procédure qui affiche la lettre posée par le joueur dont c'est le tour
def drawCell(mySurface, board, i, j, player):
    """
    :param mySurface: fenetre de jeu pygame
    :param board: liste à double dimension représentant le tableau
    :param i: coordonnée (entre 0 et n) de la colonne de la case sur laquelle à cliqué le joueur
    :param j: coordonnée (entre 0 et n) de la ligne de la case sur laquelle à cliqué le joueur
    :param player: (0 ou 1) numéro du joueur dont c'est le tour
    :return: nothing
    """
    font = pygame.font.Font(None, 100)                                                                                  # On déclare la police et la taille d'écriture pour le contenue des cellules (les lettres que les joueurs choisiront)

    # Détermination des couleurs à utiliser
    COULEUR_JOUEUR = BLEU if player == 0 else VIOLET                                                                    # Si c'est au joueur 1 de jouer, alors sa couleur sera le bleu, sinon ce sera le violet
    COULEUR_FOND = BLEU_FOND if player == 0 else VIOLET_FOND                                                            # Même principe pour la couleur de fond de la case

    # Déclaration des lettres
    S = font.render("S", 1, COULEUR_JOUEUR)                                                                             # On déclare les lettres dans des variables
    O = font.render("O", 1, COULEUR_JOUEUR)

    # Récupération de la lettre choisie
    l = board[i][j]                                                                                                     # On récupère la lettre choisie par le joueur (qui est déjà stockée dans la liste "board")

    # Affichage de la lettre choisie
    pygame.draw.rect(mySurface, COULEUR_FOND,                                                                           # On dessine un rectangle en fond de la case en fonction du joueur dont c'est le tour
                     (i * LARGEUR_CASE + 2 + MARGE_GAUCHE, j * LARGEUR_CASE + 2 + MARGE_HAUT, 72, 72))                  # Il a pour coordonnées i et j (transformées) et fait la même largeur que la case, moins l'épaisseur des lignes, soit 3px
    if l == 1:                                                                                                          # Si j'ai un S que le joueur à choisit
        mySurface.blit(S, (i * LARGEUR_CASE + 15 + MARGE_GAUCHE, j * LARGEUR_CASE + 7 + MARGE_HAUT))                    # On affiche un S dans toute la case, de la couleur du joueur
    elif l == 2:                                                                                                        # Sinon, si c'est un O qu'il a choisit
        mySurface.blit(O, (i * LARGEUR_CASE + 12 + MARGE_GAUCHE, j * LARGEUR_CASE + 7 + MARGE_HAUT))                    # On affiche un O dans toute la case, de la couleur du joueur
                                                                                                                        # Vous lisez vraiment toooouuuuut ça ?! Chapeau !
    pygame.display.update()                                                                                             # On met à jour l'affichage


# Procédure qui dessine les nouvelles lignes représentant les alignements
def drawLines(mySurface, lines, player):
    """
    :param mySurface: fenetre de jeu pygame
    :param lines: liste à double dimension de tuples contenant toutes les lignes ajoutées pendant ce tour
    :param player: (0 ou 1) numéro du joueur dont c'est le tour
    :return: nothing
    """
    # Détermination de la couleur à utiliser
    COULEUR_JOUEUR = BLEU if player == 0 else VIOLET                                                                    # Si c'est le joueur 1 qui joue, alors sa couleur sera le bleu, sinon ce sera le violet

    # Affichage des lignes
    for ligne in lines:                                                                                                 # Pour toutes les lignes dans la liste contenant toutes les nouvelles lignes qu'il faut tracer
        pygame.draw.line(mySurface, COULEUR_JOUEUR, ligne[0], ligne[1], 5)                                              # On trace une ligne en utilisant les coordonnées du tuple du rang de la ligne qu'on traite

    pygame.display.update()                                                                                             # On met à jour l'affichage


# Procédure qui permet d'afficher le joueur gagnant
def displayWinner(mySurface, n, scores):
    """
    :param mySurface: fenetre de jeu pygame
    :param n: taille du tableau de jeu
    :param scores: liste contenant les scores des joueurs
    :return: nothing
    """

    # Déclaration de la police
    font = pygame.font.Font(None, 36)                                                                                   # On déclare la police et la taille d'écriture

    # Affichage du joueur gagnant
    gagnant = font.render(sosAlgorithms.winner(scores), 1, ROUGE)                                                       # On met dans une variable le texte retourné par la fonction définissant qui est le vainqueur
    mySurface.blit(gagnant, (40 + n * 75 + 45, 290))                                                                    # On l'affiche

    pygame.display.update()                                                                                             # On met à jour l'affichage


##################################################### JEU ##############################################################
# Procédure qui gère la partie
def gameplay(mySurface, board, n, scores):
    """
    :param mySurface: fenetre de jeu pygame
    :param board: liste à double dimension représentant le tableau
    :param n: taille du tableau de jeu
    :param scores: liste contenant les scores des joueurs
    :return: nothing
    """
    # Initialisation des variables
    player = 0                                                                                                          # C'est le joueur 1 commence à jouer
    inProgress = True                                                                                                   # On lance la partie

    while inProgress:                                                                                                   # Tant que la partie est en cours
        for event in pygame.event.get():

            # Si on clique sur le bouton "fermer de la fenêtre"
            if event.type == QUIT:                                                                                      # Si on clic sur la "croix"
                inProgress = False                                                                                      # On arrête la partie

            # Affichage des scores
            displayScore(mySurface, n, scores)                                                                          # On appelle la fonction permettant d'afficher les scores des joueurs

            # Affichage de la flèche indiquant quel joueur doit jouer
            displayPlayer(mySurface, n, player)                                                                         # On appelle la focntion permettant d'affciher le joueur dont c'est le tour

            # Si il y a un relache le bouton gauche de la souris et que le clic est dans le tableau
            if event.type == MOUSEBUTTONUP and event.button == 1 and \
                    MARGE_GAUCHE <= event.pos[0] <= (n + 1) * LARGEUR_CASE \
                    and MARGE_HAUT <= event.pos[1 <= (n + 1) * LARGEUR_CASE]:                                           # Si on fait un clique gauche dans le tableau

                # On stocke les coordonnées du clic
                i = event.pos[0]                                                                                        # On récupère l'abscisse du clic
                j = event.pos[1]                                                                                        # On récupère l'ordonnée du clic

                # Si le clic est sur la partie gauche de la case
                if (i - MARGE_GAUCHE) % LARGEUR_CASE <= DEMI_CASE:                                                      # Si on clique dans la partie gauche de la case (sur le S)
                    l = 1                                                                                               # Ca veut dire qu'on a demandé un S, donc l vaut 1
                else:                                                                                                   # Sinon
                    l = 2                                                                                               # Ca veut sire qu'on a demandé un O,donc l vaut 2

                # Convertion des coordonnées en px en coordonnées pour le tableau
                i, j = case(i, j)                                                                                       # On convertit les coordonnées en pixel, en coordonnées pour le tableau (entre 0 et n)

                # Si la case choisie est correcte
                if sosAlgorithms.possibleSquare(board, n, i, j):                                                        # Si la case sur laquelle on a cliqué est correcte
                    # Remise à zéro de la variable qui stocke les sos du tour
                    lines = []                                                                                          # On remet lines à zéro pour ne pas redessiner toutes les lignes

                    # Mise à jour suite au tour du joueur
                    sosAlgorithms.update(board, n, i, j, l, scores, player, lines)                                      # On appelle la procédure update, qui permet de mettre à jour l'affichage suite à la pose d'une lettre
                    drawCell(mySurface, board, i, j, player)                                                            # On appelle la procédure qui permet d'afficher la lettre choisie par le joueur dans sa couleur
                    drawLines(mySurface, lines, player)                                                                 # On appelle la procédure pqui permet d'afficher les SOS fait par le joueur dans ce tour dans sa couleur

                    # Changement de joueur
                    if player == 1:                                                                                     # Si c'était le tour du joueur 2
                        player = 0                                                                                      # Alors c'est au tour du joueur 1
                    else:                                                                                               # Sinon, si c'était le tour du joueur 1
                        player = 1                                                                                      # C'est le tour du joueur 2

        # Test pour savoir si c'est la fin de la partie
        nbr = 0                                                                                                         # On initialise un compteur
        for colonne in board:                                                                                           # On parcourt tout le tableau
            for element in colonne:
                if element == 0:                                                                                        # Si on a une case vide
                    break                                                                                               # On arrète, si jamais on trouve une case vide dans le tableau
                else:                                                                                                   # Sinon, si la case a déjà une valeur
                    nbr += 1                                                                                            # On ajoute 1 au compteur
        if nbr == n ** 2:                                                                                               # Si toutes les cases ont déjà une lettre
            # Détermination du gagnant
            sosAlgorithms.winner(scores)                                                                                # Alors on détermine le gagnant, car ça veut dire que la partie est finie
            displayWinner(mySurface, n, scores)                                                                         # On affiche le joueur gagnant

    pygame.quit()                                                                                                       # On quitte pygame


# Procédure qui initialise et lance la partie
def SOS(n):
    """
    :param n: taille du plateau de jeu
    :return: nothing
    """
    pygame.init()                                                                                                       # On intialise pygame

    # Déclaration du titre de la fenêtre
    font = pygame.font.Font(None, 70)                                                                                   # On déclare la police et la taille d'écriture du titre
    titre = font.render("SOS GAME " * n, 1, MARRON_CLAIR)                                                               # On met dans une variable la "bannière" de titre (c'est purement esthétique)

    # Déclaration de la taille de la fenêtre
    HAUTEUR = n * LARGEUR_CASE + MARGE_HAUT + MARGE_BAS                                                                 # La fenetre fait une hauteur de la taille du tableau, + la marge du haut(100px) et la marge du bas (40px)
    LARGEUR = n * LARGEUR_CASE + MARGE_GAUCHE + MARGE_DROITE                                                            # La fenetre fait une largeur de la taille du tableau, + la marge à gauche (40px) et la marge à droite (400px)

    # Création de la fenêtre
    mySurface = pygame.display.set_mode((LARGEUR, HAUTEUR))                                                             # On créé une fenetre de jeu pygame
    pygame.display.set_caption('SOS Game')                                                                              # On lui donne un titre

    # Affichage du design choisit
    mySurface.fill(COULEUR_DE_FOND)                                                                                     # On remplit la fenetre de la couleur de fond
    mySurface.blit(titre, (0, 20))                                                                                      # On affiche le titre

    # Création du tableau
    board = sosAlgorithms.newboard(n)                                                                                   # On créer le tableau de jeu initial
    drawBoard(mySurface, n)                                                                                             # On l'affiche

    # Initialisation des scores
    scores = [0, 0]                                                                                                     # On initialise les scores

    # Lancement de la partie
    gameplay(mySurface, board, n, scores)                                                                               # On lance la partie


# Appel de la procédure permettant d'initialiser et lancer la partie
n = int(input("Choisissez la taille de votre tableau de jeu : "))                                                       # On demande la taille du tableau au joueur
SOS(n)                                                                                                                  # On lance l'initialisation de la partie
