import time
import tkinter
from collections import defaultdict
from doctest import master

from Playground.genetic_algorithm.robot.robot import generate_grid, Robot, Evolution


class GUI:
    def __init__(self, width: int = 1920, height: int = 1080, cell_size: int = 5):

        self.top = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        self.colours = {
            ("empty", 0): "blue",
            ("point", 0): "red",
            ("point", 1): "green",
            ("empty", 1): "green"}

        self.width = width
        self.height = height
        self.canvas = tkinter.Canvas(master, width=self.width, height=self.height)
        self.cell_size = cell_size

        self.cells = defaultdict(lambda: (-1, -1), {})

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

                    if self.cells[(x, y)] != (-1, -1):
                        self.canvas.delete(self.cells[(x, y)])

                    rectangle = self.canvas.create_rectangle(coordinate["x1"],
                                                             coordinate["y1"],
                                                             coordinate["x2"],
                                                             coordinate["y2"],
                                                             fill=self.colours[cell])
                    self.cells[(x, y)] = rectangle
                x = coordinate['x2']
            y = coordinate['y2']
            x = 0
        self.top.update()

    def main_loop(self):

        self.top_frame.pack(side="top", fill="both", expand=True)
        self.button_frame.pack(side="bottom", fill="both")
        self.canvas.pack(in_=self.button_frame)


if __name__ == "__main__":
    width: int = 400
    height: int = 400
    cell_size: int = 20
    grid_states = ["empty", "point"]
    grid = generate_grid(width // cell_size, height // cell_size, grid_states, [0.7, 0.3])
    prev_grid = [[(-1, -1) for _ in range(width // cell_size)] for _ in
                 range(height // cell_size)]

    evolution = Evolution(width // cell_size, height // cell_size)
    evolution.generate_init_population(400)
    for i in range(200):
        evolution.play_generation()
        evolution.generate_new_population(get_best=10)
        print("*" * 10)
        print(f"generation:{i} best:{evolution.best}")
        print("*" * 10)

    strategy = evolution.get_best()

    gui = GUI(width, height, cell_size)
    gui.main_loop()

    gui.draw(grid, prev_grid)
    prev_grid = [[value for value in row] for row in grid]
    time.sleep(0.5)

    robot = Robot(width // cell_size, height // cell_size, [[value for value in row] for row in grid])

    for i in range(200):
        grid = robot.play_strategy(strategy)
        gui.draw(grid, prev_grid)
        prev_grid = [[value for value in row] for row in grid]
        time.sleep(0.5)

    print(f"Robot points: {robot.points}")
    while 1:
        pass
