contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
k = 3


def luck_balance(k, contests):
    max_luck = 0
    loose_important = 0
    contests.sort(reverse=True)
    for contest in contests:
        if contest[1] == 0:
            max_luck += contest[0]
        else:
            if loose_important < k:
                max_luck += contest[0]
                loose_important += 1
            else:
                max_luck -= contest[0]
    return max_luck


if __name__ == "__main__":
    print(luck_balance(k, contests))
