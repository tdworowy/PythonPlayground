def characters(frm, to):
    # return ','.join([chr(x) for x in range(frm,to)]) #max 1114111
    return [chr(x) for x in range(frm, to)]  # max 1114111


if __name__ == '__main__':
    with open("allChars.txt", 'a', encoding='utf-32') as f:
        list = characters(0, 1114111)
        for char in list:
            try:
                f.write(char)
            except Exception:
                continue
