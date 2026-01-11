import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

dt = 0.03
k = 2 / np.pi
w = 2 * np.pi

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
fig, axis = plt.subplots()
axis.grid()
axis.set_xlim(min(x), max(x))
axis.set_ylim(-2, 2)

axis.spines["left"].set_position("zero")
axis.spines["bottom"].set_position("zero")
axis.spines["top"].set_color("none")
axis.spines["right"].set_color("none")
axis.tick_params(labelbottom=False, labelleft=False)
(anim_plot,) = axis.plot([], [])


def update(frames):
    t = dt * frames
    y = np.sin(k * x - w * t)
    anim_plot.set_data(x, y)
    return (anim_plot,)


animation = FuncAnimation(fig, update, frames=400, interval=25)
plt.show()
