def count(aClass):
    aClass.numInstnaces = 0
    return aClass


@count
class Spam:
    def __init__(self):
        Spam.numInstnaces +=1
    def printNumInstances():#it works
        print("Instances created: ",Spam.numInstnaces)


x = Spam()
y = Spam()

Spam.printNumInstances()
