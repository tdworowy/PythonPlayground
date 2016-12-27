
TestL= ["Test"]*10
print(TestL)
file = open("testFile.txt",'w')
for el in TestL:
    print(el,file=file)
file.close()

for line in open("testFile.txt"):
    print(line)

file2 = open("testFile.txt")
print(next(file2).upper())