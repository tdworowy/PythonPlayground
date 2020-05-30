from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pdf
import numpy


def plot_staff(r: float, x: float, iterations: int):
    iterations_list = []
    results_list = []
    x1 = x2 = x
    for i in range(iterations):
        x1 = r / 4 * sin(pi * x1)
        x2 = r * (x2 - x2 ** 2)
        results_list.append(x1)
        iterations_list.append(x2)
    plt.xlabel(f"{r}/4* sin(pi * {x1})")
    plt.ylabel(f"{r} * ({x2} - {x2} ** 2)")
    plt.plot(iterations_list, results_list)
    return plt


pdf = pdf.PdfPages("experiment _1_output.pdf")
for i in numpy.arange(0.1, 5.0, 0.1):
    for j in numpy.arange(0.1, 0.9, 0.1):
        pdf.savefig(plot_staff(i, j, 10).gcf())
        plt.clf()
pdf.close()