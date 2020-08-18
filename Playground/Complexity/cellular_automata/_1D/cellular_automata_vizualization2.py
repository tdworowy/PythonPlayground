import pygame
import yaml

from Playground.Complexity.cellular_automata._1D.cellular_automata import cellular_automata_step, generate_rule
from Playground.Complexity.cellular_automata._1D.cellular_automata_vizualization1 import generate_random
from Playground.Complexity.cellular_automata.utils.utils import RoundList


class GUI:
    def __init__(self, width: int = 1920, height: int = 1080, cell_size: int = 5, color_count: int = 2,
                 neighborhood_size: int = 3, rule_number: int = 90):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Cellular Automata')

        pygame.display.flip()

        self.x = 0
        self.y = 0
        self.cell_size = cell_size
        self.color_count = color_count
        self.neighborhood_size = neighborhood_size
        self.rule_number = rule_number
        self.running = True
        self.input_list = self.random_init_list()

    def random_init_list(self):
        return RoundList(generate_random(
            input_list=[i for i in range(self.color_count)],
            length=self.width // self.cell_size)
        )

    def rectangle_coordinates(self, x: int, y: int) -> dict:
        dic = {'x1': x, 'y1': y, 'x2': self.cell_size + x, 'y2': self.cell_size + y}
        return dic

    def draw_cell(self, cells: list):
        colours = {
            0: (0, 0, 255),
            1: (255, 0, 0),
            2: (0, 255, 0),
            3: (0, 0, 0),
            4: (255, 255, 255),
            5: (255, 200, 200)
        }
        self.x = 0
        for cell in cells:
            coordinate = self.rectangle_coordinates(self.x, self.y)
            pygame.draw.rect(self.screen, colours[cell], (coordinate["x1"],
                                                          coordinate["y1"],
                                                          coordinate["x2"],
                                                          coordinate["y2"]))
            self.x += self.cell_size
        self.y += self.cell_size
        pygame.display.flip()

    def run(self):
        rule = generate_rule(self.rule_number,
                             self.neighborhood_size,
                             [i for i in range(self.color_count)])

        while self.running:
            self.draw_cell(self.input_list)
            self.input_list = cellular_automata_step(self.input_list, rule)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


def read_config():
    with open("visualization_config.yaml") as file:
        return yaml.safe_load(file)


if __name__ == "__main__":
    rule_id = 4
    config = read_config()
    config = config[rule_id]
    config = config.get(f"rule_{rule_id}")
    print(config)
    GUI(
        color_count=config.get("colors"),
        neighborhood_size=config.get("neighborhood_size"),
        rule_number=config.get("rule")

    ).run()
