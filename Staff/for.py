T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])

Z = {1, 2, 3, 4, 'a', 'b'}
for element in Z:
    print(element)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]
for key in tests:
    if key in items:
        print(key, "found")
    else:
        print(key, 'not found')

for key in tests:
    for item in items:
        if item == key:
            print(key, "found")
            break
    else:
        print(key, 'not found')

S = "abcdefghjklawdwd" * 10
for c in S[::2]: print(c, end='')
