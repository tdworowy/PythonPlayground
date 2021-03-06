import matplotlib.pyplot as plt
import numpy as np


def plot_bifurcation_diagram(map_function, n: int = 10000, iterations: int = 1000):
    r = np.linspace(2.5, 4.0, n)
    last = 100
    x = 1e-5 * np.ones(n)
    lyapunov = np.zeros(n)
    fig, (ax1, ax2) = plt.subplots(2, 1,
                                   figsize=(8, 9),
                                   sharex=True)
    for i in range(iterations):
        x = map_function(r, x)
        lyapunov += np.log(abs(r - 2 * r * x))
        if i >= (iterations - last):
            ax1.plot(r, x, ',k', alpha=.25)
    ax1.set_xlim(2.5, 4)
    ax1.set_title("Bifurcation diagram")

    ax2.axhline(0, color='k', lw=.5, alpha=.5)
    ax2.plot(r[lyapunov < 0],
             lyapunov[lyapunov < 0] / iterations,
             '.k', alpha=.5, ms=.5)
    ax2.plot(r[lyapunov >= 0],
             lyapunov[lyapunov >= 0] / iterations,
             '.r', alpha=.5, ms=.5)
    ax2.set_xlim(2.5, 4)
    ax2.set_ylim(-2, 1)
    ax2.set_title("Lyapunov exponent")
    plt.tight_layout()
    return plt


def logistic_map(r: float, x: float):
    return r * x * (1 - x)


if __name__ == "__main__":
    plot_bifurcation_diagram(logistic_map).savefig('logistic_map_bifurcation_diagram.png')
