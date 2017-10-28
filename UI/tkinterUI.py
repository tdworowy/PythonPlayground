import tkinter
from doctest import master
from tkinter import messagebox


class GUI:
    def __init__(self):

        self.top = tkinter.Tk()
        self.width = 600
        self.height = 300

        self.btn_text = tkinter.StringVar(master)
        self.btn_text.set("Display Rectangle")
        self.canvas = tkinter.Canvas(master, width=self.width, height=self.height)
        self.button = tkinter.Button(master, textvariable=self.btn_text, command=self.call_back)
        self.entryW = tkinter.Entry(master)
        self.entryH = tkinter.Entry(master)

        self.flag = False

    def rectangle_cordinats(self):

        try:
            x = 50
            y = 25
            dic = {'x': x, 'y': y, 'x1': int(self.entryW.get()) + x, 'y1': int(self.entryH.get()) + y}
            return dic

        except Exception as ex:
            messagebox.showinfo(ex)

    def call_back(self):
        try:
            if not self.flag:
                coordinate = self.rectangle_cordinats()
                self.rectangle = self.canvas.create_rectangle(coordinate['x'], coordinate['y'], coordinate['x1'],
                                                              coordinate['y1'], fill="blue")

                self.flag = True
                self.btn_text.set("Hide Rectangle")
                print("Rectangle ON")
            else:
                self.canvas.delete(self.rectangle)
                self.flag = False
                self.btn_text.set("Display Rectangle")
                print("Rectangle OFF")

        except Exception as ex:
            print(ex)

    def main_Loop(self):
        self.button.pack()
        self.canvas.pack()
        self.entryW.pack()
        self.entryH.pack()

        self.top.mainloop()


def main():
    ui = GUI()
    ui.main_Loop()


if __name__ == "__main__":
    main()
