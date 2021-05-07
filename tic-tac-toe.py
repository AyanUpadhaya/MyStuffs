#Tic-tac-toe Man vs Ai game

#keyboard moves player
#7-top left corner
#8-top middle 
#9-top right corner
#4-left side
#5-middle
#6-right
#1-bottom left
#2-bottom middle
#3-bottom right

import random

#we need to draw board first

def drawBoard(board):
	#this function points out the board that it was passed
	#"board" is a list of 10 strings representing the board(ignore index 0)

	print(board[7]+'|'+board[8]+'|'+board[9])
	print('-+-+-')
	print(board[4]+'|'+board[5]+'|'+board[6])
	print('-+-+-')
	print(board[1]+'|'+board[2]+'|'+board[3])
	print('-+-+-')

def inputPlayerLetter():
	#lets the player type which letter they want to be
	#returns a list with player's letter as the first item and the computer's letter as the second

	letter=''
	while not(letter=='X' or letter=='O'):
		print('Do you want to be X or O:')
		letter=input().upper()

	#the first element in the list is player's letter and second one is computer's letter
	if letter=='X':
		return['X','O']
	else:
		return['O','X']

def whoGoesFirst():
	#randomly choices which player goes first

	if random.randint(0,1)==0:
		return 'computer'
	else:
		return 'player'

def makeMove(board,letter,move):
	
	board[move]=letter

def isWinner(bo,le):
	#given a board to check if player wins returns true
	#bo for board and le- letter

	return((bo[7]==le and bo[8]==le and bo[9]==le) or #accross top
	(bo[4]==le and bo[5]==le and bo[6]==le) or #Across the middle
	(bo[1]==le and bo[2]==le and bo[3]==le) or #Across the bottom
	(bo[7]==le and bo[4]==le and bo[1]==le) or #Across left side
	(bo[8]==le and bo[5]==le and bo[2]==le) or #Across the middle
	(bo[9]==le and bo[6]==le and bo[3]==le) or #Across the right side
	(bo[7]==le and bo[5]==le and bo[3]==le) or #Across the diagonal
	(bo[9]==le and bo[5]==le and bo[1]==le ))#Diagonal

def getBoardCopy(board):
	#make a copy of the board list and return it

	boardCopy=[]
	for i in board:
		boardCopy.append(i)
	return boardCopy

def isSpaceFree(board,move):
	#return True if the passed move is free on the passed board
	return board[move]==' '

def getPlayerMove(board):
	#let the player enter their move
	move=' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
		print('What is your next move?(1-9)')
		move=input()
	return int(move)
def chooseRandomMovesFromList(board,movesList):
	#returns a valid move from movesList
	#returns none if there is no valid moves

	possibleMoves=[]
	for i in movesList:
		if isSpaceFree(board,i):
		    possibleMoves.append(i)

	if len(possibleMoves)!=0:
		return random.choice(possibleMoves)
	else:
		return None

def getComputersMove(board,computerLetter):
	#given a board and the computer's letter,determine where to move
	#and return that move
	if computerLetter=='X':
		playerletter='O'
	else:
		playerletter='X'
	#here is the algorithm for our Tic-Tac-Toe Ai:
	#first check if we can win in the next move

	for i in range(1,10):
		boardCopy=getBoardCopy(board)
		if isSpaceFree(boardCopy,i):
		    makeMove(boardCopy,computerLetter,i)
		    if isWinner(boardCopy,computerLetter):
		    	return i
	#check if the player could win on their next move and block them
	for i in range(1,10):
		boardCopy=getBoardCopy(board)
		if isSpaceFree(boardCopy,i):
			makeMove(boardCopy,playerletter,i)
			if isWinner(boardCopy,playerletter):
				return i
	#try to take one of the corner if they are free
	move=chooseRandomMovesFromList(board,[1,3,7,9])

	if move!=None:
		return move

	#try to take the center if it is free.

	if isSpaceFree(board,5):
		return 5

	#move on one of the sides

	return chooseRandomMovesFromList(board,[2,4,6,8])

def isBoardFull(board):
	#return true if every space on the board has been taken
	#else return false

	for i in range(1,10):
		if isSpaceFree(board,i):
			return False

	return True





print("Welcome to tic tac toe:")

#mainloop
while True:
	#reset the board
	theBoard=[' ']*10
	playerletter,computerLetter=inputPlayerLetter()
	turn=whoGoesFirst()


	print('The '+turn+'will go first.')

	gameIsPlaying=True

	while gameIsPlaying:
		if turn=="player":
			#player's turn
			drawBoard(theBoard)
			move=getPlayerMove(theBoard)
			makeMove(theBoard,playerletter,move)

			if isWinner(theBoard,playerletter):
				drawBoard(theBoard)
				print("Hurray you have won the game")
				break
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print("The game is a tie")
					break
				else:
					turn="computer"
		else:
			#computer's turn
			move=getComputersMove(theBoard,computerLetter)
			makeMove(theBoard,computerLetter,move)

			if isWinner(theBoard,computerLetter):
				drawBoard(theBoard)
				print("The computer has beaten you")
				break
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('The Game is a tie')
					break
				else:
					turn='player'

	print("Do you want to play again(yes or no)")
	if not input().lower().startswith('y'):
		break
