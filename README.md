	- Soutenance orale de 20 mins (par groupe de 2)
		○ Montrer le bon fonctionnement du projet
		○ Préparer un ppt
			§ Expliquer les points du code les plus importants
			§ Pas à envoyer à l'examinateur avant la soutenance
		
	- Nom du fichier "algo" = sosAlgorithms.py
	- Nom du fichier "graphique" = sosGUI.py
	
	- Règles :
		○ Plateau 
			§ n lignes/colonnes (carré)
			§ Initialement => vide
		○ Tour d'un joueur 
			§ Choisir une case vide
			§ Inscrire dedans un S ou un O
			§ Si après la pose de sa lettre => réalisation d'un "SOS"
				□ Score du joueur incrémenté de 1
		○ But
			§ Réaliser des séquences de lettre "SOS" (diagonales, verticales ou horizontales)
			§ Utiliser aussi bien ses lettres que celles de l'adversaire pour se faire
		○ A noter 
			§ Une lettre peut servir dans plusieurs alignements
			§ La pose d'une lettre peut provoquer plusieurs alignements simultanés (chacune d'elle vaudra alors 1 points qui sera ajouté au score du joueur)
		○ Fin du jeu
			§ Quand le plateau est rempli
			§ Le gagnant est le joueur qui a le plus de points
			§ Match nul possible

	- Structure des données :
		○ Plateau => liste à deux dimensions
			§ Case vide = 0
			§ S = 1
			§ O = 2
		○ Joueurs => entier (0 ou 1)
		○ Scores => liste à 2 valeurs

	- Notation des paramètres :
		○ Board = liste à 2 dimensions (chaque valeur => 0, 1 ou 2) qui représente le plateau
		○ N = entier >0 qui est la taille du tableau
		○ Player = entier qui représente le joueur dont c'est le tour
		○ Scores = liste de 2 entiers qui représente le score des deux joueurs
		○ I = entier quelconque
		○ J = entier quelconque
		○ Lines =  liste à 2 dimensions composée de listes de tuples de 2 entiers (ces listes sont les coordonnées de 2 points => extrémités d'une ligne lors d'un alignement)
		○ L = entier (valant 1 ou 2) qui représente un S ou un O
		
	- Sous-Programmes:
		○ newBoard(n) = retourne l'état initial d'un plateau de jeu (de taille n)
		○ possibleSquare(board,n,i,j) = retourne
			§ True si i et j sont les coordonnées d'une case vide
			§ False sinon
		○ updateScoreS(board,n,i,j,scores,player,lines) = suppose que le joueur a posé un S sur la case (i,j) => cherche les alignements de SOS possiblement engendrés => met à jour les listes "lines" et "scores"
		○ updateScoreO(board,n,i,j,scores,player,lines) = suppose que le joueur a posé un O sur la case (i,j) => cherche les alignements de SOS possiblement engendrés => met à jour les listes "lines" et "scores"
		○ update(board,n,i,j,l,scores,player,lines) =
			§ Met à jour le plateau en affectant la valeur l à la case (i,j)
			§ Appelle updateScoreS ou updateScoreO (en fonction de la valeur de l)
			§ NB : à l'appel de cette procédure, lines est vide
		○ winner(scores) = retourne une chaine de caractère indiquant le résultat de la partie

	- Interface graphique => forcément Pygame
		○ Garder des traces de qui a réalisé quel alignement (code couleur par exemple)
		○ Chaque lettre posée par le joueur est de "sa" couleur
		○ mySurface = surface sur laquelle on dessine
		○ Graphisme libre
		○ Que des évènements à la souris
		○ Flèche à droite du score qui indique à qui le tour
		○ Chaque case vide = divisée en 2
			§ Clique à gauche => S
			§ Clique à droite => O
		○ A la pose d'un lettre => ne pas redessiner tout le tableau, juste faire les changements nécessaires
		○ Affichage du gagnant du type "Reds win !" sans effacer les scores et le plateau

	- Sous-programmes (graphisme):
		○ drawBoard(mySurface) = dessine le plateau initial
		○ displayScore(mySurface,n,scores) = affiche les scores des joueurs
		○ displayPlayer(mySurface,n,player) = place la flèche à côté du score du joueur dont c'est le tour
		○ drawCell(mySurface,board,i,j,player) = dessine le contenue de la case (i,j) de la couleur du joueur dont c'est le tour
		○ drawLines(mySurface,lines,player) = dessine les lignes pour tous les alignements contenus dans "lines"
		○ displayWinner(mySurface,n,scores) = affiche le gagnant
		○ selectSquare(mySurface,board,n) = permet de choisir une case et une lettre, retourne un tuple (i,j,l) (coordonnées de la case et valeur à assigner)
		○ gamePlay(mySurface,board,n,scores) = gère une partie complète
		○ SOS(n) = créer une fenetre, initialise les structures de données et gère une partie complète


	- Barème :
		○ Soutenance = 20 pts
		○ Graphisme = 25 pts
		○ Algo = 15 pts
		○ Bonus = 10 pts
		
			
			
