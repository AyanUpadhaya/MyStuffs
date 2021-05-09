#Tic-tac-toe Multiplayer Game by Ayan Upadhaya contact: ayanu881@gmail.com
#player one =X
#player two =O

#keyboard moves for players 
#7-top left corner
#8-top middle 
#9-top right corner
#4-left side
#5-middle
#6-right side
#1-bottom left corner
#2-bottom middle
#3-bottom right corner

import random

def game():

	board=[' ']*10

	playerOneLetter='x'.upper()
	playerTwoLetter='o'.upper()

	def drawBoard():
		#first we will print spaces with characters
		print(board[7]+' | '+board[8]+' | '+board[9])
		print('---'+'---'+'---')
		print(board[4]+' | '+board[5]+' | '+board[6])
		print('---'+'---'+'---')
		print(board[1]+' | '+board[2]+' | '+board[3])
		
	def whoGoesfirst():
		#checks to see who goes first
		letter=random.choice(['X','O'])
		if letter=='X':
			return "playerOne"
		return "playerTwo"

	def isSpaceFree(board,move):
		#checks to see if the move spot is free to pass the move on board
		if board[move]==" ":
			return True

	def isPlayerOneWinner(board):
		#first passing the board which is a list to check every possible condition
		#if player one wins return true
		if((board[7]=='X' and board[8]=='X' and board[9]=='X') or #horizontal 
		(board[4]=='X' and board[5]=='X' and board[6]=='X') or 
		(board[1]=='X' and board[2]=='X' and board[3]=='X') or
		(board[7]=='X' and board[4]=='X' and board[1]=='X') or #vertical
		(board[8]=='X' and board[5]=='X' and board[2]=='X') or
		(board[9]=='X' and board[6]=='X' and board[3]=='X') or 
		(board[7]=='X' and board[5]=='X' and board[3]=='X') or #diagonal
		(board[1]=='X' and board[5]=='X' and board[9]=='X')):
			return True

	def isPlayerTwoWinner(board):
		#first passing the board which is a list to check every possible condition
		#if player two wins return true
		if((board[7]=='O' and board[8]=='O' and board[9]=='O') or #horizontal 
		(board[4]=='O' and board[5]=='O' and board[6]=='O') or 
		(board[1]=='O' and board[2]=='O' and board[3]=='O') or
		(board[7]=='O' and board[4]=='O' and board[1]=='O') or #vertical
		(board[8]=='O' and board[5]=='O' and board[2]=='O') or
		(board[9]=='O' and board[6]=='O' and board[3]=='O') or 
		(board[7]=='O' and board[5]=='O' and board[3]=='O') or #diagonal
		(board[1]=='O' and board[5]=='O' and board[9]=='O')):
			return True


	#just draw the board first
	drawBoard()
	print()#for space
	turn=whoGoesfirst()
	print(f'{turn}'+' is going first')
	print()#for space
	
	#thegameloop
	totalmoves=0
	while totalmoves!=9:

		if turn=='playerOne':
			print("Give a move playerone:")
			try:
				moveOne=int(input())
				if moveOne in [1,2,3,4,5,6,7,8,9] and isSpaceFree(board,moveOne):
					board[moveOne]=playerOneLetter
				else:
					continue
			except ValueError:
				continue
			drawBoard()
			turn='playerTwo'
		else:
			print("Give a move playertwo:")
			try:
				moveTwo=int(input())
				if moveTwo in [1,2,3,4,5,6,8,7,9] and isSpaceFree(board,moveTwo):
					board[moveTwo]=playerTwoLetter
				else:
					continue
			except ValueError:
				continue
			drawBoard()
			turn='playerOne'
		
		if isPlayerOneWinner(board):
			print("Player One wins the game")
			break
		if isPlayerTwoWinner(board):
			print("Player two wins the game")
			break

		totalmoves+=1

	if totalmoves==9:
		print("It's a tie")
#mainloop
choice=''
while choice!='n':
	choice=input("Do you want to play a game,y/n?:").lower()
	if choice in ['y','n']:
		if choice=='y':
			game()
	else:
		continue

