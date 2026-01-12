import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import numpy as np

dt = 0.01
w = np.pi
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(10, 4))

for ax in fig.axes:
    ax.grid(True)
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    ax.set_aspect("equal", adjustable="box")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    circle = Circle((0, 0), 1, fill=False, zorder=1)
    ax.add_patch(circle)
    ax.tick_params(labelbottom=False, labelleft=False)

anim_plot_ax1, anim_plot_ax2, anim_plot_ax3 = (
    ax1.scatter([1], [0], zorder=3, s=50),
    ax2.scatter([1], [0], zorder=3, s=50),
    ax3.scatter([0], [0], zorder=3, s=50),
)

(line_ax1,) = ax1.plot([0, 1], [0, 0], zorder=2)
(line_ax2,) = ax2.plot([0, 1], [0, 0], zorder=2)
(line_ax3,) = ax3.plot([0, 0], [0, 1], zorder=2)


def init():
    anim_plot_ax1.set_offsets([[1, 0]])
    anim_plot_ax2.set_offsets([[1, 0]])
    anim_plot_ax3.set_offsets([[0, 0]])

    line_ax1.set_data([0, 1], [0, 0])
    line_ax2.set_data([0, 1], [0, 0])
    line_ax3.set_data([0, 0], [0, 0])

    return (anim_plot_ax1, anim_plot_ax2, anim_plot_ax3, line_ax1, line_ax2, line_ax3)


def update(frames):
    t = frames * dt
    x = np.cos(w * t)
    y = np.sin(w * t)

    anim_plot_ax1.set_offsets([[x, 0]])
    anim_plot_ax2.set_offsets([[x, y]])
    anim_plot_ax3.set_offsets([[0, y]])

    line_ax1.set_data([0, x], [0, 0])
    line_ax2.set_data([0, x], [0, y])
    line_ax3.set_data([0, 0], [0, y])

    return (anim_plot_ax1, anim_plot_ax2, anim_plot_ax3, line_ax1, line_ax2, line_ax3)


animation = FuncAnimation(
    fig, update, frames=400, interval=20, init_func=init, blit=True
)
plt.show()
