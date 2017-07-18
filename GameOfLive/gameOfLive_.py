class Cell:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.live = False

    def revive(self):
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


    def getCall(self,x,y):

        return [call for call in self.cellList if call.x ==x and call.y ==y][0]

    def getkNeighbours(self,cell_check):#TODO
        neighbours = []
        try:
            for i in range(cell_check.x-2,cell_check.x+2):
                    for j in range(cell_check.y-2,cell_check.y+3):
                           neighbours.append(self.getCall(i,j))
        except Exception as ex:
            print((i,j))
            print(str(ex))
            pass
        return neighbours

    def checkRules(self,bornCount,stayAlive):
        index = 0
        for cell in self.cellList:
            index =+1
            if index % 10 == 0 :
                print("Calls checked: %s" % index)
            aliveCount = 0
            for neighbour in self.getkNeighbours(cell):
                if neighbour.live : aliveCount=+1
            if aliveCount == bornCount : cell.revive()
            if aliveCount == stayAlive: pass
            else: cell.kill()

    def initLive(self,list):
        for cell in self.cellList:
            for tuple in list:
                if tuple[0] == cell.x and tuple[1] == cell.y:
                    cell.revive



if __name__ == "__main__":
    game = GameOfLive(20,20)
    game.printCells()


#TODO
#https://pl.wikipedia.org/wiki/Gra_w_życie