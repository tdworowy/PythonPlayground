# broken example from book it maybe worked in older than 3.5.2 version of python
def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
        nested.state = start
        return nested

F = tester(0)
F("spam")
F('dupa')

g = tester(33)
g("spam2")
F('dupa2')
