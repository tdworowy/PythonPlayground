if __name__ == "__main__":
    log = open("log.txt", "w")
    print(1, 2, 3, file=log)
    log.close()
    print(open("log.txt").read())
    log.close()
