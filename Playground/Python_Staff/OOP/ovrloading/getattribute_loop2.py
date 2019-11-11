class getA:
    def __getattribute__(self, item):
       self.other #innfinite loop

if __name__ == '__main__':
    x = getA()
    x.name