"""
basic_plot.py

In order to visualize various plots and simulations in Python,
we will make use of the matplotlib.pyplot and matplotlib.animations libraries initially.
As we go along and require more involved graphs, we'll also use seaborn library.

Of course - numpy is an indispensable library that is necessary for it all.
"""

# importing
import matplotlib.pyplot as plt
import numpy as np


def plotting_a_line(m, c):
    """
    plot a simple line in matplotlib.

    :param m: slope
    :param c: y-intercept
    """
    x = np.linspace(0, 100, 101)
    y = m * x + c
    plt.plot(x, y)
    plt.show()


def scatter_plot_line(m, c):
    """
    plot a scatter plot of line in matplotlib.

    :param m: slope
    :param c: y-intercept
    """
    x = np.linspace(0, 100, 50)
    y = m * x + c
    plt.scatter(x, y, c="r", marker="o", alpha=0.6, s=20)
    plt.show()


def plot_a_function(x=np.linspace(0, 2 * np.pi, 50), func=np.sin):
    """
    use the given function to plot on the provided domain.

    :param x: iterable list/array object of domain values
    :param func: function to be plotted. sin function by default.
    """
    x_ = np.array(x)
    y = func(x)

    plt.plot(x_, y)
    plt.show()
