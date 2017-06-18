def func():
    x =4
    action = (lambda n : x**n)
    return  action

x = func()
print(x(2))
print(x(4))
print(x(8))


#

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda  x: i **x)
    return acts

acts = makeActions()
print(acts[0])
print(acts[1])

print(acts[0](2))
print(acts[1](2))
print(acts[1](3)) #to get correct result need to use default value


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i:i ** x)
    return acts


acts = makeActions()
print(acts[0])
print(acts[1])

print(acts[0](2))
print(acts[0](3))
print(acts[1](2))
print(acts[2](2))
print(acts[1](3))
print(acts[4](2))
print(acts[4](4))