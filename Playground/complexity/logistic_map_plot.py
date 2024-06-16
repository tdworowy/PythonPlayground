import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pdf
import numpy


def plot_logistic_map(r: float, x: float, iterations: int):
    iterations_list = []
    results_list = []
    for i in range(iterations):
        x = r * (x - x**2)
        results_list.append(x)
        iterations_list.append(i)

    plt.xlabel("Iterations")
    plt.ylabel(f"R = {r}")
    plt.plot(iterations_list, results_list)

    return plt


if __name__ == "__main__":
    pdf = pdf.PdfPages("logistic_map_output.pdf")
    for i in numpy.arange(0.1, 5.0, 0.1):
        pdf.savefig(plot_logistic_map(i, 0.02, 30).gcf())
        plt.clf()
    pdf.close()
