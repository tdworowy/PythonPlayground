
print("I'm : ",__name__)
def minmax(test,*args):
    res = args[0]
    for arg in args:
        if test(arg,res):
            res = arg
    return res

def lessthan(x,y) : return  x < y
def grtrthan (x,y): return  x > y

if __name__ == '__main__': #tests , won't run if module is imported
    print(minmax(lessthan,4,2,1,4,67,8,9,3,1))
    print(minmax(grtrthan, 4, 2, 1, 4, 67, 8, 9, 3, 1))