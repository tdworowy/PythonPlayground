def calculate_fine(return_date, due_date):
    _return_date = [int(x) for x in return_date.split(" ")]
    _due_date = [int(x) for x in due_date.split(" ")]

    if _return_date[2] > _due_date[2]:
        return 10000
    if _return_date[2] == _due_date[2]:
        if _return_date[1] > _due_date[1]:
            return 500 * (_return_date[1] - _due_date[1])
        if _return_date[1] == _due_date[1]:
            if _return_date[0] > _due_date[0]:
                return 15 * (_return_date[0] - _due_date[0])
    return 0


if __name__ == "__main__":
    print(calculate_fine("31 12 2009", "1 1 2010"))
