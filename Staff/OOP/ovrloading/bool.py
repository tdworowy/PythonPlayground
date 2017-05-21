class false:
    def __bool__(self):return  False

x = false()
if not x:  print("False")

class length:
    def __len__(self): return  10


x= length()
print(len(x))
    