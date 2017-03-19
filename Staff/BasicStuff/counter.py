def countLines(name):
    with(open(name,'r') ) as file:
        return len(file.readlines())

def countChars(name):
    with(open(name, 'r')) as file:
        return len(file.read())

def test(name):
    print("Lines: ",countLines(name))
    print("Chars: ",countChars(name))


if __name__ == '__main__':
    test("counter.py")