class SkipIterator:
    def __init__(self,wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset +=2
            return item

class SkipObject:
    def __init__(self,wrapped):
        self.wrapped =wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

if __name__ == "__main__":
    alpha = "abcdefghijk"
    skiiper = SkipObject(alpha)
    I = iter(skiiper)
    print( next(I),next(I),next(I))

    for x in skiiper:
        for y in skiiper:
            print(x+y,end=" ")