import os
import random
import logging

logging.basicConfig(filename='game.log', level=logging.DEBUG)

# Dungeon game - Treehouse solution

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


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):

    # get player location
    x, y = player
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

    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]

    # Unpacks the Tuple directly into the corresponding vars
    x, y = player

    # if player y == 0, they can not move up (already at top of map)
    if y == 0:
        moves.remove("UP")
    # if player y == 4, they can not move down (already at bottom of map)
    if y == 4:
        moves.remove("DOWN")
    # if player x == 0, they can not move left (already at left edge of map)
    if x == 0:
        moves.remove("LEFT")
    # if player y == 4, they can not move right (already at right edge of map)
    if x == 4:
        moves.remove("RIGHT")

    return moves


def draw_map(player):
    print(" _"*5)
    tile = "|{}"

    for cell in CELLS:
        x, y, = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():

    # get locations returns a Tuple and will unpack directly
    # into the variables
    monster, door, player = get_locations()
    playing = True
    logging.info('monster: {}; player: {}; door: {}'.format(monster, door, player))

    while playing:

        clear_screen()
        draw_map(player)
        available_moves = get_moves(player)

        print("You're currently in room {}".format(player))  # fill w/ player position
        print("You can move {}".format(", ".join(available_moves)))  # fill with available moves
        print("Enter QUIT to quit")

        move = input("> ")
        move = move.upper()

        # debug
        # print("door: {}".format(door))
        # print("monster: {}".format(monster))

        if move == 'QUIT':
            print("\n ** Cool, thanks for playing. **\n")
            break

        # Good move? Change player position
        if move in available_moves:
            # move player
            player = move_player(player, move)

            # On the door? They win.
            if player == door:
                print("\n ** You found the door, OMG, HUGE WIN! **\n")
                playing = False
            # On the monster? They lose.
            if player == monster:
                print("\n ** You got eaten you fuck head. **\n")
                playing = False

        # bad move? Don't change anything.
        else:
            input("\n ** Watch out for the god damned wall! ** \n")
    else:
        if input("Play again? [Y, n] ").lower() != "n":
            game_loop()

clear_screen()
print('Welcome to the dungeon!')
input("Press RETURN to begin....")
clear_screen()

game_loop()
