import itertools


def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for res in itertools.product(dice1, dice2):
        if res[0] > res[1]:
            dice1_wins += 1
        if res[1] > res[0]:
            dice2_wins += 1

    return dice1_wins, dice2_wins


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    dices = {i: dice for i, dice in enumerate(dices)}
    wins_dices = {i: 0 for i, dice in enumerate(dices)}
    for c in itertools.combinations(dices.keys(), 2):
        wins = count_wins(dices[c[0]], dices[c[1]])
        if wins[0] > wins[1]:
            wins_dices[c[0]] += 1
        if wins[1] > wins[0]:
            wins_dices[c[1]] += 1

    max_value = max(list(wins_dices.items()))
    if max_value[1] < len(dices) - 1:
        return -1
    else:
        return max_value[0]


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    for i in range(len(dices)):
        strategy[i] = (i + 1) % len(dices)

    # TODO

    return strategy


if __name__ == "__main__":
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    wins = count_wins(dice1, dice2)

    assert wins == (15, 15)

    dice1 = [1, 1, 6, 6, 8, 8]
    dice2 = [2, 2, 4, 4, 9, 9]
    assert count_wins(dice1, dice2) == (16, 20)

    dices1 = [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
    best_dice = find_the_best_dice(dices1)
    assert best_dice == -1
    dices2 = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
    best_dice = find_the_best_dice(dices2)
    assert best_dice == 2
    dices3 = [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]
    best_dice = find_the_best_dice(dices3)
    assert best_dice == -1

    dices4 = [[1, 2, 3, 4, 5, 6], [1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7]]
    best_dice = find_the_best_dice(dices4)
    print(best_dice)  # -1 is inncorrect
    # assert best_dice == -1
