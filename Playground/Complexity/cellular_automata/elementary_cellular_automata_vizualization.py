import tkinter
from doctest import master
from random import choice

from Playground.Complexity.cellular_automata.elementary_cellular_automata import RoundList, generate_rule, \
    cellular_automata_step


class GUI:
    def __init__(self):
        self.top = tkinter.Tk()
        self.width = 1200
        self.height = 900

        self.btn_step_text = tkinter.StringVar(master)
        self.btn_step_text.set("Step")

        self.btn_init_text = tkinter.StringVar(master)
        self.btn_init_text.set("Init Random")

        self.btn_init_one_text = tkinter.StringVar(master)
        self.btn_init_one_text.set("Init One")

        self.btn_clear_text = tkinter.StringVar(master)
        self.btn_clear_text.set("Clear")

        self.btn_play_text = tkinter.StringVar(master)
        self.btn_play_text.set("play")

        self.canvas = tkinter.Canvas(master, width=self.width, height=self.height)

        self.button_step = tkinter.Button(master, textvariable=self.btn_step_text, command=self.step_call_back)
        self.button_play = tkinter.Button(master, textvariable=self.btn_play_text, command=self.play_call_back)
        
        self.button_init_random = tkinter.Button(master, textvariable=self.btn_init_text, command=self.init_call_back)
        self.button_init_one = tkinter.Button(master, textvariable=self.btn_init_one_text, command=self.init_one_call_back)
        self.button_clear = tkinter.Button(master, textvariable=self.btn_clear_text, command=self.clear_call_back)
        self.wolfram_rule_number = tkinter.Entry(master)

        self.size = 5

        self.x = 0
        self.y = 0

        self.rectangles = []

    def rectangle_coordinates(self, x: int, y: int) -> dict:
        dic = {'x': x, 'y': y, 'x1': self.size + x, 'y1': self.size + y}
        return dic

    def init_call_back(self):
        self.rule = generate_rule(int(self.wolfram_rule_number.get()))
        self.input_list = RoundList([choice([0, 1]) for i in range(self.width // self.size)])

    def init_one_call_back(self):
        self.rule = generate_rule(int(self.wolfram_rule_number.get()))
        self.input_list = RoundList([0 for i in range(self.width // self.size)])
        self.input_list[len(self.input_list)//2] = 1


    def step_call_back(self):
        self.x = 0
        for i in self.input_list:
            coordinate = self.rectangle_coordinates(self.x, self.y)
            colour = "blue" if i == 1 else "red"
            rectangle = self.canvas.create_rectangle(coordinate['x'],
                                                     coordinate['y'],
                                                     coordinate['x1'],
                                                     coordinate['y1'], fill=colour)

            self.rectangles.append(rectangle)
            self.x += self.size
        self.input_list = cellular_automata_step(self.input_list, self.rule)
        self.y += self.size

    def play_call_back(self):
        for i in range(self.height // self.size):
            self.step_call_back()
            self.top.update()

    def clear_call_back(self):
        self.x = 0
        self.y = 0
        for rectangle in self.rectangles:
            self.canvas.delete(rectangle)

    def main_loop(self):
        self.button_step.pack()
        self.button_play.pack()
        self.button_init_random.pack()
        self.button_init_one.pack()
        self.button_clear.pack()
        self.wolfram_rule_number.pack()
        self.canvas.pack()

        self.top.mainloop()


def main():
    ui = GUI()
    ui.main_loop()


if __name__ == "__main__":
    main()
