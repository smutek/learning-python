# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)


def move(player, direction):
    x, y, hp = player
    a, b = direction

    # see if we are running into a wall
    if x + a == -1 or x + a == 10 or y + b == -1 or y + b == 10:
        # if yes, don't move player, decrease hp
        x, y, hp = x, y, hp - 5
    else:
        # otherwise move the player
        x, y, hp = x + a, y + b, hp

    return x, y, hp

print(move((1, 1, 10), (-1, 0)))
print(move((0, 1, 10), (-1, 0)))
print(move((0, 9, 5), (0, 1)))
