#!/usr/bin/python

def setBoard() :
	return {'width': input('Set board with : '), 'height': input('Set board height :')}

boardConfig = setBoard()

def createGameBoard(width, height) :
	gameboard = [];
	for i in range(0, width) :
		column = []
		for i in range(0, height) :
			column.append(True)
		gameboard.append(column)
	return gameboard

print(createGameBoard(boardConfig['width'], boardConfig['height']))