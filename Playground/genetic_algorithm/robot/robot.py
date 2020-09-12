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
        if new_x >= self.width | new_y >= self.height:
            self.points -= 10
        elif new_x < 0 | new_y < 0:
            self.points -= 10
        else:
            self.grid[self.x][self.y] = (self.grid[self.x][self.y][0], 0)
            self.grid[new_x][new_y] = (self.grid[new_x][new_y][0], 1)

            self.x = new_x
            self.y = new_y

    def take_point(self):
        if self.grid[self.x][self.y][0] == "point":
            self.points += 1
            self.grid[self.x][self.y] = ("empty", self.grid[self.x][self.y][1])
        else:
            self.points -= 1

    def play_strategy(self, strategy: list) -> list:
        current_situation = {}
        try:
            current_situation["up"] = self.grid[self.x - 1][self.y][0]
        except IndexError:
            current_situation["up"] = "wall"
        try:
            current_situation["down"] = self.grid[self.x + 1][self.y][0]
        except IndexError:
            current_situation["down"] = "wall"
        try:
            current_situation["left"] = self.grid[self.x][self.y - 1][0]
        except IndexError:
            current_situation["left"] = "wall"
        try:
            current_situation["right"] = self.grid[self.x][self.y + 1][0]
        except IndexError:
            current_situation["right"] = "wall"

        current_situation["current"] = self.grid[self.x][self.y][0]

        for situation in strategy:
            if situation[0] == current_situation:
                print(f"Make move: {situation[1]['action']}")
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
