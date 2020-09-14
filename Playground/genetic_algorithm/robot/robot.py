import statistics
from random import choices
from itertools import product
from random import randrange


def generate_grid(width: int, height: int, states: list, weights: list) -> list:
    grid = [[(choices(states, weights)[0], 0) for _ in range(width)] for _ in range(height)]
    grid[0][0] = (states[0], 1)
    return grid


class Robot:
    def __init__(self, width: int, height: int, grid: list):
        self.width = width
        self.height = height
        self.grid = grid

        self.x = 0
        self.y = 0

        self.actions = {
            "go_up": lambda x, y: self.move(x - 1, y),
            "go_down": lambda x, y: self.move(x + 1, y),
            "go_left": lambda x, y: self.move(x, y - 1),
            "go_right": lambda x, y: self.move(x, y + 1),
            "take_point": lambda x, y: self.take_point()
        }
        self.states = ["empty", "point", "wall"]
        self.points = 0

        self.wall_penalty = 10
        self.pickup_empty_penalty = 5
        self.step_penalty = 1
        self.pickup_reward = 10

    def move(self, new_x: int, new_y: int):
        if 0 <= new_x < self.height and 0 <= new_y < self.width:
            self.grid[self.x][self.y] = (self.grid[self.x][self.y][0], 0)
            self.grid[new_x][new_y] = (self.grid[new_x][new_y][0], 1)

            self.x = new_x
            self.y = new_y
            self.points -= self.step_penalty
        else:
            self.points -= self.wall_penalty

    def take_point(self):
        if self.grid[self.x][self.y][0] == "point":
            self.points += self.pickup_reward
            self.grid[self.x][self.y] = ("empty", self.grid[self.x][self.y][1])
        else:
            self.points -= self.pickup_empty_penalty

    def play_strategy(self, strategy: list) -> list:
        current_situation = {}
        if self.x - 1 < 0:
            current_situation["up"] = "wall"
        else:
            current_situation["up"] = self.grid[self.x - 1][self.y][0]

        if self.x + 1 >= self.height:
            current_situation["down"] = "wall"
        else:
            current_situation["down"] = self.grid[self.x + 1][self.y][0]

        if self.y < 0:
            current_situation["left"] = "wall"
        else:
            current_situation["left"] = self.grid[self.x][self.y - 1][0]

        if self.y + 1 >= self.width:
            current_situation["right"] = "wall"
        else:
            current_situation["right"] = self.grid[self.x][self.y + 1][0]

        current_situation["current"] = self.grid[self.x][self.y][0]

        for situation in strategy:
            if situation[0] == current_situation:
                self.actions[situation[1]["action"]](self.x, self.y)
                break

        return self.grid


class Evolution:
    def __init__(self, width: int, height: int):
        self.grid_states = ["empty", "point"]
        self.width = width
        self.height = height
        self.init_grid = generate_grid(width, height, self.grid_states, [0.7, 0.3])
        self.robot = Robot(width, height, [[value for value in row] for row in self.init_grid])

        self.states = self.robot.states
        self.actions = list(self.robot.actions.keys())
        self.moves = 300
        self.env_per_strategy = 10
        self.keep_parents = True

        self.mutation_rate = 0.05

        self.population = {}
        self.results = {}

    def generate_init_population(self, population_size: int):
        for i in range(population_size):
            strategy = [({"up": state[0],
                          "down": state[1],
                          "left": state[2],
                          "right": state[3],
                          "current": state[4]},
                         {"action": choices(self.actions)[0]}) for state in
                        product(self.states, repeat=5)]
            self.population[i] = strategy

    def play_generation(self):
        for key in self.population:
            points = []
            for j in range(self.env_per_strategy):
                for i in range(self.moves):
                    self.robot.play_strategy(self.population[key])
                points.append(self.robot.points)
                self.robot = Robot(self.width, self.height,
                                   generate_grid(self.width, self.height, self.grid_states, [0.7, 0.3]))

            self.results[key] = (statistics.mean(points), self.population[key])

    @staticmethod
    def _get_best(results: dict) -> tuple:
        best = -100000
        strategy_id = 0
        for key in results:
            if results[key][0] > best:
                best = results[key][0]
                strategy_id = key
        return strategy_id, best

    def get_best(self) -> list:
        strategy_id = self._get_best(self.results)[0]
        return self.population[strategy_id]

    def selection(self, get_best: int = 4) -> tuple:
        results_temp = self.results.copy()
        best_ids = []
        best_points = []
        for i in range(get_best):
            id, res = self._get_best(results_temp)
            best_ids.append(id)
            best_points.append(res)
            del results_temp[id]
        return best_ids, best_points

    def generate_new_population(self, get_best: int = 4):
        best = self.selection(get_best)[0]
        new_population = {}
        i = 0

        if self.keep_parents:
            for id in best:
                new_population[i] = self.population[id]
                i += 1

        while len(new_population) < len(self.population):

            for j in range(get_best - 1):

                split_place = randrange(0, len(self.population[best[j]]))
                first_half = self.population[best[j]][:split_place]
                second_half = self.population[best[j + 1]][split_place:]
                new_population[i] = first_half + second_half

                if choices([0, 1], weights=[1 - self.mutation_rate, self.mutation_rate])[0]:
                    x = randrange(0, len(new_population[i]))
                    new_population[i][x] = (
                        new_population[i][x][0], {"action": choices(self.actions)[0]})  # random mutation
                i += 1

        self.population = new_population
