#!/usr/bin/python

def setBoard() :
	return {'width': input('Set board with : '), 'height': input('Set board height :')}

boardConfig = setBoard()

print(boardConfig['width'])
