class Life:
    def __init__(self,name='unknown'):
        print('Welcome ',name)
        self.name = name
    def __del__(self):
        print('Goodbye ',self.name)


brian = Life("Brian")
brian2 = Life("Brian2")
