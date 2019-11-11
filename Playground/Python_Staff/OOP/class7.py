class x:
    def __init__(self):
        print("Class is called")

class y :
    def __init__(self):
        self.x = 2
    def __repr__(self):
        return str(self.x)
if __name__ == '__main__':
    x()
    print(y())

