class Cell:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.live = False

    def Revive(self):
        self.live = True

    def kill(self):
        self.live = False

    def __str__(self):
        coordinate = "coordinate %s %s" % (self.x , self.y)
        alive = "Alive: %s" % str(self.live)
        return coordinate +"\n" +alive


class GameOfLive:
    def __init__(self,length,width):
        self. cellList = []
        for x in range(0,length):
            for y in range(0,width):
                self.cellList.append(Cell(x,y))

    def printCells(self):
        for cell in self.cellList:
            print(cell)

    def getAlive(self):
        return [cell for cell in self.cellList if cell.live]

    def getDead(self):
        return [cell for cell in self.cellList if not cell.live]

    def printAlive(self):
        for cell in self.getAlive():
            print(cell)

    def printDead(self):
        for cell in self.getDead():
            print(cell)



if __name__ == "__main__":
    game = GameOfLive(20,20)
    game.printCells()


#TODO
#https://pl.wikipedia.org/wiki/Gra_w_życie