import binascii


def hex_to_str(hex_lines: list[str]) -> list[str]:
    str_lines = []
    for line in hex_lines:
        s = ""
        for char in line:
            if not char.isspace():
                s = s + char
            else:
                str_lines.append(str(binascii.unhexlify(s)))
    return str_lines


if __name__ == "__main__":
    with open("hex.txt", "r") as f1, open("str.txt", "w", encoding="utf8") as f2:
        hex_lines = hex_to_str(f1.readlines())
        for line in hex_lines:
            f2.write(line)
