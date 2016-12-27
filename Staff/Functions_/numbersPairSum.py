list1 = [1, 2, 3, 4, 5]
list2 = [7, 2, 3, 4, 4]
list3 = [11, 2, 3, 4, 4]
list4 = [11, 2, 3, 4, 4, 22]
list5 = [1, 1, 1, 1, 1, 22]
list6 = [4, 1, 1, 4, 1, 22]
list7 = [-1, 1, 1, 4, 1, 9]
list8 = [-1, 1, 4, 4, 1, 20]
list9 = [0, 8]


def finndPair(numbers, suma):
    if type(suma) != int: return "Second argument must be the int"
    if type(numbers) != list: return "First argument must be list"
    if len(numbers) < 2: return "List must have at leas 2 elements"
    while (True):
        print("List", numbers)

        if len(numbers) == 0:
            print("FALSE")
            return False
        largest = max(numbers)
        negativeElements = sum(1 for number in numbers if number < 0)

        while largest > suma and negativeElements < 0:
            print("Largest number = ", largest)
            numbers.remove(largest)
            largest = max(numbers)
            print("While List after remove", numbers)

        numbers.remove(largest)
        print("List after remove", numbers)

        for number in numbers:
            print("Check if", number, "+", largest, "=", suma)
            if number + largest == suma:
                print("TRUE")
                return True


finndPair(list1, 8)
finndPair(list2, 8)
finndPair(list3, 8)
finndPair(list4, 8)
finndPair(list5, 8)
finndPair(list6, 8)
finndPair(list7, 8)
finndPair(list8, 8)
finndPair(list9, 8)
