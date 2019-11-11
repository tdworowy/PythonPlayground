if __name__ == "__main__":

    L1 = [1, 2, 3, 4, 5]
    L2 = [5, 6, 7, 8, 9]

    zpiList = list(zip(L1,L2))

    for(x,y) in zpiList:
        print(x,y, '--', x+y)



    keys=["spam","eggs" ,"tost"]
    vals = [1,3,5]

    dict1 = dict(zip(keys,vals)) # create dictionary
    print(dict1)