grid_size = 8
start = "@"
jewel = "+"
wall = "#"
bomb = "*"
stop = "O"
free = "-"

directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


class Tile:
    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y
        self.paths = []

class Path:
    def __init__(self):
        passing_tiles = []

def print_grid():
    print()
    for y in range(grid_size):
        for x in range(grid_size):
            print(grid[x][y].value, end="")
        print()
    print()


#Initalize and fill grid
#grid= [[]] * 8 only creates one list instance. Good to know
grid = [[] for i in range(grid_size)]
for y in range(grid_size):
    line = input()
    for x in range(len(line)):
        grid[x].append(Tile(x, y, line[x]))

#Define possible paths for each tile
def path(start_tile, direction):
    path = []
    v = directions[direction]
    condition = 1
    while condition:

        next_tile = tile(start_tile.x + v[0], start_tile.y + v[1])

        print("Test")

        if not next_tile:
            break

        condition = next_tile.value != wall
        if next_tile.value == bomb:
            return

        path.append(next_tile)
        start_tile = next_tile

    return path

def tile(x, y):
    if x < 0 or x >= grid_size or y < 0 or y >= grid_size:
        return 0
    return grid[x][y]

def add_paths():
    print()
    for y in range(grid_size):
        for x in range(grid_size):
            for d in range(8):
                grid[x][y].paths.append(path(grid[x][y], d))
            print(x, y, "has", len(grid[x][y].paths), "paths")
        print()
    print()


x = 1
y = 6
for d in range(8):
    grid[x][y].paths.append(path(grid[x][y], d))
print(x, y, "has", len(grid[x][y].paths), "paths")

print_grid()









