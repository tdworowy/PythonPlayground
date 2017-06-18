def a1():
    b = []
    b.append('Test1')
    print(b)
def a2(b = []):
    b.append('Test2')
    print(b)

a1()
a1()
a2()
a2()
a2()