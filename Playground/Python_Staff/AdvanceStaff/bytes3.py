if __name__ == "__main__":

    x = b'avedwereajkwbdkjwabmb 2m'
    print(list(x))
    y = [z+1 for z in list(x)]
    print(y)
    z = ([chr(z) for z in y ])
    print(z)