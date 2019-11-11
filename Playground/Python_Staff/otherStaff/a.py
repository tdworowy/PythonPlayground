import random
if __name__ == '__main__':
    x=0
    y =  random.sample(range(1, 100), 99)
    print(sum(y))
    print(sum(y)/99)
    print(y)
    for i in range(100):
        x=x+1


    print(x)
    print(x/100)
