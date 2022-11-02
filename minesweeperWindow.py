from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from minesweeperModel import *
import random
import time

class minesweeperWindow(QMainWindow):
	def __init__(self):
		super(minesweeperWindow, self).__init__()
		
		widget = QWidget()
		self.setCentralWidget(widget)
		
		labelsWidget = QWidget()
		labelLayout = QHBoxLayout(labelsWidget)
		
		label_1 = QLabel(self)
		label_1.setFrameStyle(QFrame.StyledPanel)
		label_1.setText(" Number of mines: 10 ")
		label_1.setAlignment(Qt.AlignCenter)
		
		label_2 = QLabel(self)
		label_2.setFrameStyle(QFrame.StyledPanel)
		label_2.setAlignment(Qt.AlignCenter)
		
		labelLayout.addWidget(label_1)
		labelLayout.addWidget(label_2)
		
		layout = QVBoxLayout()
		layout.addWidget(labelsWidget)
		
		grid = QGridLayout()
		numbers = ['0','1']
		numMines = random.randint(5,10)
		self.buttons = []
		
		for i in range(100):
			button = QPushButton()
			button.setFixedSize(QSize(25,25))
			button.clicked.connect(self.buttonClicked)
			self.buttons.append(button)
			row = i // 10
			col = i % 10
			button.setProperty("myRow", row)
			button.setProperty("myCol", col)
			button.setProperty("clicked", '0')

			grid.addWidget(self.buttons[i], row, col)
		
		grid.setSpacing(0)
		layout.addLayout(grid)
		widget.setLayout(layout)
		self.setWindowTitle("Minesweeper")
		self.model = minesweeperModel()
		self.newGame()
		
	def newGame(self):
		print("starting new game")
		for button in self.buttons:
			button.setEnabled(True)
			button.setProperty("clicked", '0')
			button.setStyleSheet("")
			button.setText("")
		self.model.newGame()
		
	def setSquareColor(self, index, value):
		self.buttons[index].setEnabled(False)		
		if (value == '-1'):
			self.buttons[index].setStyleSheet("background-color : red")
		if (value == '1'):
			self.buttons[index].setStyleSheet("background-color : blue")
		if (value == '2'):
			self.buttons[index].setStyleSheet("background-color : green")
		if (value == '3'):
			self.buttons[index].setStyleSheet("background-color : purple")

	def updateSquare(self, index, row, col):
		squareValue = self.model.reveal(row, col)
		if(self.buttons[index].property("clicked") == '0'):
				self.buttons[index].setProperty("clicked", '1')
				self.buttons[index].setText(squareValue)
				self.setSquareColor(index, squareValue)

	def buttonClicked(self):
		#get clicked button
		#reveal adjacent squares
		#check get state to see if mine was hit
		clicked = self.sender()
		row = clicked.property("myRow")
		col = clicked.property("myCol")

		index = self.buttons.index(clicked)
		self.model.updateClicks()
		print(f"button -{row}- -{col}- was clicked!")
		numClicks = self.model.getMoveCount()
		self.updateSquare(index, row, col)
		print(f"Number of squares clicked: {numClicks}")
		self.checkStatus(row,col)

	def checkStatus(self,row,col):
		#if clicked square was -1 (bomb), restart the game
		if (self.model.getGameState(row, col) == -1):
			print("clicked a mine, restarting game")
			self.newGame()
		
		if (self.model.getGameState(row, col) == 1):
			print("winner! revealed all tiles!")
			self.newGame()
			

