# 2e projet de Python - SOS GAME (Groupe de 2)
# Anaïs Depeau et Camille Lamoureux
# Bibliothèque des fonctions algorithmiques permettant le jeu

# Fonction de création d'un nouveau tableau
def newboard(n):
    board = []
    for ligne in range(n):
        board.append(n *[0])
    return board


# Fonction qui check si la case sélectionnée par le joueur est correcte
#def possibleSquare(board,n,i,j):


# Procédure qui met à jour lines et scores si on a posé un S
#def updateScoreS(board,n,i,j,scores,player,lines):


# Procédure qui met à jour lines et scores si on a posé un O
#def updateScoreO(board,n,i,j,scores,player,lines):


# Prodécudre qui met à jour le plateau de jeu
#def update(board,n,i,j,l,scores,player,lines):


# Fonction qui retourne le gagnant de la partie
def winner(scores):
    return "Le joueur 1 à gagné" if scores[0] > scores[1] else "Le joueur 2 à gagné"