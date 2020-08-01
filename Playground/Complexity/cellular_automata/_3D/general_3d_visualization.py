from vpython import box, vector, color

from Playground.Complexity.cellular_automata._3D.general_3d_automata import generate_grid_center_cell_start, \
    random_rule, update_grid, rule_1
from time import sleep


def generate_stage():
    side = 40
    thk = 0.1
    s2 = 2 * side - thk
    s3 = 2 * side + thk

    wall_r = box(pos=vector(side, 0, 0), size=vector(thk, s2, s3), color=color.blue)
    wall_l = box(pos=vector(-side, 0, 0), size=vector(thk, s2, s3), color=color.blue)
    wall_g = box(pos=vector(0, -side, 0), size=vector(s3, thk, s3), color=color.blue)
    wall_t = box(pos=vector(0, side, 0), size=vector(s3, thk, s3), color=color.blue)
    wall_bk = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color=color.blue)


def generate_cells(grid: dict):
    for key in grid.keys():
        if grid[key]:
            box(pos=vector(*key), size=vector(1, 1, 1), color=color.red)


if __name__ == "__main__":
    grid = generate_grid_center_cell_start()
    rules =rule_1 #random_rule()
    print(rules)
    generate_stage()
    while 1:
        generate_cells(grid)
        grid = update_grid(grid, rules)
        sleep(0.5)
