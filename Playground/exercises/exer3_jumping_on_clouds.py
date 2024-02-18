x1 = [0, 0, 1, 0, 0, 1, 0]  # 4
x2 = [0, 0, 0, 0, 1, 0]  # 3


def jumping_on_clouds(c):
    jumps = 0
    index = 0
    for i, _ in enumerate(c):

        if index + 2 < len(c) and c[index + 2] != 1:
            jumps += 1
            index += 2
        else:
            if index + 1 < len(c) and c[index + 1] != 1:
                jumps += 1
                index += 1
    return jumps


if __name__ == "__main__":
    print(jumping_on_clouds(x1))
    print(jumping_on_clouds(x2))
