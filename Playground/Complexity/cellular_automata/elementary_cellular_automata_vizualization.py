import tkinter
from doctest import master
from random import choice

from Playground.Complexity.cellular_automata.elementary_cellular_automata import RoundList, generate_rule, \
    cellular_automata_step


class GUI:
    def __init__(self, width: int = 1200, height: int = 900, cell_size: int = 5):
        self.top = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        self.width = width
        self.height = height

        self.canvas = tkinter.Canvas(master, width=self.width, height=self.height)

        self.button_step = tkinter.Button(master, text="Step", command=self.step_call_back)
        self.button_play = tkinter.Button(master, text="Play", command=self.play_call_back)

        self.button_init_random = tkinter.Button(master, text="Init random", command=self.init_call_back)
        self.button_init_one = tkinter.Button(master, text="Init one", command=self.init_one_call_back)

        self.button_clear = tkinter.Button(master, text="Clear", command=self.clear_call_back)

        self.wolfram_rule_number = tkinter.Entry(master)

        self.cell_size = cell_size

        self.x = 0
        self.y = 0

        self.cells = []

    def rectangle_coordinates(self, x: int, y: int) -> dict:
        dic = {'x': x, 'y': y, 'x1': self.cell_size + x, 'y1': self.cell_size + y}
        return dic

    def init_call_back(self):
        self.rule = generate_rule(int(self.wolfram_rule_number.get()))
        self.input_list = RoundList([choice([0, 1]) for i in range(self.width // self.cell_size)])

    def init_one_call_back(self):
        self.rule = generate_rule(int(self.wolfram_rule_number.get()))
        self.input_list = RoundList([0 for i in range(self.width // self.cell_size)])
        self.input_list[len(self.input_list) // 2] = 1

    def step_call_back(self):
        self.x = 0
        for i in self.input_list:
            coordinate = self.rectangle_coordinates(self.x, self.y)
            colour = "blue" if i == 1 else "red"
            rectangle = self.canvas.create_rectangle(coordinate['x'],
                                                     coordinate['y'],
                                                     coordinate['x1'],
                                                     coordinate['y1'], fill=colour)

            self.cells.append(rectangle)
            self.x += self.cell_size
        self.input_list = cellular_automata_step(self.input_list, self.rule)
        self.y += self.cell_size

    def play_call_back(self):
        for i in range(self.height // self.cell_size):
            self.step_call_back()
            self.top.update()

    def clear_call_back(self):
        self.x = 0
        self.y = 0
        for rectangle in self.cells:
            self.canvas.delete(rectangle)

    def main_loop(self):

        self.top_frame.pack(side="top", fill="both", expand=True)
        self.button_frame.pack(side="bottom", fill="both")

        self.button_step.pack(in_=self.top_frame, side="left")
        self.button_play.pack(in_=self.top_frame, side="left")
        self.button_init_random.pack(in_=self.top_frame, side="left")
        self.button_init_one.pack(in_=self.top_frame, side="left")
        self.button_clear.pack(in_=self.top_frame, side="left")

        self.wolfram_rule_number.pack(in_=self.top_frame, side="left")

        self.canvas.pack(in_=self.button_frame)

        self.top.mainloop()


def main():
    ui = GUI()
    ui.main_loop()


if __name__ == "__main__":
    main()
