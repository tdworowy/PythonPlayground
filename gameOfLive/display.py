import tkinter
from doctest import master
from tkinter import messagebox

from gameOfLive.gameOfLive_ import GameOfLive


class Display:
    def __init__(self,width,height):

        self.top = tkinter.Tk()
        self.width = width
        self.height = height

        self.btn_text = tkinter.StringVar(master)
        self.btn_text.set("START")
        self.canvas = tkinter.Canvas(master, width= self.width, height= self.height)
        self.startButton = tkinter.Button(master, textvariable=self.btn_text, command=self.start)
        self.entryW = tkinter.Entry(master)
        self.entryH = tkinter.Entry(master)

        self.game = GameOfLive(self.width, self.height)
        self.game.initLive([(10,10),(11,11),(12,12),(13,13),(14,14)])

    def rectangleCordinats(self,x,y):

        try:

          dic ={'x':x , 'y':y, 'x1':10+x, 'y1':10+y }
          return dic

        except Exception as ex:
            messagebox.showinfo(str(ex))



    def start(self):

        self.game.checkRules(3,2)
        self.generate(self.game.cellList)

    def generate(self, callesList):
        for call in callesList:
            cordinate = self.rectangleCordinats(call.x+10,call.y+10)
            if call.live : color = "green"
            else: color = "red"
            print("Generate rectangle: x: %s y: %s color: %s" % (cordinate['x'], cordinate['y'],color))
            self.canvas.create_rectangle(cordinate['x'], cordinate['y'], cordinate['x1'], cordinate['y1'],
                                                          fill=color)


    def mainLoop(self):
        self.startButton.pack()
        self.canvas.pack()
        self.top.mainloop()


def main():
    ui = Display(500,500)
    ui.mainLoop()


if __name__ == "__main__":
    main()