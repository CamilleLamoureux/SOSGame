# 2e projet de Python - SOS GAME (Groupe de 2)
# Anaïs Depeau et Camille Lamoureux
# Bibliotheque des fonctions algorithmiques permettant le jeu


# Fonction de creation d'un nouveau tableau
def newboard(n):
    board = []
    for ligne in range(n):
        board.append(n * [0])
    return board


# Fonction qui check si la case selectionnee par le joueur est correcte
def possibleSquare(board, n, i, j):
    return True if board[i][j] == 0 else False


# Fonction qui permet de vérifier si les cases sont dans le tableau
def isintheboard(i, j, n):
    return True if 0 <= i < n and 0 <= j < n else False


# Procedure qui met a jour lines et scores si on a pose un S
def updateScoreS(board, n, i, j, scores, player, lines):
    if isintheboard(i - 1, j, n) and board[i - 1][j] == 2 and isintheboard(i - 2, j, n) and board[i - 2][j] == 1:
        scores[player] += 1
        lines.append([[(i * 75 + 40 + 37), (j * 75 + 100 + 37)], \
                      [((i - 2) * 75 + 40 + 37), (j * 75 + 100 + 37)]])

    if isintheboard(i + 1, j, n) and board[i + 1][j] == 2 and isintheboard(i + 2, j, n) and board[i + 2][j] == 1:
        scores[player] += 1
        lines.append([[(i * 75 + 40 + 37), (j * 75 + 100 + 37)], \
                      [((i + 2) * 75 + 40 + 37), (j * 75 + 100 + 37)]])

    if isintheboard(i, j - 1, n) and board[i][j - 1] == 2 and \
            isintheboard(i, j - 2, n) and board[i][j - 2] == 1:
        scores[player] += 1
        lines.append([[(i * 75 + 40 + 37), (j * 75 + 100 + 37)], \
                      [(i * 75 + 40 + 37), ((j - 2) * 75 + 100 + 37)]])

    if isintheboard(i, j + 1, n) and board[i][j + 1] == 2 and isintheboard(i, j + 2, n) and board[i][j + 2] == 1:
        scores[player] += 1
        lines.append([[(i * 75 + 40 + 37), (j * 75 + 100 + 37)],\
                      [(i * 75 + 40 + 37), ((j + 2) * 75 + 100 + 37)]])

    if isintheboard(i - 1, j - 1, n) and board[i - 1][j - 1] == 2 \
            and isintheboard(i - 2, j - 2, n) and board[i - 2][j - 2] == 1:
        scores[player] += 1
        lines.append([[(i * 75 + 40 + 37), (j * 75 + 100 + 37)],
                      [((i - 2) * 75 + 40 + 37), ((j - 2) * 75 + 100 + 37)]])

    if isintheboard(i + 1, j + 1, n) and board[i + 1][j + 1] == 2 \
            and isintheboard(i + 2, j + 2, n) and board[i + 2][j + 2] == 1:
        scores[player] += 1
        lines.append([[(i * 75 + 40 + 37), (j * 75 + 100 + 37)],
                      [((i + 2) * 75 + 40 + 37), ((j + 2) * 75 + 100 + 37)]])

    if isintheboard(i + 1, j - 1, n) and board[i + 1][j - 1] == 2 \
            and isintheboard(i + 2, j - 2, n) and board[i + 2][j - 2] == 1:
        scores[player] += 1
        lines.append([[(i * 75 + 40 + 37), (j * 75 + 100 + 37)],
                      [((i + 2) * 75 + 40 + 37), ((j - 2) * 75 + 100 + 37)]])

    if isintheboard(i - 1, j + 1, n) and board[i - 1][j + 1] == 2 \
            and isintheboard(i - 2, j + 2, n) and board[i - 2][j + 2] == 1:
        scores[player] += 1
        lines.append([[(i * 75 + 40 + 37), (j * 75 + 100 + 37)],
                      [((i - 2) * 75 + 40 + 37), ((j + 2) * 75 + 100 + 37)]])


# Procedure qui met a jour lines et scores si on a pose un O
def updateScoreO(board, n, i, j, scores, player, lines):
    if isintheboard(i - 1, j, n) and board[i - 1][j] == 1 and isintheboard(i + 1, j, n) and board[i + 1][j] == 1:
        scores[player] += 1
        lines.append([[((i - 1) * 75 + 40 + 37), (j * 75 + 100 + 37)], [((i + 1) * 75 + 40 + 37), (j * 75 + 100 + 37)]])

    if isintheboard(i, j - 1, n) and board[i][j - 1] == 1 and isintheboard(i, j + 1, n) and board[i][j + 1] == 1:
        scores[player] += 1
        lines.append([[(i * 75 + 40 + 37), ((j - 1) * 75 + 100 + 37)], [(i * 75 + 40 + 37), ((j + 1) * 75 + 100 + 37)]])

    if isintheboard(i - 1, j - 1, n) and board[i - 1][j - 1] == 1 \
            and isintheboard(i + 1, j + 1, n) and board[i + 1][j + 1] == 1:
        scores[player] += 1
        lines.append([[((i - 1) * 75 + 40 + 37), ((j - 1) * 75 + 100 + 37)],
                      [((i + 1) * 75 + 40 + 37), ((j + 1) * 75 + 100 + 37)]])

    if isintheboard(i - 1, j + 1, n) and board[i - 1][j + 1] == 1 \
            and isintheboard(i + 1, j - 1, n) and board[i + 1][j - 1] == 1:
        scores[player] += 1
        lines.append([[((i - 1) * 75 + 40 + 37), ((j + 1) * 75 + 100 + 37)],
                      [((i + 1) * 75 + 40 + 37), ((j - 1) * 75 + 100 + 37)]])


# Prodecudre qui met a jour le plateau de jeu
# AJOUTER SCORES et LINES en variables
def update(board, n, i, j, l, scores, player, lines):
    board[i][j] = l

    if l == 1:
        updateScoreS(board, n, i, j, scores, player, lines)
    elif l == 2:
        updateScoreO(board, n, i, j, scores, player, lines)


# Fonction qui retourne le gagnant de la partie
def winner(scores):
    if scores[0] > scores[1]:
        return "Player 1 wins !"
    elif scores[0] == scores[1]:
        return "Egality"
    else:
        return "Player 2 wins !"
