import string


def print_line(line: list, max_len: int):
    line_ = "-".join(line)
    dashes = "-" * ((max_len - len(line_)) // 2)
    line_ = dashes + line_ + dashes
    print(line_)


def print_rangoli(size: int):
    max_len = 4 * size - 3
    lines = []
    leathers = string.ascii_lowercase[0:size]
    leathers = leathers[::-1] + leathers[1:]

    middle = "-".join(leathers)

    while len(leathers) > 1:
        line = leathers[: len(leathers) // 2 - 1] + leathers[len(leathers) // 2 + 1 :]
        lines.append(line)
        leathers = line
    for line in lines[::-1]:
        print_line(line, max_len)
    print(middle)
    for line in lines:
        print_line(line, max_len)


if __name__ == "__main__":
    print_rangoli(5)
    # print(len('--------e--------'))

# size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
