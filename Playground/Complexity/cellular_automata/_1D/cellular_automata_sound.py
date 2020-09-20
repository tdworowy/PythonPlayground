import winsound
import random

from Playground.Complexity.cellular_automata._1D.cellular_automata import generate_rule, cellular_automata_step
from Playground.Complexity.cellular_automata.utils.utils import RoundList

if __name__ == "__main__":
    sounds = {
        0: 100,
        1: 1300,
        2: 170,
        3: 1000,
        4: 250,
        5: 600
    }
    input_list = [0] * random.randrange(50, 100) + [1] * random.randrange(50, 100)
    random.shuffle(input_list)
    input_list = RoundList(input_list)

    rule = generate_rule(93254582498332408388995153046981554390801802940703147376395510193, 3, [0, 1, 2, 3, 4, 5])

    for i in range(20):
        input_list = cellular_automata_step(input_list, rule)
        for cell in input_list:
            winsound.Beep(sounds[cell], 200)
