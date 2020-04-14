if __name__ == "__main__":

    print(len([i for i in range(1,10000) if sum([int(x) for x in [z for z in str(i)]]) == 9]))
    print(len([i for i in range(1, 10000) if sum([int(x) for x in [z for z in str(i)]]) == 10]))