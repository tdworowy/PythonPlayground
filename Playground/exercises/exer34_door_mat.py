def door_mat(x: int, y: int):
    z = 1
    up = True
    for i in range(x):
        part = (y - (3 * z)) // 2
        middle = ".|." * z
        to_print = ("-" * part) + middle + ("-" * part)
        if i == (x - 1) / 2:
            message = "WELCOME"
            part = (y - len(message)) // 2
            to_print = ("-" * part) + message + ("-" * part)
            up = False

        print(to_print)
        if up:
            z += 2
        else:
            z -= 2


if __name__ == "__main__":
    door_mat(7, 21)
