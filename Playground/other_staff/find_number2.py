if __name__ == "__main__":
    for i in range(10000, 99999):
        x = i * i
        if str(x).startswith("27182"):
            print(i)
            break
