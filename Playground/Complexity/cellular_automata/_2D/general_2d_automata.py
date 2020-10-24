from random import choices
from collections import defaultdict
from Playground.Complexity.cellular_automata.utils.utils import RoundList, default_dict

game_of_live_rules = {
    (0, 3): 1,
    (1, 3): 1,
    (1, 2): 1
}
game_of_live_rules = defaultdict(lambda: 0, game_of_live_rules)

amoeba_rules = {
    (0, 3): 1,
    (0, 5): 1,
    (0, 7): 1,
    (1, 1): 1,
    (1, 3): 1,
    (1, 5): 1,
    (1, 8): 1
}
amoeba_rules = defaultdict(lambda: 0, amoeba_rules)

_2x2_rules = {
    (0, 3): 1,
    (0, 6): 1,
    (1, 1): 1,
    (1, 2): 1,
    (1, 5): 1,
}
_2x2_rules = defaultdict(lambda: 0, _2x2_rules)

_34_live_rules = {
    (0, 3): 1,
    (0, 4): 1,
    (1, 3): 1,
    (1, 4): 1,
}
_34_live_rules = defaultdict(lambda: 0, _34_live_rules)

coagulations_rules = {
    (0, 3): 1,
    (0, 7): 1,
    (0, 8): 1,
    (1, 2): 1,
    (1, 3): 1,
    (1, 5): 1,
    (1, 6): 1,
    (1, 7): 1,
    (1, 8): 1,
}
coagulations_rules = defaultdict(lambda: 0, coagulations_rules)

mazectric_rules = {
    (0, 3): 1,
    (1, 1): 1,
    (1, 2): 1,
    (1, 3): 1,
    (1, 4): 1,
}
mazectric_rules = defaultdict(lambda: 0, mazectric_rules)

move_rules = {
    (0, 3): 1,
    (0, 6): 1,
    (0, 8): 1,
    (1, 2): 1,
    (1, 4): 1,
    (1, 5): 1,
}
move_rules = defaultdict(lambda: 0, move_rules)

walled_cities_rules = {
    (0, 4): 1,
    (0, 5): 1,
    (0, 6): 1,
    (0, 7): 1,
    (0, 8): 1,

    (1, 2): 1,
    (1, 3): 1,
    (1, 4): 1,
    (1, 5): 1,
}
walled_cities_rules = defaultdict(lambda: 0, walled_cities_rules)


def generate_snowflake_rule(neighbours_numbers: list):
    snowflake_rules = default_dict(lambda self, key: key[0])

    for neighbours_number in neighbours_numbers:
        snowflake_rules[(0, neighbours_number)] = 1
        snowflake_rules[(1, neighbours_number)] = 1

    return snowflake_rules


def generate_grid_random_cells(width: int, height: int, probability_of_one: float) -> list:
    probability_of_zero = 1 - probability_of_one
    return RoundList(
        [RoundList([choices([0, 1], [probability_of_zero, probability_of_one])[0] for _ in range(width)])
         for _ in range(height)])


def generate_grid_one_cell(width: int, height: int) -> list:
    grid = RoundList([RoundList([0 for _ in range(width)]) for _ in range(height)])
    grid[width // 2][height // 2] = 1
    return grid


def generate_grid_central(width: int, height: int, cell_count: int = 1) -> list:
    if cell_count == 1: return generate_grid_one_cell(width, height)
    grid = RoundList([RoundList([0 for _ in range(width)]) for _ in range(height)])
    x = width // 2
    y = height // 2
    for i in range(cell_count // 2):
        for j in range(cell_count // 2):
            grid[x + i][y + j] = 1
    return grid


def count_colored_neighbours(x: int, y: int, grid: list):
    colored_neighbours = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if grid[i][j] == 1 and (i, j) != (x, y): colored_neighbours += 1
    return colored_neighbours


def update_grid(grid: list, rules: defaultdict):
    new_grid = RoundList([RoundList([value for value in row]) for row in grid])
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            state = cell
            live_neighbours = count_colored_neighbours(i, j, grid)
            new_grid[i][j] = rules[(state, live_neighbours)]
    return new_grid


if __name__ == "__main__":
    grid = generate_grid_random_cells(1000, 1000, 0.7)
    for i in range(100):
        print(i)
        grid = update_grid(grid, game_of_live_rules)
