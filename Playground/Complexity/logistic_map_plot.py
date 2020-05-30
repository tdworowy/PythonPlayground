import matplotlib.pyplot as plt


def plot_logistic_map(r: float, x: float, iterations: int):
    iterations_list = []
    results_list = []
    for i in range(iterations):
        x = r * (x - x ** 2)
        results_list.append(x)
        iterations_list.append(i)
    plt.plot(iterations_list, results_list)
    plt.show()


plot_logistic_map(2.0, 0.2, 40)  # fix point
plot_logistic_map(3.0, 0.2, 40)  # cyclical
plot_logistic_map(3.5, 0.2, 40)  # cyclical2
plot_logistic_map(4.0, 0.2, 40)  # chaotic
plot_logistic_map(4.0, 0.3, 40)  # chaotic2
