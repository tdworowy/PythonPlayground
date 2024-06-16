import random
from itertools import permutations
from typing import Callable, Iterable

import matplotlib.pyplot as plt
from Playground.my_utils.staff.timer3 import timer3

from collections import Counter

seed = 111
width = 500
height = 300


def distance_tour(a_tour: list) -> int:
    return sum(distance_point(a_tour[i - 1], a_tour[i]) for i in range(len(a_tour)))


def distance_point(first: int, second: int) -> int:
    return abs(first - second)


def generate_cities(number: int) -> frozenset:
    random.seed((number, seed))
    return frozenset(
        complex(random.randint(1, width), random.randint(1, height))
        for c in range(number)
    )


def shortest_tout(tours):
    return min(tours, key=distance_tour)


def visualize_tour(tour, style="bo-"):
    if len(tour) > 1000:
        plt.figure(figsize=(15, 10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, "rd")
    plt.show()


def visualize_segment(segment, style="bo-"):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
    plt.axis("scaled")
    plt.axis("off")


def X(city):
    return city.real


def Y(city):
    return city.imag


def first(collection: Iterable):
    return next(iter(collection))


def nearest_neighbor(current_city, cities: Iterable):
    return min(cities, key=lambda city: distance_point(city, current_city))


def brute_force(cities: frozenset):
    return shortest_tout(permutations(cities))


def greedy_algorithm(cites, start=None):
    city = start or first(cites)
    tour = [city]
    unvisited = set(cites - {city})
    while unvisited:
        city = nearest_neighbor(city, unvisited)
        tour.append(city)
        unvisited.remove(city)
    return tour


@timer3
def tsp(algorithm: Callable, cities: Iterable):
    tour = algorithm(cities)
    assert Counter(tour) == Counter(cities)
    return tour


if __name__ == "__main__":
    print("Brute Force")
    tour = tsp(brute_force, generate_cities(10))
    visualize_tour(tour)

    print("Greedy algorithm")
    tour = tsp(greedy_algorithm, generate_cities(2000))
    visualize_tour(tour)
