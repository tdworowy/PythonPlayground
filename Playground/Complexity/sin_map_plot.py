import matplotlib.pyplot as plt
from math import sin, pi
import matplotlib.backends.backend_pdf as pdf
import numpy


def plot_sin_map(r: float, x: float, iterations: int):
    iterations_list = []
    results_list = []
    for i in range(iterations):
        x = r / 4 * sin(pi * x)
        results_list.append(x)
        iterations_list.append(i)

    plt.xlabel("Iterations")
    plt.ylabel(f"R = {r}")
    plt.plot(iterations_list, results_list)
    return plt


if __name__ == "__main__":

    pdf = pdf.PdfPages("sin_map_output.pdf")
    for i in numpy.arange(0.1, 5.0, 0.1):
        pdf.savefig(plot_sin_map(i, .02, 30).gcf())
        plt.clf()
    pdf.close()
