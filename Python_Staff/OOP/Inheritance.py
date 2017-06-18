class c1 :
    def display1(self):
        print("from c1")

class c2 (c1):
     def display2(self):
        print("from c2")



test = c2()
test.display1()
test.display2()

