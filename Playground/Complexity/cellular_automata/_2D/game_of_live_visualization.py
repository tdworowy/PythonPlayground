import tkinter
from collections import defaultdict
from doctest import master

from Playground.Complexity.cellular_automata._2D.general_2d_automata import generate_grid_random_cells, update_grid, \
    game_of_live_rules


class GUI:
    def __init__(self, width: int = 1085, height: int = 1085, cell_size: int = 10):
        self.top = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        self.width = width
        self.height = height

        self.canvas = tkinter.Canvas(master, width=self.width, height=self.height)
        self.button_play = tkinter.Button(master, text="Play", command=self.play_call_back)

        self.labelText = tkinter.StringVar(master)
        self.rules_count = tkinter.Label(master, textvariable=self.labelText)

        self.cell_size = cell_size

        self.prev_step = [[-1 for _ in range(self.width // self.cell_size)] for _ in
                          range(self.height // self.cell_size)]

        self.probability_of_one = 0.7

        self.cells = defaultdict(lambda: (-1, -1), {})
        self.step = 1

    def rectangle_coordinates(self, x: int, y: int) -> dict:
        dic = {'x': x, 'y': y, 'x1': self.cell_size + x, 'y1': self.cell_size + y}
        return dic

    def step_call_back(self):
        colours_rules = {
            0: "blue",
            1: "red",
        }
        x = y = 0

        for row, row_prev in zip(self.grid, self.prev_step):
            for value, value_prev in zip(row, row_prev):
                coordinate = self.rectangle_coordinates(x, y)
                if value != value_prev:

                    if self.cells[(x, y)] != (-1, -1):
                        self.canvas.delete(self.cells[(x, y)])

                    colour = colours_rules[value]
                    rectangle = self.canvas.create_rectangle(coordinate['x'],
                                                             coordinate['y'],
                                                             coordinate['x1'],
                                                             coordinate['y1'],
                                                             fill=colour)
                    self.cells[(x, y)] = rectangle
                y = coordinate['y1']
            x = coordinate['x1']
            y = 0
        self.prev_step = [[value for value in row] for row in self.grid]
        self.grid = update_grid(self.grid, rules=game_of_live_rules)

    def play_call_back(self):
        self.grid = generate_grid_random_cells(self.width // self.cell_size, self.height // self.cell_size,
                                               self.probability_of_one)

        while 1:
            self.step_call_back()
            self.top.update()
            print(f"step: {self.step}")
            self.step += 1

    def main_loop(self):

        self.top_frame.pack(side="top", fill="both", expand=True)
        self.button_frame.pack(side="bottom", fill="both")

        self.button_play.pack(in_=self.top_frame, side="left")
        self.rules_count.pack(in_=self.top_frame, side="left")

        self.canvas.pack(in_=self.button_frame)

        self.top.mainloop()


def main():
    ui = GUI()
    ui.main_loop()


if __name__ == "__main__":
    main()
