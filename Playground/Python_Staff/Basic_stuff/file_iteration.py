if __name__ == "__main__":

    test_l= ["Test"] * 10
    print(test_l)
    file = open("testFile.txt",'w')
    for el in test_l:
        print(el,file=file)
    file.close()

    for line in open("testFile.txt"):
        print(line)

    file2 = open("testFile.txt")
    print(next(file2).upper())