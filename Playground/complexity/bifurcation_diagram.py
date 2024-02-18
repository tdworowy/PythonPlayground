import matplotlib.pyplot as plt
import numpy as np

x_lower_lim = 2.8  # 2.5
x_upper_lim = 4  # 4


def plot_bifurcation_diagram(map_function, n: int = 100000, iterations: int = 10000) -> plt:
    r = np.linspace(x_lower_lim, x_upper_lim, n, dtype=np.float64)
    last = 1000
    x = 1e-5 * np.ones(n, dtype=np.float64)
    lyapunov = np.zeros(n, dtype=np.float64)
    fig, (ax1, ax2) = plt.subplots(2, 1,
                                   figsize=(16, 18),
                                   sharex=True)

    ax1.set_title("Bifurcation diagram")
    for i in range(iterations):
        x = map_function(r, x)
        lyapunov += np.log(abs(r - 2 * r * x), dtype=np.float64)
        if i >= (iterations - last):
            ax1.plot(r, x, ',k', alpha=.25)
    ax1.set_xlim(x_lower_lim, x_upper_lim)

    ax2.set_title("Lyapunov exponent")
    ax2.axhline(0, color='k', lw=.5, alpha=.5)
    ax2.plot(r[lyapunov < 0],
             lyapunov[lyapunov < 0] / iterations,
             '.k', alpha=.5, ms=.5)
    ax2.plot(r[lyapunov >= 0],
             lyapunov[lyapunov >= 0] / iterations,
             '.r', alpha=.5, ms=.5)
    ax2.set_xlim(x_lower_lim, x_upper_lim)
    ax2.set_ylim(-2, 1)

    plt.tight_layout()
    return plt


def logistic_map(r: np.ndarray, x: np.ndarray) -> np.ndarray:
    return r * x * (1 - x)


if __name__ == "__main__":
    plot_bifurcation_diagram(logistic_map).savefig('logistic_map_bifurcation_diagram.png')
