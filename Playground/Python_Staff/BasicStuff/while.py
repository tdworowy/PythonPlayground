
if __name__ == "__main__":

    while True:
        reply = input("Enter digit")
        if reply == "stop":break
        elif not reply.isdigit():
            print("Error!" * 5)
        else: print(int(reply) ** 2)
    print("End")



    while True:
        reply = input("Enter digit")
        if reply == "stop":break
        try:
            num = int(reply)
        except:
            print("Error")
        else:
            print(int(reply)*2)
    print("End")


    L = [1,2,3,4]
    while L:
        front , L =L[0],L[1:]
        print(front,L)

    L = [1, 2, 3, 4]
    while L:
            front, *L= L
            print(front, L)