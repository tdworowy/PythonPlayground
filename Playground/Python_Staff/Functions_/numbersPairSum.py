


def find_pair(numbers, sume):
    if type(sume) != int: return "Second argument must be the int"
    if type(numbers) != list: return "First argument must be list"
    if len(numbers) < 2: return "List must have at leas 2 elements"
    while True:
        print("List", numbers)

        if len(numbers) == 0:
            print("FALSE")
            return False
        largest = max(numbers)
        negative_elements = sum(1 for number in numbers if number < 0)

        while largest > sume and negative_elements < 0:
            print("Largest number = ", largest)
            numbers.remove(largest)
            largest = max(numbers)
            print("While List after remove", numbers)

        numbers.remove(largest)
        print("List after remove", numbers)

        for number in numbers:
            print("Check if", number, "+", largest, "=", sume)
            if number + largest == sume:
                print("TRUE")
                return True

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [7, 2, 3, 4, 4]
    list3 = [11, 2, 3, 4, 4]
    list4 = [11, 2, 3, 4, 4, 22]
    list5 = [1, 1, 1, 1, 1, 22]
    list6 = [4, 1, 1, 4, 1, 22]
    list7 = [-1, 1, 1, 4, 1, 9]
    list8 = [-1, 1, 4, 4, 1, 20]
    list9 = [0, 8]

    find_pair(list1, 8)
    find_pair(list2, 8)
    find_pair(list3, 8)
    find_pair(list4, 8)
    find_pair(list5, 8)
    find_pair(list6, 8)
    find_pair(list7, 8)
    find_pair(list8, 8)
    find_pair(list9, 8)
