import json


def read_json(file):
    with open(file) as data_file:
        data = json.load(data_file)
    return data


def get_element(file, ele):
    names = []
    groups = read_json(file)["objectTags"]["groups"]
    for group in groups:
        tags = group["tags"]
        for tag in tags:
            # print(tag["name"])
            names.append(tag[ele])
    return names


def compere(list1, list2):
    first_set = set(map(tuple, list1))
    second_set = set(map(tuple, list2))
    return first_set.symmetric_difference(second_set)


if __name__ == "__main__":
    list1_n = get_element("json1.json", "name")
    list2_n = get_element("json2.json", "name")

    list1_k = get_element("json1.json", "key")
    list2_K = get_element("json2.json", "key")

    print(compere(list1_n, list2_n))
    print(compere(list1_k, list2_K))
