def getDiff(string1, string2):
    charList = list(string2)
    i =0
    diff = []
    for char1 in string1:
        if(i < len(charList)):
            if char1 != charList[i]:
                diff.append((charList[i],char1))
            i +=1
    return diff


