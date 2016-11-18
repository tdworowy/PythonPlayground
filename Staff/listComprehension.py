import random
import string

L1=[1,2,3,4,5]
L2 = [x+10 for x in L1]
print(L1)
print(L2)

L3 = [1,2,3,4,5]

for i in range(len(L3)):
    L3[i] +=10

print(L3)


test = "Test" * 10
test2 = [x +"X" for x in test]
print(test2)

f = open("testFile.txt")
lines = f.readlines()
print(lines)

lines = [line.rstrip() for line in lines]
print(lines)

lines = [line.rstrip() for line in open("testFile.txt")]
print(lines)

f2 = open('testFike2.txt','r+')
for _ in range(1,30):
    print(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50)), file=f2)
lines = f2.readlines()
print(lines)

lines = [line for line in lines if line[0] == 'P']
print(lines)


test = [x+y for x in 'abc' for y in 'lmn']
print(test)