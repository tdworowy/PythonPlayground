from random import choices
from collections import defaultdict

from Playground.Complexity.cellular_automata.utils.utils import RoundList

ant_symbol = 2

rules = {
    (0, 3): 1,
    (1, 3): 1,
    (1, 2): 1
}
rules = defaultdict(lambda: 0, rules)


def generate_grid(width: int, height: int, probability_of_one: float) -> list:
    probability_of_zero = 1 - probability_of_one
    return RoundList(
        [RoundList([choices([0, 1], [probability_of_zero, probability_of_one])[0] for _ in range(width)]) for _ in
         range(height)])


def count_live_neighbours(x: int, y: int, grid: list):
    live_neighbours = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if grid[i][j] == 1 and (i, j) != (x, y): live_neighbours += 1
    return live_neighbours


def update_grid(grid: list):
    new_grid = RoundList([RoundList([value for value in row]) for row in grid])
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            state = cell
            live_neighbours = count_live_neighbours(i, j, grid)
            new_grid[i][j] = rules[(state, live_neighbours)]
    return new_grid


if __name__ == "__main__":
    grid = generate_grid(5, 5, 0.7)
    for row in grid:
        print(row)
    print("*" * 10)
    grid = update_grid(grid)
    for row in grid:
        print(row)
