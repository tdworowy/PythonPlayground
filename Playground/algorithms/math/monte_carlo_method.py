import numpy as np
import math
import random
import matplotlib.pyplot as plt


def generate_point(size: int) -> tuple:
    x = random.random() * size
    y = random.random() * size
    return x, y


def is_in_circle(point: tuple, size: int) -> bool:
    return math.sqrt(point[0] ** 2 + point[1] ** 2) <= size


def compute_pi(points_inside_circle: int, points_inside_square: int) -> float:
    return 4 * (points_inside_circle / points_inside_square)


def monte_carlo_method(sample_size: int, square_size: int):
    arc = np.linspace(0, np.pi / 2, 100)
    points_inside_circle = 0
    points_inside_square = 0

    plt.axes().set_aspect('equal')
    plt.plot(1 * np.cos(arc), 1 * np.sin(arc))

    for i in range(sample_size):
        point = generate_point(square_size)
        plt.plot(point[0], point[1], 'c.')
        points_inside_square += 1
        if is_in_circle(point, square_size):
            points_inside_circle += 1

    print(f"Approximate value of pi is {compute_pi(points_inside_circle, points_inside_square)}")
    plt.show()


if __name__ == "__main__":
    square_size = 1
    sample_size = 3000
    monte_carlo_method(sample_size, square_size)
