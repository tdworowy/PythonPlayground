def count(aClass):
    aClass.numInstnaces = 0
    return aClass


@count
class Spam:
    def __init__(self):
        Spam.numInstnaces +=1
    def print_num_instances():#it works
        print("Instances created: ",Spam.numInstnaces)

if __name__ == "__main__":


    x = Spam()
    y = Spam()

    Spam.print_num_instances()
