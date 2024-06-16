if __name__ == "__main__":
    map1 = list(map(ord, "spam"))
    print(map1)

    list1 = ["a", "b", "c", "d"]
    list2 = [list1 * 10, list1 * 2, list1 * 5]
    map2 = list(map(len, list2))
    print(map2)
