# 2e projet de Python - SOS GAME (Groupe de 2)
# Anaïs Depeau et Camille Lamoureux
# Bibliotheque des fonctions algorithmiques permettant le jeu

# Déclaration des tailles
LARGEUR_CASE = 75
DEMI_CASE = 37
MARGE_GAUCHE = 40
MARGE_HAUT = 100


# Fonction de creation d'un nouveau tableau
def newboard(n):
    board = []                                                                                                          #création du tableau
    for ligne in range(n):
        board.append(n * [0])                                                                                           #pour chaque ligne du tableau, ajouter n élément vide [0] dans la liste
    return board


# Fonction qui check si la case selectionnee par le joueur est correcte
def possibleSquare(board, n, i, j):
    return True if board[i][j] == 0 else False                                                                          #si la case selectionnée est vide, retourner "True" > elle est disponible, sinon "False"


# Fonction qui permet de vérifier si les cases sont dans le tableau
def isintheboard(i, j, n):
    return True if 0 <= i < n and 0 <= j < n else False                                                                 #retourner "True" si les coordonnées dont on se sert, que l'on utilise, sont dans le tableau de jeu, sinon "False"


# Procedure qui met a jour lines et scores si on a pose un S
def updateScoreS(board, n, i, j, scores, player, lines):
    # Vérification des cases à gauche
    if isintheboard(i - 1, j, n) and board[i - 1][j] == 2 and isintheboard(i - 2, j, n) and board[i - 2][j] == 1:       #conditions: si case à gauche du "S posé" = 2 (donc = O) et si deux cases à gauche du "S" posé = 1 (donc = S), + vérif de isintheboard des 2 cases
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui pose a lettre
        lines.append([[(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],     #mise à jour de lines pour tracer le trait sur le "SOS" qui vient d'être créé
                      [((i - 2) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE),                                             #coordonnées des cases "S" du SOS, en fonction de la marge de la fenêtre et de la largeur de la case
                       (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]])                                                   #on commence le trait au milieu des cases "S"

    # Vérification des cases à droite
    if isintheboard(i + 1, j, n) and board[i + 1][j] == 2 and isintheboard(i + 2, j, n) and board[i + 2][j] == 1:       #conditions: si 2e case droite "S" posé = 1 (donc = S) et si 1e case droite "S" posé = 2 (donc = O), + isintheboard
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui pose la lettre
        lines.append([[(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],     #mise à jour de lines > coordonnées des milieux des deux cases "S" du SOS créé
                      [((i + 2) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE),                                             #en fonction de largeur case et marge de la fenêtre, on commence le trait au milieu des cases "S"
                       (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]])

    # Vérification des cases au dessus
    if isintheboard(i, j - 1, n) and board[i][j - 1] == 2 and isintheboard(i, j - 2, n) and board[i][j - 2] == 1:       #conditions: si 2e case au dessus du "S" posé = 1 et si 1e case au dessus du "S" = 2,  + isintheboard
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui poe la lettre
        lines.append([[(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],     #mise à jour lines > coordonnées des milieus des deux cases "S" du SOS créé
                      [(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE),                                                   #en fonction de largeur case et marge fenêtre
                       ((j - 2) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]])

    # Vérification des cases en dessous
    if isintheboard(i, j + 1, n) and board[i][j + 1] == 2 and isintheboard(i, j + 2, n) and board[i][j + 2] == 1:       #conditions: si 1ere case en dessous = 2 (soit "O") et si 2 ème case en dessous =1 ( soit "S"), + isintheboard
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui pose la lettre
        lines.append([[(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],     #mise à jour lines > coordonnées des milieus des deux cases "S" du SOS créé
                      [(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE),                                                   #en fonction de la largeur des cases  et de la marge fenêtre
                       ((j + 2) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]])

    # Vérification des cases en diagonale en haut à gauche
    if isintheboard(i - 1, j - 1, n) and board[i - 1][j - 1] == 2 \
            and isintheboard(i - 2, j - 2, n) and board[i - 2][j - 2] == 1:                                             #conditions: si case haut gauche = 2 et si 2ème case haut gauche = 1, + vérif fctn isintheboard
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui pose la lettre
        lines.append([[(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],     #mise à jour lines > comme mise à jour précédente, avec nouveaux coordonnées
                      [((i - 2) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE),
                       ((j - 2) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]])

    # Vérification des cases en diagonale en bas à droite
    if isintheboard(i + 1, j + 1, n) and board[i + 1][j + 1] == 2 \
            and isintheboard(i + 2, j + 2, n) and board[i + 2][j + 2] == 1:                                             #conditions: si 1ère case bas-droite du "S" posé = 2  et 2ème case bas-droite = 1, + vérif fctn isintheboard
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui pose  la lettre
        lines.append([[(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],     #mise à jour lines > comme précédemment , avec nouveaux coordonnées
                      [((i + 2) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE),
                       ((j + 2) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]])

    # Vérification des cases en digonale en haut à droite
    if isintheboard(i + 1, j - 1, n) and board[i + 1][j - 1] == 2 \
            and isintheboard(i + 2, j - 2, n) and board[i + 2][j - 2] == 1:                                             #conditions: si 1ère case haut-droite du "S" = 2 et 2ème case haut-droite = 1, + fctn isintheboard
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui pose la lettre
        lines.append([[(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],     #mise à jour lines > comme précédemment, avec nouveaux coordonnées
                      [((i + 2) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE),
                       ((j - 2) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]])

    # Vérification des cases en diagonale en bas à gauche
    if isintheboard(i - 1, j + 1, n) and board[i - 1][j + 1] == 2 \
            and isintheboard(i - 2, j + 2, n) and board[i - 2][j + 2] == 1:                                             #conditions: si 1ère case bas-gauche du "S" = 2 (donc O) et 2ème case bas-gauche du "S" = 1 (donc S), + isintheboard
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui pose la lettre
        lines.append([[(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],     #mise à jour de lines > comme précédemment, avec nouveaux coordonnées
                      [((i - 2) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE),
                       ((j + 2) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]])


# Procedure qui met a jour lines et scores si on a pose un O
def updateScoreO(board, n, i, j, scores, player, lines):
    # Vérification des cases à l'horizontale
    if isintheboard(i - 1, j, n) and board[i - 1][j] == 1 and isintheboard(i + 1, j, n) and board[i + 1][j] == 1:       #condition: cases à gauche et à droite du "O" posé = 1 ( 1 étant = à S) & vérification si cases sont dans le tableau
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui pose la lettre
        lines.append(                                                                                                   #mise à jour de "lines" pour tracer le trait sur le SOS
            [[((i - 1) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],        #coordonnées des cases S à gauche et droite du "O" posé pour tracer le trait entre ces deux points
             [((i + 1) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), (j * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]])       #en fonction de la marge, la largeur de la case et pour que le trait aille des milieux des cases des S

    # Vérification des cases à la verticale
    if isintheboard(i, j - 1, n) and board[i][j - 1] == 1 and isintheboard(i, j + 1, n) and board[i][j + 1] == 1:       #condition: case en haut et en bas du "O" posé = 1 (1 étant = à S) & vérification de la fonction "isintheboard"
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui pose la lettre
        lines.append(                                                                                                   #mise à jour de lines
            [[(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), ((j - 1) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],        #coordonnées des cases S en haut et en bas du "O" posé
             [(i * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), ((j + 1) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]])       #en fonction de la marge, largeur de la case, et des moitiés des cases S

    # Vérification des cases en diagonale (de en haut à gauche à en bas à droite)
    if isintheboard(i - 1, j - 1, n) and board[i - 1][j - 1] == 1\
            and isintheboard(i + 1, j + 1, n) and board[i + 1][j + 1] == 1:                                             #condition: cases en haut à gauche et en bas à droite du "O" = 1 & vérification de fonction "isintheboard"
        scores[player] += 1                                                                                             #mise à jour score joueur et augmentation de 1 du joueur qui pose la lettre
        lines.append(                                                                                                   #mise à jour de lines
            [[((i - 1) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), ((j - 1) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],  #coordonnées des cases S en diagonale du "O" posé
             [((i + 1) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), ((j + 1) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]]) #en fonction du milieu des cases S pour faire partir le trait au centre des cases

    # Vérification des cases en diagonale (de en bas à gauche à en haut à droite)
    if isintheboard(i - 1, j + 1, n) and board[i - 1][j + 1] == 1 \
            and isintheboard(i + 1, j - 1, n) and board[i + 1][j - 1] == 1:                                             #condition: case en haut à droite et en bas à gauche du "O" = 1 & vérif de la fctn "isintheboard" pour les deux cases
        scores[player] += 1                                                                                             #ajouter un point au score du joueur qui pose la lettre
        lines.append(                                                                                                   #mise à jour de lines
            [[((i - 1) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), ((j + 1) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)],  #coordonnées des cases S en diagonale du "O" posé
             [((i + 1) * LARGEUR_CASE + MARGE_GAUCHE + DEMI_CASE), ((j - 1) * LARGEUR_CASE + MARGE_HAUT + DEMI_CASE)]]) #en fonction de la marge, largeur, et milieux des cases S


# Prodecudre qui met a jour le plateau de jeu
# AJOUTER SCORES et LINES en variables
def update(board, n, i, j, l, scores, player, lines):
    # Mise à jour du tableau
    board[i][j] = l

    # Appel de la procédure associée à la lettre choisie
    if l == 1:                                                                                                          #condition: si la variable l vaut "S"
        updateScoreS(board, n, i, j, scores, player, lines)                                                             #appel de la fonction "updateScoreS" décrite plus haut
    elif l == 2:                                                                                                        #condition:  si la variable l vaut "O"
        updateScoreO(board, n, i, j, scores, player, lines)                                                             #appel de la fonction "updateScoreO" décrite plus haut


# Fonction qui retourne le gagnant de la partie
def winner(scores):
    if scores[0] > scores[1]:                                                                                           #condition: si le score final du joueur 1 est supérieure au score final du joueur 2
        return "Le joueur 1 gagne la partie !"                                                                          #inscription dans la fenêtre de jeu " Le joueur 1 gagne la partie"
    elif scores[0] == scores[1]:                                                                                        #autre condition: si les sscores finau sont égaux
        return "Égalité..."                                                                                             #inscription dans la fenêtre de jeu "Egalité"
    else:                                                                                                               #si les conditions précédentes sont fausses
        return "Le joueur 2 gagne la partie !"                                                                          #inscription dans la fenêtre de jeu " Le joueur 2 gagne la partie"
