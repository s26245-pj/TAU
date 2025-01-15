import random

class InvalidMove(Exception):
    pass

class GridGame:
    def __init__(self, height=5, width=5):
        self.height = height
        self.width = width
        self.grid = [['.' for _ in range(width)] for _ in range(height)]
        self.entry = None
        self.exit = None
        self.setup_entry_and_exit()
        self.add_barriers()

    def setup_entry_and_exit(self):
        boundaries = [(i, 0) for i in range(self.height)] + \
                     [(i, self.width - 1) for i in range(self.height)] + \
                     [(0, j) for j in range(self.width)] + \
                     [(self.height - 1, j) for j in range(self.width)]

        self.entry = random.choice(boundaries)
        boundaries.remove(self.entry)

        self.exit = random.choice(boundaries)
        while abs(self.entry[0] - self.exit[0]) <= 1 and abs(self.entry[1] - self.exit[1]) <= 1:
            self.exit = random.choice(boundaries)

        self.grid[self.entry[0]][self.entry[1]] = 'E'
        self.grid[self.exit[0]][self.exit[1]] = 'X'

    def add_barriers(self, count=5):
        placed = 0
        while placed < count:
            row, col = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if self.grid[row][col] == '.':
                self.grid[row][col] = '#'
                placed += 1

    def show_grid(self):
        for line in self.grid:
            print(" ".join(line))
        print()

    def validate_move(self, row, col):
        if not (0 <= row < self.height and 0 <= col < self.width):
            raise InvalidMove(f"Position ({row}, {col}) is out of bounds.")
        if self.grid[row][col] == '#':
            raise InvalidMove(f"Position ({row}, {col}) is blocked by a barrier.")
        if self.grid[row][col] in ('E', 'X'):
            raise InvalidMove(f"Position ({row}, {col}) is restricted (entry/exit).")
        return True

    def make_move(self, location, direction):
        row, col = location
        directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        if direction in directions:
            dr, dc = directions[direction]
            new_row, new_col = row + dr, col + dc
            if self.validate_move(new_row, new_col):
                return new_row, new_col
        return row, col


game = GridGame(6, 6)
game.show_grid()

current_pos = game.entry
print(f"Entry point: {current_pos}")

for move in ["right", "down", "left", "up"]:
    print(f"Attempting move: {move}")
    try:
        new_pos = game.make_move(current_pos, move)
        print(f"Moved {move} to: {new_pos}")
        current_pos = new_pos
    except InvalidMove as error:
        print(error)
