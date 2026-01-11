import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import numpy as np

w = np.pi
dt = 0.01
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

for ax in fig.axes:
    ax.grid()
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    ax.set_aspect("equal", adjustable="box")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.tick_params(labelbottom=False, labelleft=False)

# define a circle
circle = Circle((0, 0), 1, fill=False, zorder=1)
ax1.add_patch(circle)

anim_plot_ax1 = ax1.scatter([], [], zorder=3, s=50)
anim_plot_ax2 = ax2.scatter([], [], zorder=3, s=50)


def init():
    anim_plot_ax1.set_offsets([[1, 0]])
    anim_plot_ax2.set_offsets([[1, 0]])
    return (anim_plot_ax1, anim_plot_ax2)


def update(frames):
    t = frames * dt
    x = np.cos(w * t)
    y = np.sin(w * t)
    anim_plot_ax1.set_offsets([[x, y]])
    anim_plot_ax2.set_offsets([[x, y]])

    return (anim_plot_ax1, anim_plot_ax2)


animation = FuncAnimation(
    fig, update, frames=400, interval=25, init_func=init, blit=True
)
plt.show()
