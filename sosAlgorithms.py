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
    return True if board[i][j] == 0 and (0 < i <= n and 0 < j <= n) else False


# Procedure qui met a jour lines et scores si on a pose un S
def updateScoreS(board, n, i, j, scores, player, lines):
    board[i][j] = 1
    if possibleSquare(board, n, i, j):
        if (board[i-1][j]==2 and board[i-2][j]==1) or (board[i+1][j]==2 and board[i+2][j]==1) or (board[i][j-1]==2 and board[i][j-2]==1) or (board[i][j+1]==2 and board[i][j+2]==1) or (board[i-1][j-1]==2 and board[i-2][j-2]==1) or (board[i+1][j+1]==2 and board[i+2][j+2]==1) or ( board[i+1][j-1]==2 and board[i+2][j-2]==1) or (board[i-1][j+1]==2 and board[i-2][j+2]==1):
            scores[player] += 1
            lines

# Procedure qui met a jour lines et scores si on a pose un O
def updateScoreO(board, n, i, j, scores, player, lines):
    board[i][j] = 2
    if possibleSquare(board, n, i,j):
        if (board[i - 1][j] == 1 and board[i + 1][j] == 1) or (board[i][j - 1] == 1 and board[i][j + 1] == 1) or (board[i - 1][j - 1] == 1 and board[i + 1][j + 1] == 1) or (board[i - 1][j + 1] == 1 and board[i + 1][j - 1] == 1):
            scores[player] += 1
            lines

# Procedure qui met a jour lines et scores si on a pose un O
def updateScoreO(board, n, i, j, scores, player, lines):
    board[i][j] = 2
    if possibleSquare(board, n, i,j):
        if (board[i - 1][j] == 1 and board[i + 1][j] == 1) or (board[i][j - 1] == 1 and board[i][j + 1] == 1) or (board[i - 1][j - 1] == 1 and board[i + 1][j + 1] == 1) or (board[i - 1][j + 1] == 1 and board[i + 1][j - 1] == 1):
            scores[player] += 1
            lines


# Prodecudre qui met a jour le plateau de jeu
# AJOUTER SCORES et LINES en variables
def update(board, n, i, j, l, player):
    board[i][j] = l

    #if l == 1 :
    #    updateScoreS(board,n,i,j,player,lines)
    #elif l == 2:
    #    updateScoreO(board,n,i,j,scores,player,lines)


# Fonction qui retourne le gagnant de la partie
def winner(scores):
    if scores[0] > scores[1]:
        return "Player 1 wins !"
    elif scores[0] == scores[1]:
        return "Egality"
    else :
        return "Player 2 wins !"
