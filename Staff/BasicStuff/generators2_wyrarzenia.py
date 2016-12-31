#wyrarzenie generatora

test = (x **2 for x in range(10))
print(test)
print(list(test))

test = (x **2 for x in range(10))
print(next(test))
print(next(test))


for num in (x ** 2 for x in range(10)):
    print('%s, %s' %(num,num /2.0))