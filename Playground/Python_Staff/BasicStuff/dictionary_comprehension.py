if __name__ == "__main__":

    dic = {x: x * x for x in range(10)}
    print(dic)

    dic =  dict((x,x *x)for x in range(10))
    print(dic)