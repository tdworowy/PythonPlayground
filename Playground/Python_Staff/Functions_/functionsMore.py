def addr(*args):
    sum = args[0]
    for x in args[1:]:
        sum += x
    return sum


def copyDic(dic):
    newDic = [{key, dic[key]} for key in dic.keys()]
    return newDic


def addDic(*dicks):
    newDic = {}
    for dic in dicks:
        for key in dic.keys():
            newDic[key] = dic[key]
    return newDic

if __name__ == "__main__":

    print(addr(1, 2, 3, 4))
    print(addr([1, 2, 3], [1, 2, 3]))

    # print(addr({1:"a",2:"b"},{1:"c",2:"D"}))
    # print(addr([1,2,3],2))
    # print(addr('a','b'))
    # print(addr(1,'b'))
    # print(addr(1,[1,2,3]))

    testDic1 = {1: "a", 2: "b"}
    testDic2 = {3: "c", 4: "d"}
    print(copyDic(testDic1))
    print(addDic(testDic1, testDic2))
