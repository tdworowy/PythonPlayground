class Number:
    def __init__(self,base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3

if __name__ == '__main__':
    x = Number(2)
    y = Number(3)
    z = Number(4)


    acts = [x.double,y.double,z.double]
    for act in acts:
         print(act())
         print(act.__self__)
         print(dir(act))