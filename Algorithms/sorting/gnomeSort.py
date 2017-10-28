from random import randint


class GnomeSort:
    @staticmethod
    def sort(list_):
        pos = 0
        list = list_[:]
        while pos < len(list):
            if pos == 0 or list[pos] >= list[pos - 1]:
                pos += 1
            else:
                list[pos], list[pos - 1] = list[pos - 1], list[pos]
                pos -= 1
        return list


if __name__ == '__main__':
    list = [randint(0, 10000) for x in range(1000)]
    sortedList = GnomeSort.sort(list)
    print(sortedList)

    list.sort()
    print(list)
    assert sortedList == list
