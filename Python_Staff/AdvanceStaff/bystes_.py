
x = 'test 123 aa'.encode()

x1 = b'test 123 aa'

print(x)
print(x[0])
print(x[-1])

for char in x:
    print(str(char) +" "+ chr(char))