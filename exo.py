#!/usr/bin/python

def setBoard() :
	return {'width': input('Set board with : '), 'height': input('Set board height :')}

def createGameBoard(width, height) :
	gameboard = []
	for i in range(0, height) :
		column = []
		for i in range(0, width) :
			column.append(True)
		gameboard.append(column)
	return gameboard

def printBoard(board) :
	for row in board :
		printedRow = ''
		for value in row :
			printedRow += ' o ' if value else ' x '
		print(printedRow)

def getNextMove(width, height) :
	x = input('Where to put on x axis (0 >= y < %d)' % (width))

	if x < 0 or x > width:
		getNextMove(width, height)

	y = input('Where to put on y axis (0 >= y < %d)' % (height))

	if y < 0 or x > height:
		getNextMove(width, height)

	return {'x' : x, 'y' : y}

def isInGameboard(x, y, gameboard) :
	return x >= 0 and x < len(gameboard[0]) and y >= 0 and y < len(gameboard)

def switchBoardValue (x, y, gameboard) :
	neighbors = [-1, 0, 1]
	for neighborXDif in neighbors :
		xToTest = x + neighborXDif
		for neighborYDif in neighbors :
			yToTest = y + neighborYDif
			print (neighborXDif)
			print (neighborYDif)
			if isInGameboard(xToTest, yToTest, gameboard) :
				gameboard[yToTest][xToTest] = False if gameboard[yToTest][xToTest] else True
	return gameboard

boardConfig = setBoard()
gameboard = createGameBoard(boardConfig['width'], boardConfig['height'])
printBoard(gameboard)
myMove = getNextMove(boardConfig['width'], boardConfig['height'])
gameboard = switchBoardValue(myMove['x'], myMove['y'], gameboard)
printBoard(gameboard)