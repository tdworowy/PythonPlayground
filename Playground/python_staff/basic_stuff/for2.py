if __name__ == "__main__":

    S = "Spam" * 10

    for char in S:
        print(ord(char))

    x = 0
    for char in S:
        x += ord(char)
    print("Sum:" + str(x))

    y = []
    for char in S:
        y.append(ord(char))
    print("List: " + str(y))

    print(list(map(ord, S)))

    for i in range(50):
        print("Welcome %d\n\a" % i)

    D = dict(a=1, b=2, c=3, d=10)

    for key in sorted(D):
        print(D[key])
