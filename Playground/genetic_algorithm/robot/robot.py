from random import choices


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

    def move(self, new_x: int, new_y: int):
        if 0 <= new_x < self.height and 0 <= new_y < self.width:
            self.grid[self.x][self.y] = (self.grid[self.x][self.y][0], 0)
            self.grid[new_x][new_y] = (self.grid[new_x][new_y][0], 1)

            self.x = new_x
            self.y = new_y
        else:
            self.points -= 10

    def take_point(self):
        if self.grid[self.x][self.y][0] == "point":
            self.points += 1
            self.grid[self.x][self.y] = ("empty", self.grid[self.x][self.y][1])
        else:
            self.points -= 1

    def play_strategy(self, strategy: list) -> list:
        current_situation = {}
        if self.x - 1 < 0:
            current_situation["up"] = "wall"
        else:
            current_situation["up"] = self.grid[self.x - 1][self.y][0]

        if self.x + 1 > self.height:
            current_situation["down"] = "wall"
        else:
            current_situation["down"] = self.grid[self.x + 1][self.y][0]

        if self.y < 0:
            current_situation["left"] = "wall"
        else:
            current_situation["left"] = self.grid[self.x][self.y - 1][0]

        if self.y + 1 > self.width:
            current_situation["right"] = "wall"
        else:
            current_situation["right"] = self.grid[self.x][self.y + 1][0]

        current_situation["current"] = self.grid[self.x][self.y][0]

        for situation in strategy:
            if situation[0] == current_situation:
                print(f"Make move: {situation[1]['action']}")
                print(f"x:{self.x} y:{self.y}")
                self.actions[situation[1]["action"]](self.x, self.y)
                break

        return self.grid


class Evolution:
    def __init__(self, actions: list, states: list, situations_per_strategy=1000):
        self.states = states
        self.actions = actions
        self.situations_per_strategy = situations_per_strategy
        self.population = []

    def generate_init_population(self, population_size: int):
        for i in range(population_size):
            strategy = [({"up": choices(self.states)[0],
                          "down": choices(self.states)[0],
                          "left": choices(self.states)[0],
                          "right": choices(self.states)[0],
                          "current": choices(self.states)[0]},
                         {"action": choices(self.actions)[0]}) for i in range(self.situations_per_strategy)]
            self.population.append(strategy)
