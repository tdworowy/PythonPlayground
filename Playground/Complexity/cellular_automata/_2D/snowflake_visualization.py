import tkinter
from doctest import master

from Playground.Complexity.cellular_automata._2D.general_2d_automata import  update_grid, \
    generate_snowflake_rule, generate_grid_central


class GUI:
    def __init__(self, width: int = 1085, height: int = 1085, cell_size: int = 4):
        self.top = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        self.width = width
        self.height = height

        self.canvas = tkinter.Canvas(master, width=self.width, height=self.height)
        self.button_play = tkinter.Button(master, text="Play", command=self.play_call_back)

        self.labelText = tkinter.StringVar(master)
        self.rules_count = tkinter.Label(master, textvariable=self.labelText)

        self.neighbours_number = tkinter.Entry(master)
        self.neighbours_number.insert(0, "1,5") # other "1,3,5", "1,3"

        self.ini_cell_count = tkinter.Entry(master)
        self.ini_cell_count.insert(0, "1")

        self.cell_size = cell_size

        self.prev_step = [[-1 for _ in range(self.width // self.cell_size)] for _ in
                          range(self.height // self.cell_size)]

        self.cells = []
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
                    colour = colours_rules[value]
                    rectangle = self.canvas.create_rectangle(coordinate['x'],
                                                             coordinate['y'],
                                                             coordinate['x1'],
                                                             coordinate['y1'],
                                                             fill=colour)
                    if self.step >= 2:
                        self.cells = [rectangle]

                y = coordinate['y1']
            x = coordinate['x1']
            y = 0
        self.prev_step = [[value for value in row] for row in self.grid]
        neighbours_number = [int(number) for number in self.neighbours_number.get().split(",")]
        self.grid = update_grid(self.grid, rules=generate_snowflake_rule(neighbours_number))

    def play_call_back(self):
        self.grid = generate_grid_central(self.width // self.cell_size,
                                           self.height // self.cell_size,
                                          int(self.ini_cell_count.get()))

        while 1:
            self.step_call_back()
            self.top.update()
            self.step += 1
            for rectangle in self.cells:
                self.canvas.delete(rectangle)

    def main_loop(self):

        self.top_frame.pack(side="top", fill="both", expand=True)
        self.button_frame.pack(side="bottom", fill="both")

        self.button_play.pack(in_=self.top_frame, side="left")
        self.rules_count.pack(in_=self.top_frame, side="left")
        self.neighbours_number.pack(in_=self.top_frame, side="left")
        self.ini_cell_count.pack(in_=self.top_frame, side="left")

        self.canvas.pack(in_=self.button_frame)

        self.top.mainloop()


def main():
    ui = GUI()
    ui.main_loop()


if __name__ == "__main__":
    main()
