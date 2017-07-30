class getA:
    def __getattribute__(self, item):
       self.other #innfinite loop

x = getA()
x.name