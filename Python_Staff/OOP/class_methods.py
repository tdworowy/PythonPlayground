class Spam:
    numInstnaces = 0
    def __init__(self):
        Spam.numInstnaces +=1
    def printNumInstances():#it works
        print("Instances created: ",Spam.numInstnaces)


x = Spam()
y = Spam()

Spam.printNumInstances()
