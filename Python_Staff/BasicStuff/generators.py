def gensquares(N):
    for i in range(N):
        yield i **2


print (gensquares(5).__next__())

for i in gensquares(5):
    print(i,end =' : ')


x = gensquares(10)
print(next(x))
print(next(x))
print(next(x))


def gen():
    for i in range(10):
        x = yield i
        print(x)

G = gen()
print('___________')
next(G)
next(G)
next(G)

G.send(77)
G.send(88)