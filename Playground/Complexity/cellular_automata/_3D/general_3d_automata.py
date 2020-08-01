import itertools
from collections import defaultdict
from random import shuffle, choice


def random_rule(min_to_born=1):
    rule_a = {(i, 0): choice([0, 1]) for i in range(27)}
    rule_b = {(i, 1): choice([0, 1]) for i in range(27)}

    rule = {**rule_a, **rule_b}

    rule[(min_to_born, 0)] = 1

    return rule


rule_1 = {
    (1, 0): 1,
    (1, 3): 1,
    (1, 2): 1
}
rule_1 = defaultdict(lambda: 0, rule_1)


def count_neighbours(cords: tuple, grid: dict):
    neighbours = 0
    x, y, z = cords[0], cords[1], cords[2]
    try:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                for k in range(z - 1, z + 2):
                    if grid[(i, j, k)] == 1 and (i, j, k) != (x, y, z): neighbours += 1
    except KeyError:
        pass
    return neighbours


def generate_random_grid(cell_range=(-20, 20)):
    grid = [x for x in range(*cell_range)]
    grid = list(itertools.product(grid, repeat=3))
    shuffle(grid)
    return {cords: choice([0, 1]) for cords in grid}


def generate_grid_center_cell_start(cell_range=(-20, 20)):
    grid = [x for x in range(*cell_range)]
    grid = list(itertools.product(grid, repeat=3))
    return {cords: 1 if cords == (0, 0, 0) else 0 for cords in grid}


def update_grid(grid: dict, rules: dict):
    new_grid = {}
    for key in grid:
        neighbours = count_neighbours(key, grid)
        state = grid[key]
        new_grid[key] = rules[(neighbours, state)]
    return new_grid
