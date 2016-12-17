list1 = [1, 2, 3, 4, 5]
list2 = [7, 2, 3, 4, 4]
list3 = [11, 2, 3, 4, 4]
list4 = [11, 2, 3, 4, 4, 22]
list5 = [1, 1, 1, 1, 1, 22]
list6 = [4, 1, 1, 4, 1, 22]


def finndPair(numbers, sum):
    while (True):
        print("List", numbers)
        if len(numbers) == 0:
            print("FALSE")
            return False
        largest = max(numbers)
        while largest >= sum:
            print("Largest number = ", largest)
            numbers.remove(largest)
            largest = max(numbers)
            print("List after remove", numbers)
        for number in numbers:
            print("Check if", number, "+", largest, "=", sum)
            if number + largest == sum:
                print("TRUE")
                return True
        else:
            numbers.remove(largest)


finndPair(list1, 8)
finndPair(list2, 8)
finndPair(list3, 8)
finndPair(list4, 8)
finndPair(list5, 8)
finndPair(list6, 8)