from myUtils.randomString import randomString


def getListPercent_head(list,percent):
    percent = int(len(list) * (percent/100))
    retuntList = list[:percent]
    return retuntList


def getListPercent_tail(list,percent):
    percent = int(len(list) * (percent/100))
    retuntList = list[-percent:]
    return retuntList



if __name__ == '__main__':
    list1= list(randomString(150))
    print(getListPercent_head(list1,10))
    print(getListPercent_tail(list1, 10))