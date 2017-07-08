import random

# draw a grid

# pick a random location for player

# pick random location for exit door

# pick random location for monster

# draw player in grid

# take input for movement

# move player, unless move invalid (outside map)

# check for win/loss

# clear screen, redraw grid

# Manually define the 5x5 grid.
CELLS = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
]


def get_locations():

    locations = random.sample(CELLS, 3)

    monster = locations[0]
    door = locations[1]
    player = locations[2]

    # returns a tuple
    return monster, door, player


def move_player(player, move):

    # get player location
    x = player[0]
    y = player[1]
    # if move == LEFT, x-1
    if move == "LEFT":
        x = x - 1
    # if move == RIGHT, x+1
    elif move == "RIGHT":
        x = x + 1
    # if move == UP, y-1
    elif move == "UP":
        y = y - 1
    # if move == DOWN, y+1
    elif move == "DOWN":
        y = y + 1

    player = x, y

    return player


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]

    x = player[0]
    y = player[1]

    # if player y == 0, they can not move up (already at top of map)
    if y == 0:
        moves.remove("UP")
    # if player y == 4, they can not move down (already at bottom of map)
    elif y == 4:
        moves.remove("DOWN")
    # if player x == 0, they can not move left (already at left edge of map)
    elif x == 0:
        moves.remove("LEFT")
    # if player y == 4, they can not move right (already at right edge of map)
    elif x == 4:
        moves.remove("RIGHT")

    return moves


locations = get_locations()

monster = locations[0]
door = locations[1]
player = locations[2]

while True:

    available_moves = get_moves(player)

    print('Welcome to the dungeon!')
    print("You're currently in room {}".format(player))  # fill w/ player position
    print("You can move {}".format(available_moves))  # fill with available moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    print("door: {}".format(door))
    print("monster: {}".format(monster))

    if move == 'QUIT':
        break

    # Good move? Change player position
    if move in available_moves:
        # move player
        new_position = move_player(player, move)
        player = new_position

        # On the door? They win.
        if player == door:
            print("You win!")
            break
        # On the monster? They lose.
        elif player == monster:
            print("You got eaten you fuck head.")
            break

    # bad move? Don't change anything.
    else:
        print("bad move")

    # Otherwise, loop again

