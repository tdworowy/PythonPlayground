import re

if __name__ == '__main__':
    s = "Test 123 spam xxx"

    x = re.findall(r'\b\d+\b', s)
    print(x)
