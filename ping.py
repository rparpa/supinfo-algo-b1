#!/usr/bin/python3

_board_config = {'width': 0, 'height': 0}
_game_board = []
_print_rules = []

# COMMON FUNCTIONS


def create_game_board(width, height, value):
    """
    Create the game board nested listed with the given width & height
    :param width:  int
    :param height: int
    :param value:  boolean
    :return: list
    """
    return [[value] * width for i in range(height)]


def set_board():
    """
    Prompt the user to set the width and height of the board
    :return: dictionary
    """
    width = int(input('Set board width : '))
    height = int(input('Set board height : '))

    return {'width': width, 'height': height}


def is_in_game_board(x, y, game_board):
    """
    Check if the given coordinates are in the game board
    :param x:           int
    :param y:           int
    :param game_board:  list
    :return: list
    """
    return 0 <= x < len(game_board[0]) and 0 <= y < len(game_board)


def get_user_wish():
    """
    Prompt the user to know if he wants to continue.
    Flame him if he quits.
    :return: boolean
    """
    user_wish = str(input('Do you want to continue y or n: '))
    if user_wish == "y":
        return True
    elif user_wish == "n":
        print('Sacre Hubert, toujours le mot pour rire')
        return False
    else:
        return get_user_wish()


def print_board(board):
    """
    Pretty print the gameboard
    The _print_rules global corresponds to the format of the board (which character represent True/False values).
    The first value of the list is the False value representation, the second is the True value representation.
    :param board: list
    :return: none
    """
    global _print_rules
    for row in board:
        printed_row = ''
        for value in row:
            printed_row += ' ' + _print_rules[int(value)] + ' '
        print(printed_row)


def tile_neighbors(x, y, game_board):
    """
    Generate the neighbors positions for the given coordinates on the game board
    The neighbors are all the combinations (-1 + x, -1 + y), (-1 + x, 0 + y), (-1 + x, 1 + y)... next to (x, y)
    coordinates.
    :param x: int
    :param y: int
    :param game_board: list
    :return: dictionary
    """
    for neighborXDif in range(-1, 2):
        for neighborYDif in range(-1, 2):
            is_current_tile = neighborXDif == 0 and neighborYDif == 0
            if not is_current_tile and is_in_game_board(x + neighborXDif, y + neighborYDif, game_board):
                yield {'x': x + neighborXDif, 'y': y + neighborYDif}


# PONG GAME

def set_pong():
    """
    Set pong game
    :return: none
    """
    global _board_config, _game_board, _print_rules
    _board_config = set_board()
    _game_board = create_game_board(_board_config['width'], _board_config['height'], False)
    _print_rules = ['.', '*']


def place_one_star(game_board):
    """
    Place one star. Take the gameboard as parameter, and ask for user input for star coordinates.
    :param game_board: list
    :return: list
    """
    x = int(input('Where do you want to put the star on x axis ? : '))
    y = int(input('Where do you want to put the star on y axis ? : '))
    if is_in_game_board(x, y, game_board):
        game_board[y][x] = True
        print_board(game_board)
    else:
        print('Coordinates are not valid')
        return place_one_star(game_board)
    return game_board


def place_stars(game_board):
    """
    Place a star on the board at the given coordinates.
    :param game_board: list
    :return: list
    """
    number_of_stars = int(input('How many star do you want to place ? : '))
    for i in range(number_of_stars):
        game_board = place_one_star(game_board)
    return game_board


def is_star(x, y, game_board):
    """
    Return true if the tile is a star (star are mapped with True value in the game)
    :param x: int
    :param y: int
    :param game_board: list
    :return: boolean
    """
    return game_board[x][y]


def has_impair_number_of_stars(x, y, game_board):
    """
    Check all the neighbors if they are star. Increment numberOfNeighborsStars if they are.
    Return true if there is an impair number of neighbors, false otherwise.
    :param x:          int
    :param y:          int
    :param game_board: list
    :return: boolean
    """
    number_of_neighbors_stars = 0
    for neighbor in tile_neighbors(x, y, game_board):
        if is_star(neighbor['x'], neighbor['y'], game_board):
            number_of_neighbors_stars += 1
    # odd bitwise AND 1 returns true, false if even
    return number_of_neighbors_stars & 1


def is_pong_game_won(game_board):
    """
    Check all value of the gameboard, and check if there is an impair number of stars next to it.
    :param game_board: list
    :return: boolean
    """
    for y in range(len(game_board)):
        for x in range(len(game_board[0])):
            if not has_impair_number_of_stars(x, y, game_board):
                print('Nop, sorry')
                return False
    print('You rules')
    return True


def play_pong():
    """
    Play the game.
    Recursive function, calling itself if the player continue and didn't win
    :return: none
    """
    global _game_board
    print_board(_game_board)
    _game_board = place_stars(_game_board)
    if is_pong_game_won(_game_board) or not get_user_wish():
        return
    else:
        set_pong()
        play_pong()


# PING FUNCTIONS


def get_next_move():
    """
    Prompt the user to get his next move
    :return: dictionary
    """
    global _game_board
    global _board_config
    x = int(input('Where to put on x axis (0 >= x < %d)' % _board_config['width']))
    y = int(input('Where to put on y axis (0 >= y < %d)' % _board_config['height']))
    if not is_in_game_board(x, y, _game_board):
        print('Not in game board')
        return get_next_move()

    return {'x': x, 'y': y}


def switch_board_value(x, y, game_board):
    """
    Switch a board value. When a value is switched, all its neighbor values are switched also
    (but not the value itself).
    :param x:         int
    :param y:         int
    :param game_board: list
    :return: list
    """
    for neighbor in tile_neighbors(x, y, game_board):
        game_board[neighbor['y']][neighbor['x']] = not game_board[neighbor['y']][neighbor['x']]

    return game_board


def is_game_won(game_board):
    """
    Check if the game is won. The game is won when all the values are equals to True.
    :param game_board: list
    :return: boolean
    """
    for row in game_board:
        for value in row:
            if value:
                print('Still much to do')
                return False
    print('You won the game.')
    return True


def set_ping():
    """
    Prompt the user to set the game config.
    The config is persisted in global variables.
    :return: none
    """
    global _board_config, _game_board, _print_rules
    _board_config = set_board()
    _game_board = create_game_board(_board_config['width'], _board_config['height'], True)
    _print_rules = ['x', 'o']


def play_ping():
    """
    Play the game.
    Recursive function, calling itself if the player continue and didn't win
    :return: none
    """
    global _game_board
    print_board(_game_board)
    user_move = get_next_move()
    _game_board = switch_board_value(user_move['x'], user_move['y'], _game_board)
    print_board(_game_board)
    if is_game_won(_game_board) or not get_user_wish():
        return
    else:
        play_ping()

print('Good evening, infideeeeel')
gameChoice = int(input('Wich game do you want to play ? 1 : ping, 2 : pong (the one with no name)'))
if gameChoice == 1:
    set_ping()
    play_ping()
else:
    set_pong()
    play_pong()
