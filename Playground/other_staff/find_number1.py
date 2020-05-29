if __name__ == "__main__":
    for i in range(100000, 100999):
        if i % 9127 == 0:
            print(i)

    flag = []
    for i in range(100, 999):
        for d in [2, 3, 4, 5, 6, 7]:
            if i % d == 1:
                flag.append(True)
            else:
                flag.append(False)
        if all(flag):
            print(i)
        flag = []
