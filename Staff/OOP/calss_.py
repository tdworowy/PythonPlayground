class tester:
    def __init__(self,start):
        self.sate = start
    def nasted(self,label):
        print(label,self.sate)
        self.sate +=1



f = tester(0)
f.nasted('spam')
f.nasted('dupa')

g = tester(33)
g.nasted("spam2")
f.nasted('dupa2')

print(f.sate)
print(g.sate)



class tester2:
    def __init__(self,start):
         self.state = start
    def __call__(self, label):
        print(label,self.state)
        self.state +=1


H = tester2(99)
H("xxx")
H("xxx2")



class klas1:
    class klaas2:
        def display(self):
            print("___________")
            print("Test")

obj1 = klas1()
obj2 = obj1.klaas2()
obj2.display()