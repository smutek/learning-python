TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for tile in TILES:

    if tile == "||":
        print("", end="\n")
    else:
        print(tile, end="")
