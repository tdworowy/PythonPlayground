import tkinter
from doctest import master

from Playground.Complexity.cellular_automata._2D.langton_ant import generate_grid, update_grid


class GUI:
    def __init__(self, width: int = 1825, height: int = 1825, cell_size: int = 5):
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

        self.cells = []

    def rectangle_coordinates(self, x: int, y: int) -> dict:
        dic = {'x': x, 'y': y, 'x1': self.cell_size + x, 'y1': self.cell_size + y}
        return dic

    def step_call_back(self):

        colours_rules = {
            (0, 0): "blue",
            (1, 0): "red",
            (0, 2): "black",
            (1, 2): "black"
        }

        for x, row in enumerate(self.grid):
            for y, value in enumerate(row):
                coordinate = self.rectangle_coordinates(x, y)# TODO use x1 and y2 or smt
                colour = colours_rules[tuple(value)]
                rectangle = self.canvas.create_rectangle(coordinate['x'],
                                                         coordinate['y'],
                                                         coordinate['x1'],
                                                         coordinate['y1'],
                                                         fill=colour)
                self.top.update()

        self.grid, self.turn = update_grid(self.grid, self.turn)

    def play_call_back(self):
        self.grid, self.turn = generate_grid(self.width//self.cell_size, self.height//self.cell_size)
        while 1:
            self.step_call_back()
            #self.top.update()

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
