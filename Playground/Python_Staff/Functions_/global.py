
# for python 2.6 (can use nonlocal in 3.x)
def tester(start):
    global state
    state = start
    def nasted(label):
        global state
        print(label ,state)
        state +=1
    return nasted
if __name__ == "__main__":

    f = tester(0)
    f("spam")
    f("Dupa")

    g = tester(22)

    g("dupa2")
    f("spam2")