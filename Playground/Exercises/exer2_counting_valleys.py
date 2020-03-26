input = "UDDDUDUU"
input = "DUDDDUUDUU"


def counting_valleys(s):
    level = 0
    valleys = 0
    in_valley = False
    for char in s:
        if char == "U":
            level += 1
        if char == "D":
            level -= 1
        if level < 0 and not in_valley:
            valleys += 1
            in_valley = True
        if level >= 0:
            in_valley = False

    return valleys


if __name__ == "__main__":
    print(counting_valleys(input))
