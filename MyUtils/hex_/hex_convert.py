import binascii

with open("hex.txt", 'r') as f1, open("str.txt", "w", encoding="utf8") as f2:
    for line in f1.readlines():
        for char in line:
            if not char.isspace():
                s = s + char
            else:
                print(str(binascii.unhexlify(s)))
                f2.write(str(binascii.unhexlify(s))+"\n")
                s = ""
