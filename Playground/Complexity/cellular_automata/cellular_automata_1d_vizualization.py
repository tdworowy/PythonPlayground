import tkinter
from doctest import master
from random import choice
from os import path, mkdir
from Playground.Complexity.cellular_automata.cellular_automata_1d import RoundList, generate_rule, \
    cellular_automata_step

from PIL import Image


def count_rules(neighborhood_size: int) -> int:
    return 2 ** (2 ** neighborhood_size)


def take_screenshot(folder: str, file_name: str, canvas: tkinter.Canvas):
    if not path.isdir(folder):
        mkdir(folder)
    if not path.isfile(path.join(folder, f'{file_name}.png')):
        canvas.postscript(file=f'{file_name}.eps')
        img = Image.open(f'{file_name}.eps')
        img.save(path.join(folder, f'{file_name}.png'), 'png')


class GUI:
    def __init__(self, width: int = 1920, height: int = 1080, cell_size: int = 5):
        self.top = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        self.width = width
        self.height = height

        self.canvas = tkinter.Canvas(master, width=self.width, height=self.height)

        self.button_step = tkinter.Button(master, text="Step", command=self.step_call_back)
        self.button_play = tkinter.Button(master, text="Play", command=self.play_call_back)

        self.button_init_random = tkinter.Button(master, text="Init random", command=self.init_random_call_back)
        self.button_init_one = tkinter.Button(master, text="Init one", command=self.init_one_call_back)

        self.button_clear = tkinter.Button(master, text="Clear", command=self.clear_call_back)

        self.button_play_all = tkinter.Button(master, text="Play all rules", command=self.play_all_rules_call_back)

        self.wolfram_rule_number = tkinter.Entry(master)
        self.wolfram_rule_number.insert(0, "90")

        self.neighborhood_size = tkinter.Entry(master)
        self.neighborhood_size.insert(0, "3")

        self.labelText = tkinter.StringVar(master)
        self.rules_count = tkinter.Label(master, textvariable=self.labelText)

        self.cell_size = cell_size

        self.x = 0
        self.y = 0

        self.cells = []
        self.init_way = "random"
        self.silent = False

    def rectangle_coordinates(self, x: int, y: int) -> dict:
        dic = {'x': x, 'y': y, 'x1': self.cell_size + x, 'y1': self.cell_size + y}
        return dic

    def init(self):
        self.rule = generate_rule(int(self.wolfram_rule_number.get()), int(self.neighborhood_size.get()))
        self.labelText.set(f"Possible Rules: {str(count_rules(int(self.neighborhood_size.get())))}")

    def random_init_list(self):
        return RoundList([choice([0, 1]) for i in range(self.width // self.cell_size)])

    def one_cell_start(self):
        input_list = RoundList([0 for i in range(self.width // self.cell_size)])
        input_list[len(input_list) // 2] = 1
        return input_list

    def init_random_call_back(self):
        self.init()
        self.input_list = self.random_init_list()
        self.init_way = "random_start"

    def init_one_call_back(self):
        self.init()
        self.input_list = self.one_cell_start()
        self.init_way = "one_cell_start"

    def step_call_back(self):
        self.x = 0
        for i in self.input_list:
            coordinate = self.rectangle_coordinates(self.x, self.y)
            colour = "blue" if i == 1 else "red"
            rectangle = self.canvas.create_rectangle(coordinate['x'],
                                                     coordinate['y'],
                                                     coordinate['x1'],
                                                     coordinate['y1'],
                                                     fill=colour)

            self.cells.append(rectangle)
            self.x += self.cell_size

        self.input_list = cellular_automata_step(self.input_list, self.rule)
        self.y += self.cell_size

    def play_call_back(self):
        for i in range(self.height // self.cell_size):
            self.step_call_back()
            if not self.silent:
                self.top.update()

    def clear_call_back(self):
        self.x = 0
        self.y = 0
        for rectangle in self.cells:
            self.canvas.delete(rectangle)

    def play_all_rules_call_back(self):
        self.silent = True
        for rule in range(count_rules(int(self.neighborhood_size.get()))):
            self.rule = generate_rule(rule, int(self.neighborhood_size.get()))

            self.wolfram_rule_number.delete(0, tkinter.END)
            self.wolfram_rule_number.insert(0, str(rule))

            self.play_call_back()
            self.top.update()

            take_screenshot(f"1d_neighborhood_size_{self.neighborhood_size.get()}", f"rule_{rule}_{self.init_way}",
                            self.canvas)

            self.clear_call_back()

            self.input_list = self.random_init_list() if self.init_way == 'random_start' else self.one_cell_start()

    def main_loop(self):

        self.top_frame.pack(side="top", fill="both", expand=True)
        self.button_frame.pack(side="bottom", fill="both")

        self.button_step.pack(in_=self.top_frame, side="left")
        self.button_play.pack(in_=self.top_frame, side="left")
        self.button_init_random.pack(in_=self.top_frame, side="left")
        self.button_init_one.pack(in_=self.top_frame, side="left")
        self.button_clear.pack(in_=self.top_frame, side="left")
        self.button_play_all.pack(in_=self.top_frame, side="left")

        self.wolfram_rule_number.pack(in_=self.top_frame, side="left")
        self.neighborhood_size.pack(in_=self.top_frame, side="left")
        self.rules_count.pack(in_=self.top_frame, side="left")

        self.canvas.pack(in_=self.button_frame)

        self.top.mainloop()


def main():
    ui = GUI()
    ui.main_loop()


if __name__ == "__main__":
    main()
