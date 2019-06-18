input = "UDDDUDUU"

def counting_valleys(n, s):
    level = 0
    valleys = 0
    in_valley = False
    for char in s:
        if char =="U":
            level +=1
        if char == "D":
            level -=1
        if level <0 and not in_valley:
            valleys +=1
            in_valley = True
        if level >=0:
            in_valley = False

    return valleys

print(counting_valleys(1, input))