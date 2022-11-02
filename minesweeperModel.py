import random

class minesweeperModel:
	def __init__(self):
		self.newGame()
		
	def newGame(self):
		# set mines on board and reset variables
		# -1 means bomb
		self.gameStatus = 0
		self.numClicks = 0
		rows, cols = (10,10)
		self.board = [[0]*(cols) for i in range(rows)]
		self.clicked = [[0]*(cols) for i in range(rows)]
		numMines = 10
		while numMines > 0:
			x = random.randint(0,9)
			y = random.randint(0,9)
			if (self.board[x][y] != -1):
				self.board[x][y] = -1
				numMines -= 1
				#set adjacent tile values
				
				#(x row,y column)
				#top left (r-,c-)
				if (x-1 >= 0 and y-1 >= 0):
					if (self.board[x-1][y-1] != -1):
						self.board[x-1][y-1] += 1
				#top middle (r-,c)
				if (x-1 >= 0):
					if(self.board[x-1][y]!= -1):
						self.board[x-1][y] += 1
				#top right (r-,c+)
				if (x-1 >= 0 and y+1 < len(self.board[0])):
					if(self.board[x-1][y+1] != -1):
						self.board[x-1][y+1] += 1
				#left(r,c-)
				if (y-1 >= 0):
					if(self.board[x][y-1] != -1):
						self.board[x][y-1] += 1
				#right (r,c+)
				if (y+1 < len(self.board[0])):
					if(self.board[x][y+1] != -1):
						self.board[x][y+1] += 1
				#bottom left (r+,c-)
				if (x+1 < len(self.board) and y-1 >= 0):
					if(self.board[x+1][y-1]!= -1):
						self.board[x+1][y-1] += 1
				#bottom middle (r+,c)
				if (x+1 < len(self.board)):
					if(self.board[x+1][y]!= -1):
						self.board[x+1][y] += 1
				#bottom right (r+,c+)
				if (x+1 < len(self.board) and y+1 < len(self.board[0])):
					if(self.board[x+1][y+1]!= -1):
						self.board[x+1][y+1] += 1
				
	def updateClicks(self):
		self.numClicks += 1

	def reveal(self, row, col):
		#reveal the square
		return str(self.board[row][col])
	
	def getSquare(self, row, col):
		#get state based off clicked square
		#clicked all possible squares
		if (self.numClicks == 90):
			self.gameStatus = 1
		#clicked a bomb square
		currentSquare = self.board[row][col]
		if (currentSquare == -1):
			self.gameStatus = -1

	def getMoveCount(self):
		#return moveCount value
		return str(self.numClicks)

	def getGameState(self, row, col):
		#-1 loss
		# 0 in progress
		# 1 win
		self.getSquare(row,col)
		if (self.gameStatus == -1):
			return -1
		if (self.gameStatus == 1):
			return 1
		return 0
			
			

		

