import tkinter
from doctest import master
from tkinter import messagebox

class gui:
    def __init__(self):

        self.top = tkinter.Tk()
        self.width = 600
        self.height = 300

        self.btn_text = tkinter.StringVar(master)
        self.btn_text.set("Display Rectangle")
        self.canvas = tkinter.Canvas(master, width= self.width, height= self.height)
        self.button = tkinter.Button(master, textvariable=self.btn_text, command=self.callback)
        self.entryW = tkinter.Entry(master)
        self.entryH = tkinter.Entry(master)

        self.flag = False

    def rectangleCordinats(self):

        try:
          x = 50
          y = 25
          dic ={'x':x , 'y':y, 'x1':int(self.entryW.get())+x, 'y1':int(self.entryH.get())+y }
          return dic

        except Exception as ex:
            messagebox.showinfo(ex)



    def callback(self):
        try:
            if not self.flag:
                cordinate = self.rectangleCordinats()
                self.rectangle =self.canvas.create_rectangle(cordinate['x'], cordinate['y'], cordinate['x1'],cordinate['y1'], fill="blue")

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


    def mainLoop(self):
        self.button.pack()
        self.canvas.pack()
        self.entryW.pack()
        self.entryH.pack()

        self.top.mainloop()


def main():
    ui = gui()
    ui.mainLoop()


if __name__ == "__main__":
    main()