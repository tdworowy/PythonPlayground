x = [(i, j) for i in range(0, 10) for j in range(0, 10)]
print(x)

for i, j in enumerate(x):
    num = int(''.join(map(str, [x[i][0], x[i][1]])))
    if (j[0] + j[1]) * 5 == num: print(num)
