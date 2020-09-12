import time

import pygame

from Playground.genetic_algorithm.robot.robot import generate_grid, Robot, Evolution


class GUI:
    def __init__(self, width: int = 1920, height: int = 1080, cell_size: int = 5):

        self.colours = {
            ("empty", 0): (0, 0, 255),
            ("point", 0): (255, 0, 0),
            ("point", 1): (0, 255, 0),
            ("empty", 1): (0, 255, 0)}

        self.width = width
        self.height = height

        self.cell_size = cell_size

    def rectangle_coordinates(self, x: int, y: int) -> dict:
        dic = {'x1': x, 'y1': y, 'x2': self.cell_size + x, 'y2': self.cell_size + y}
        return dic

    def draw(self, grid: list, prev_grid: list):
        x = 0
        y = 0
        for row, prev_row in zip(grid, prev_grid):
            for cell, prev_cell in zip(row, prev_row):
                coordinate = self.rectangle_coordinates(x, y)
                if cell != prev_cell:
                    pygame.draw.rect(self.screen, self.colours[cell], (coordinate["x1"],
                                                                       coordinate["y1"],
                                                                       coordinate["x2"],
                                                                       coordinate["y2"]))
                y = coordinate['y2']
            x = coordinate['x2']
            y = 0
        pygame.display.flip()

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.flip()


if __name__ == "__main__":
    width: int = 400
    height: int = 400
    cell_size: int = 20
    grid_states = ["empty", "point"]

    grid = generate_grid(width // cell_size, height // cell_size, grid_states, [0.7, 0.3])
    prev_grid = [[(-1, -1) for _ in range(width // cell_size)] for _ in
                 range(height // cell_size)]

    robot = Robot(width // cell_size, height // cell_size, grid)
    evolution = Evolution(list(robot.actions.keys()), robot.states)

    evolution.generate_init_population(1)

    gui = GUI(width, height, cell_size)
    gui.init()

    gui.draw(grid, prev_grid)
    prev_grid = [[value for value in row] for row in grid]
    time.sleep(0.5)

    for i in range(200):
        grid = robot.play_strategy(evolution.population[0])
        gui.draw(grid, prev_grid)
        prev_grid = [[value for value in row] for row in grid]
        time.sleep(0.5)

    print(robot.points)
    while 1:
        pass
