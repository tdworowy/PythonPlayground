def get_diff(string1, string2):
    char_list = list(string2)
    i = 0
    diff = []
    for char1 in string1:
        if i < len(char_list):
            if char1 != char_list[i]:
                diff.append((char_list[i], char1))
            i += 1
    return diff
