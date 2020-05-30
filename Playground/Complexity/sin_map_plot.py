import matplotlib.pyplot as plt
from math import sin, pi

def plot_sin_map(r: float, x: float, iterations: int):
    iterations_list = []
    results_list = []
    for i in range(iterations):
        x = r/4 * sin(pi *x)
        results_list.append(x)
        iterations_list.append(i)

    plt.plot(iterations_list, results_list)
    plt.show()


plot_sin_map(2.0, 0.2, 40)  # fix point
plot_sin_map(3.0, 0.2, 40)  # cyclical
plot_sin_map(3.5, 0.2, 40)  # cyclical2
plot_sin_map(4.0, 0.2, 40)  # chaotic
plot_sin_map(4.0, 0.3, 40)  # chaotic2
