def commas(N):
    digits = str(N)
    assert digits.isdigit()
    result = ""
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + "," + result) if result else last3
    return result


def money(N, width=0):
    sign = "-" if N < 0 else ""
    N = abs(N)
    whole = commas(int(N))
    fract = ("%.2f" % N)[-2:]
    format = "%s%s.%s" % (sign, whole, fract)
    return "$%*s" % (width, format)


if __name__ == "__main__":

    def self_test():
        tests = 0, 1
        tests += 12, 123, 1234, 12345, 123456, 1234567
        for test in tests:
            print(commas(test))
        print("")
        tests = 0.1, 1, 1.23, 1.0, 1.2, 3.14156
        tests += 12.34, 12.344, 12.345, 12.346
        tests += 2**32, (2**32 + 0.2345)
        tests += 1.2345, 1.2, 0.2345
        tests += (2**32), (2**32 + 0.2345)
        tests += (2**100), (2**100)
        for test in tests:
            print("%s [%s]" % (money(test, 17), test))

    import sys

    if len(sys.argv) == 1:
        self_test()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))
