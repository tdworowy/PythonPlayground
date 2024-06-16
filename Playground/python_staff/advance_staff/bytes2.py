if __name__ == "__main__":

    list = [x for x in range(0, 256)]
    print(bytes(list))
    chars = []
    for byte in bytes(list):
        try:
            chars.append(chr(byte))
        except Exception:
            continue

    print(",".join(chars))
