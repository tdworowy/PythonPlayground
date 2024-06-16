s1 = "aba"
n1 = 10

s2 = "a"
n2 = 1000000000000

s3 = "aab"
n3 = 882787


def repeated_string(s, n):
    if len(s) == 1 and s == "a":
        return n
    new_str = s * int(n / len(s))
    return new_str.count("a") + 1


def repeated_string(s, n):
    if len(s) == 1 and s == "a":
        return n
    if not "a" in s:
        return 0
    res = []
    while len(res) < n:
        res.extend(list(s))
    new_string = "".join(res)
    return new_string[:n].count("a")


def repeated_string(s, n):
    return s.count("a") * (n // len(s)) + s[: n % len(s)].count("a")


if __name__ == "__main__":
    print(repeated_string(s1, n1))
    print(repeated_string(s2, n2))
    print(repeated_string(s3, n3))
