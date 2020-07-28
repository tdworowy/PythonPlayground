class ListTree:
    def __str__(self):
        self.__visited = {}
        return '<Class instance {0}, adress {1}: \n{2} {3}>'.format(self.__class__.__name__,
                                                                    id(self),
                                                                    self.__attr_names(self, 0),
                                                                    self.__list_class(self.__class__, 3))

    def __list_class(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, adress{2}:( Look up)>\n'.format(dots, aClass.__name__, id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__list_class(c, indent + 4) for c in aClass.__bases__)
            return '\n{0} <Class {1}, adress {2}: \n{3} {4} {5}>\n'.format(dots, aClass.__name__, id(aClass),
                                                                           self.__attr_names(aClass, indent),
                                                                           ''.join(genabove), dots)

    def __attr_names(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0} = <>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result


if __name__ == '__main__':
    class Spam(ListTree):
        def __init__(self):
            self.data1 = 'spam1'
            self.data2 = {'spam2'}
            self.data3 = ['spam3']


    class Spam2(Spam):
        def __init__(self):
            Spam.__init__(self)
            self.data_1 = 'SPAM'
            self.data_2 = {'SPAM2'}
            self.data_3 = ['SPAM3']


    class Spam3(Spam):
        def __init__(self):
            Spam.__init__(self)
            self.data_1 = 'SPAMA'
            self.data_2 = {'SPAB2'}
            self.data_3 = ['SPAMC']


    class Spam4(Spam2, Spam3, Spam):
        def __init__(self):
            Spam2.__init__(self)
            Spam3.__init__(self)
            self.data_1 = 'SPAMA'
            self.data_2 = {'SPAB2'}
            self.data_3 = ['SPAMC']

if __name__ == '__main__':
    x1 = Spam()
    x2 = Spam2()
    x3 = Spam3()
    x4 = Spam4()
    print(x1)
    print(x2)
    print(x3)
    print(x4)
