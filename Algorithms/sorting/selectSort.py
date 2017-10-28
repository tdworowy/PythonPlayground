from random import randint


class SelectSort:
    @staticmethod
    def sort(list_):
        result = []
        list = list_[:]
        while len(list) > 0:
            result.append(min(list))
            index = list.index(min(list))
            list.pop(index)
        return result


if __name__ == '__main__':
    list = [randint(0, 1000) for x in range(10)]
    sortedList = SelectSort.sort(list)
    print(sortedList)

    list.sort()
    print(list)
    assert sortedList == list
