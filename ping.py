#!/usr/bin/python

boardConfig = {'width': 0, 'height': 0}
gameboard = []
printRules = []

"""

COMMON FUNCTIONS

"""

def createGameBoard(width, height, value):
    """ Create the gameboard nested listed with the given width & height
    createGameBoard(int, int) -> [][]
    """
    gameboard = []
    for i in range(0, height):
        column = []
        for i in range(0, width):
            column.append(bool(value))
        gameboard.append(column)

    return gameboard


def setBoard():
    """ Prompt the user to set the width and height of the board
    setBoard() -> {'width': int, 'height': int}
    """
    width = int(input('Set board width : '))
    height = int(input('Set board height : '))

    return {'width': width, 'height': height}

def isInGameboard(x, y, gameboard):
    """ Check if the given coordinates are in the gameboard
    isInGameboard(int, int, [][]) -> Boolean
    """
    return 0 <= x < len(gameboard[0]) and 0 <= y < len(gameboard)


def getUserWish():
    """ Prompt the user to know if he wants to continue.
    Flame him if he quits.
    getUserWish() -> Boolean
    """
    userWish = str(input('Do you want to continue y or n: '))
    if userWish == "y":
        return True
    elif userWish == "n":
        print('Sacre Hubert, toujours le mot pour rire')
        return False
    else:
        return getUserWish()

"""

PONG GAME

"""

def setPong():
    """ Set pong game
    setPong() ->
    """
    global boardConfig, gameboard, printRules
    boardConfig = setBoard()
    gameboard = createGameBoard(boardConfig['width'], boardConfig['height'], False)
    printRules = ['.', '*']


def placeOneStar(gameboard):
    """ Place one star. Take the gameboard as parameter, and ask for user input for star coordinates.
    placeOneStar([][]) -> [][]
    """
    x = int(input('Where do you want to put the star on x axis ? : '))
    y = int(input('Where do you want to put the star on y axis ? : '))
    if isInGameboard(x, y, gameboard):
        gameboard[y][x] = True
        printBoard(gameboard)
    else:
        print('Coordinates are not valid')
        placeOneStar(gameboard)
    return gameboard


def placeStars(gameboard):
    numberOfStars = int(input('How many star do you want to place ? : '))
    for i in range(numberOfStars):
        gameboard = placeOneStar(gameboard)
    return gameboard


def hasImpairNumberOfStars(x, y, gameboard):
    """ Check all the neighbors if they are star. Increment numberOfNeighborsStars if they are.
    Return true if there is an impair number of neighbors, false otherwise.
    checkNeighbors(int, int, [][]) -> Boolean
    """
    neighbors = [-1, 0, 1]
    numberOfNeighborsStars = 0
    for neighborXDif in neighbors:
        xToTest = x + neighborXDif
        for neighborYDif in neighbors:
            yToTest = y + neighborYDif
            isCurrentTile = neighborXDif == 0 and neighborYDif == 0
            if isInGameboard(xToTest, yToTest, gameboard) and gameboard[yToTest][xToTest] and not isCurrentTile:
                numberOfNeighborsStars += 1
    return numberOfNeighborsStars & 1


def isPongGameWon(gameboard):
    """ Check all value of the gameboard, and check if there is an impair number of stars next to it.
    isPongGameWon([][]) -> Boolean
    """
    for y in range(len(gameboard)):
        for x in range(len(gameboard[0])):
            if not hasImpairNumberOfStars(x, y, gameboard):
                print('Nop, sorry')
                return False
    print('You rules')
    return True


def playPong():
    """ Play the game.
    Recursive function, calling itself if the player continue and didn't win
    playPing() ->
    """
    global gameboard
    printBoard(gameboard)
    gameboard = placeStars(gameboard)
    if isPongGameWon(gameboard) or not getUserWish():
        return
    else:
        setPong()
        playPong()

"""

PING FUNCTIONS

"""

def printBoard(board):
    """ Pretty print the gameboard
    The rules argument correspond to format of the board (which character represent True/False values).
    The first value of the list is the False value, the second is the True value.
    printBoard([][], []) ->
    """
    global printRules
    for row in board:
        printedRow = ''
        for value in row:
            printedRow += ' ' + printRules[int(value)] + ' '
        print(printedRow)


def getNextMove(width, height):
    """ Prompt the user to get his next move
    getNextMove(int, int) -> {'x' => int, 'y' => int}
    """
    x = int(input('Where to put on x axis (0 >= x < %d)' % width))
    if x < 0 or x > width or not isinstance(x, int):
        getNextMove(width, height)
    y = int(input('Where to put on y axis (0 >= y < %d)' % height))
    if y < 0 or x > height or not isinstance(y, int):
        getNextMove(width, height)

    return {'x': x, 'y': y}

def switchBoardValue(x, y, gameboard):
    """ Switch a board value. When a value is switched, all its neighbor values are switched also
    (but not the value itself).
    The neighbors are all the combinations (-1 + x, -1 + y), (-1 + x, 0 + y), (-1 + x, 1 + y)...
    next to (x, y) coordinates.
    switchBoardValue(int, int, [][]) -> [][]
    """
    neighbors = [-1, 0, 1]
    for neighborXDif in neighbors:
        xToTest = x + neighborXDif
        for neighborYDif in neighbors:
            yToTest = y + neighborYDif
            isCurrentTile = neighborXDif == 0 and neighborYDif == 0
            if isInGameboard(xToTest, yToTest, gameboard) and not isCurrentTile:
                gameboard[yToTest][xToTest] = not gameboard[yToTest][xToTest]
    return gameboard


def isGameWon(gameboard):
    """ Check if the game is won. The game is won when all the values are equals to True
    isGameWon([][]) -> Boolean
    """
    for row in gameboard:
        for value in row:
            if value:
                print('Still much to do')
                return False
    print('You won the game.')
    return True


def setPing():
    """ Prompt the user to set the game config.
    The config is persisted in global variables.
    setPing() ->
    """
    global boardConfig, gameboard, printRules
    boardConfig = setBoard()
    gameboard = createGameBoard(boardConfig['width'], boardConfig['height'], True)
    printRules = ['x', 'o']


def playPing():
    """ Play the game.
    Recursive function, calling itself if the player continue and didn't win
    playPing() ->
    """
    global gameboard
    printBoard(gameboard)
    userMove = getNextMove(boardConfig['width'], boardConfig['height'])
    gameboard = switchBoardValue(userMove['x'], userMove['y'], gameboard)
    printBoard(gameboard)
    if isGameWon(gameboard) or not getUserWish():
        return
    else:
        playPing()

setPing()
playPing()