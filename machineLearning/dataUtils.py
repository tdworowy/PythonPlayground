def getListPercent_head(list,percent):
    percent = int(len(list) * (percent/100))
    retuntList = list[percent:]
    return retuntList


def getListPercent_tail(list,percent):
    percent = int(len(list) * (percent/100))
    retuntList = list[:percent]
    return retuntList