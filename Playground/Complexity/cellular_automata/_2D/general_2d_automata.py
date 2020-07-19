from random import choices
from collections import defaultdict
from Playground.Complexity.cellular_automata.utils.utils import RoundList, default_dict

game_of_live_rules = {
    (0, 3): 1,
    (1, 3): 1,
    (1, 2): 1
}
game_of_live_rules = defaultdict(lambda: 0, game_of_live_rules)


def generate_snowflake_rule(neighbours_numbers: list):
    snowflake_rules = default_dict(lambda self, key: key[0])
    for neighbours_number in neighbours_numbers:
        snowflake_rules[(0, neighbours_number)] = 1
        snowflake_rules[(1, neighbours_number)] = 1
    return snowflake_rules


def generate_grid(width: int, height: int, probability_of_one: float) -> list:
    probability_of_zero = 1 - probability_of_one
    return RoundList(
        [RoundList([choices([0, 1], [probability_of_zero, probability_of_one])[0] for _ in range(width)]) for _ in
         range(height)])


def generate_grid_one_cell(width: int, height: int) -> list:
    grid = RoundList([RoundList([0 for _ in range(width)]) for _ in range(height)])
    grid[width // 2][height // 2] = 1
    return grid


def count_colored_neighbours(x: int, y: int, grid: list):
    colored_neighbours = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if grid[i][j] == 1 and (i, j) != (x, y): colored_neighbours += 1
    return colored_neighbours


def update_grid(grid: list, rules: defaultdict = game_of_live_rules):
    new_grid = RoundList([RoundList([value for value in row]) for row in grid])
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            state = cell
            live_neighbours = count_colored_neighbours(i, j, grid)
            new_grid[i][j] = rules[(state, live_neighbours)]
    return new_grid


if __name__ == "__main__":
    grid = generate_grid(5, 5, 0.7)
    for row in grid:
        print(row)
    print("*" * 10)
    grid = update_grid(grid, rules=snowflake_rules)
    for row in grid:
        print(row)
