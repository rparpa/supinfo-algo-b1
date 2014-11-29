#!/usr/bin/python

def setBoard() :
	""" Prompt the user to set the width and height of the board
	setBoard() -> {'width': int, 'height': int}
	"""
	width = input('Set board width : ')
	if (isinstance(width, int) == False) :
		setBoard()
	height = input('Set board height : ')
	if (isinstance(height, int) == False) :
		setBoard()

	return {'width': width, 'height': height}

def createGameBoard(width, height) :
	""" Create the gameboard nested listed with the given width & height
	createGameBoard(int, int) -> [][]
	"""	
	gameboard = []
	for i in range(0, height) :
		column = []
		for i in range(0, width) :
			column.append(True)
		gameboard.append(column)

	return gameboard

def printBoard(board) :
	""" Pretty print the gameboard
	printBoard([][]) -> 
	"""
	for row in board :
		printedRow = ''
		for value in row :
			printedRow += ' o ' if value else ' x '
		print(printedRow)

def getNextMove(width, height) :
	""" Prompt the user to get his next move
	getNextMove(int, int) -> {'x' => int, 'y' => int}
	"""
	x = input('Where to put on x axis (0 >= y < %d)' % (width))
	if x < 0 or x > width or isinstance(x, int) == False:
		getNextMove(width, height)
	y = input('Where to put on y axis (0 >= y < %d)' % (height))
	if y < 0 or x > height or isinstance(y, int) == False:
		getNextMove(width, height)

	return {'x' : x, 'y' : y}

def isInGameboard(x, y, gameboard) :
	""" Check if the given coordinates are in the gameboard
	isInGameboard(int, int, [][]) -> Boolean
	"""
	return x >= 0 and x < len(gameboard[0]) and y >= 0 and y < len(gameboard)

def switchBoardValue(x, y, gameboard) :
	""" Switch a board value. When a value is switched, all its neighbor values are switched also.
	The neighbors are all the combinaisons (-1 + x, -1 + y), (-1 + x, 0 + y), (-1 + x, 1 + y)... next to (x, y) coordinates.
	switchBoardValue(int, int, [][]) -> [][]
	""" 
	neighbors = [-1, 0, 1]
	for neighborXDif in neighbors :
		xToTest = x + neighborXDif
		for neighborYDif in neighbors :
			yToTest = y + neighborYDif
			if isInGameboard(xToTest, yToTest, gameboard) :
				gameboard[yToTest][xToTest] = False if gameboard[yToTest][xToTest] else True
	return gameboard

def isGameWon(gameboard) :
	""" Check if the game is won. The game is won when all the values are equals to True
	isGameWon([][]) -> Boolean
	"""
	for row in gameboard :
		for value in row :
			if value != True :
				return False
	return True

def getUserWish() :
	""" Prompt the user to know if he wants to continue.
	Flame him if he quits.
	getUserWish() -> Boolean
	"""
	userWish = raw_input('Do you want to continue y or n: ')
	if userWish == "y" :
		return True
	elif userWish == "n" :
		print('Sacre Hubert, toujours le mot pour rire')
		return False
	else :
		return getUserWish()


boardConfig = setBoard()
gameboard = createGameBoard(boardConfig['width'], boardConfig['height'])
printBoard(gameboard)
myMove = getNextMove(boardConfig['width'], boardConfig['height'])
gameboard = switchBoardValue(myMove['x'], myMove['y'], gameboard)
printBoard(gameboard)

print(isGameWon(gameboard))
getUserWish()
