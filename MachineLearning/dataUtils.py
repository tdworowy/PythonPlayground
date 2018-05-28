from MyUtils.randomString import generate_random_string


def get_list_percent_head(list, percent):
    percent = int(len(list) * (percent / 100))
    return list[:percent]


def get_list_percent_tail(list, percent):
    percent = int(len(list) * (percent / 100))
    return list[-percent:]


if __name__ == '__main__':
    list1 = list(generate_random_string(150))
    print(get_list_percent_head(list1, 10))
    print(get_list_percent_tail(list1, 10))
