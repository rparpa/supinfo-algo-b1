#!/usr/bin/python

def setBoard() :
	return {'width': input('Set board with : '), 'height': input('Set board height :')}

boardConfig = setBoard()

def createGameBoard(width, height) :
	gameboard = [];
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
	x = input('Where to put on x axis (between 0 and %d)' % (width))

	if x < 0 or x > width:
		getNextMove(width, height)

	y = input('Where to put on y axis (between 0 and %d)' % (height))

	if y < 0 or x > height:
		getNextMove(width, height)

getNextMove(4, 5)