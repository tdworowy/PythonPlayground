def count_lines(name):
    with(open(name, 'r')) as file:
        return len(file.readlines())


def count_chars(name):
    with(open(name, 'r')) as file:
        return len(file.read())


def test(name):
    print("Lines: ", count_lines(name))
    print("Chars: ", count_chars(name))


if __name__ == '__main__':
    test("counter.py")
