import json


def readJson(file):
    with open(file) as data_file:
        data = json.load(data_file)
    return data


def getElment(file, ele):
    namesList = []
    groups = readJson(file)["objectTags"]["groups"]
    for group in groups:
        tags = group["tags"]
        for tag in tags:
            # print(tag["name"])
            namesList.append(tag[ele])
    return namesList


def compereList(lsit1, list2):
    first_set = set(map(tuple, lsit1))
    secnd_set = set(map(tuple, list2))
    return first_set.symmetric_difference(secnd_set)


if __name__ == "__main__":
    list1_n = getElment("json1.json", "name")
    list2_n = getElment("json2.json", "name")

    list1_k = getElment("json1.json", "key")
    list2_K = getElment("json2.json", "key")

    print(compereList(list1_n, list2_n))
    print(compereList(list1_k, list2_K))
