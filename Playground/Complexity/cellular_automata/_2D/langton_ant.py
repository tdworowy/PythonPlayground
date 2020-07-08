ant_symbol = 2


def if_zero(grid: list, x: int, y: int, turn: int) -> tuple:
    grid[x][y] = [1, 0]
    turn = turn + 1
    return grid, turn


def if_one(grid: list, x: int, y: int, turn: int) -> tuple:
    grid[x][y] = [0, 0]
    turn = turn - 1
    return grid, turn


rules = {
    0: if_zero,
    1: if_one
}


def generate_grid(width: int, hight: int) -> tuple:
    array = [[[0, 0] for _ in range(width)] for _ in range(hight)]
    array[width // 2][hight // 2] = (0, ant_symbol)
    turn = 1
    return array, turn


def update_grid(grid: list, turn: int, rules: dict = rules) -> tuple:
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if ant_symbol in value:
                position = i, j
    x, y = position
    grid, turn = rules[grid[x][y][0]](grid, x, y, turn)
    if turn == 5: turn = 1
    if turn == 1:
        grid[x + 1][y][1] = 2
    if turn == 2:
        grid[x][y - 1][1] = 2
    if turn == 3:
        grid[x - 1][y][1] = 2
    if turn == 4:
        grid[x][y + 1][1] = 2

    return grid, turn


if __name__ == "__main__":
    grid, turn = generate_grid(75, 75)
    for i in range(10):
        grid, turn = update_grid(grid, turn)
        print("*" * 10)
        for line in grid:
            print(line)
