import random
from itertools import product


class RoundList(list):
    def __getitem__(self, index):
        while index not in range(0, len(self)):
            if index >= len(self):
                index = index - len(self)
            else:
                if index < 0: index = len(self) - (index * -1)
        return list.__getitem__(self, index)


class RuleSegment:
    def __init__(self, neighborhood: tuple, type: int):
        self.neighborhood = neighborhood
        self.type = type


def wolfram_number_to_bin(wolfram_number: int, possible_states: int) -> list:
    wolfram_number = bin(wolfram_number)[2:]
    temp = possible_states - len(wolfram_number)
    wolfram_number = "0" * temp + wolfram_number
    return list(wolfram_number)[::-1]


def generate_rule(wolfram_number: int, neighborhood_size: int = 3):
    possible_states = 2 ** neighborhood_size
    assert wolfram_number < 2 ** possible_states
    assert neighborhood_size % 2 != 0
    rule = []

    wolfram_number = wolfram_number_to_bin(wolfram_number, possible_states)
    for i, comb in enumerate(product([0, 1], repeat=neighborhood_size)):
        rule.append(RuleSegment(comb, int(wolfram_number[i])))
    return rule


def cellular_automata_step(input_list: RoundList, rules: list) -> RoundList:
    output_list = []
    for i in range(len(input_list)):
        for rule in rules:
            neighborhood_size = len(rule.neighborhood)
            temp = (neighborhood_size - 1) // 2
            if tuple(input_list[j] for j in range(i - temp, i + temp + 1)) == rule.neighborhood:
                output_list.append(rule.type)
    return RoundList(output_list)


if __name__ == "__main__":
    input_list = [0] * random.randrange(50, 100) + [1] * random.randrange(50, 100)
    random.shuffle(input_list)
    input_list = RoundList(input_list)
    rule = generate_rule(110, 5)

    for i in range(50):
        input_list = cellular_automata_step(input_list, rule)
        print("".join(["*" if i == 1 else " " for i in input_list]))
