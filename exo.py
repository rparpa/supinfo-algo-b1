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

printBoard(createGameBoard(boardConfig['width'], boardConfig['height']))