def tester(start):
    state = start
    def nasted (label):
        print(label,state)
    return nasted

F = tester(0)

print(F('Spam'))
print(F('Dupa'))


def tester(start):
    state = start
    def nasted (label):
        nonlocal  state
        print(label,state)
        state +=1
    return nasted

F = tester(0)
print(F('Spam'))
print(F('Dupa'))

G = tester(50)
print(G('Spam'))
print(G('Dupa'))

print(F('AAAA'))
