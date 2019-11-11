class getA:
    def __getattribute__(self, item):
        print("GET attribute")
        x = self.other  # infinite loop_

    def __getattribute__(self, item):
        x = object.__getattribute__(self,"other") # now works ok


    def __setattr__(self, key, value):
        self.other = value # infinite loop

    def __setattr__(self, key, value):
        self.__dict__['other'] =value # now works ok
if __name__ == '__main__':
    x = getA()
    x.name = 'test'
    x.name