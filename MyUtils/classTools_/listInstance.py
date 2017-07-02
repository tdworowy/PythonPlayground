class ListInstance:
    def __str__(self):
        return '<Class instance %s, addres %s:\n%s>' %(self.__class__.__name__,id(self),self.__attrnames2())

    # def __repr__(self):
    #     return '<Class instance %s, addres %s:\n%s>' %(self.__class__.__name__,id(self),self.__attrnames2())


    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tName %s = %s\n' % (attr,self.__dict__[attr])
        return result

    def __attrnames2(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result +='\tName %s = <>\n' % attr
            else:
                result += '\tName %s = %s\n' % (attr, getattr(self,attr))
        return result



if __name__ == '__main__':
    class Spam(ListInstance):
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



    x= Spam()
    y = Spam2()
    print(x)
    print(y)