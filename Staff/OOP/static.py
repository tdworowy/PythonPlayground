class c2 :
    def __init__(self):
        self.message = "__init__ was run (new object created)"

    def display(self):
        try:
           print(self.message)
        except Exception:
            print("__init__ was not run (like static in java)")


obj1 = c2()
obj1.display()

c2.display(c2)