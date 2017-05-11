class AttrDisplay:
    def __getherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append("%s = %s" % (key,getattr(self,key)))
        return ", ".join(attrs)
    def __str__(self):
        return "[%s: %s ]" % (self.__class__.__name__,self.__getherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        cout =0
        def __init__(self):
            self.attr1 = TopTest.cout
            self.attr2 = TopTest.cout + 1
            TopTest.cout +=2
    class SubTest(TopTest): pass

    X, Y = TopTest(),SubTest()
    print(X)
    print(Y)