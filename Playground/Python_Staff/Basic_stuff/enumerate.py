if __name__ == "__main__":

    s = "spam_"* 30

    for(offset,item) in enumerate(s):
        print(item , "on position ", offset);


    e = enumerate(s)
    print(e)


    E = enumerate('SPAM')
    I = iter(E)
    print(next(I))
    print(next(I))
    print(next(I))
    print(list(E))
    print(list(enumerate('SPAM')))