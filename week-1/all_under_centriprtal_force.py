import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

r_0 = np.array([35.0, 0.0])
v_0 = np.array([0.0, 5.0])
speed = np.linalg.norm(v_0)
radius = np.linalg.norm(r_0)
w = speed / radius
dt = 0.01

fig, axis = plt.subplots()
axis.spines["left"].set_position("zero")
axis.spines["bottom"].set_position("zero")
axis.spines["right"].set_position("zero")
axis.spines["top"].set_position("zero")
axis.set_aspect("equal", adjustable="box")
axis.grid(True)
axis.tick_params(labelbottom=False, labelleft=False)
axis.set_xlim(-50, 50)
axis.set_ylim(-50, 50)

anim_plot = plt.scatter(*r_0, zorder=3)


def init():
    anim_plot.set_offsets(r_0)
    return (anim_plot,)


def update(frames):
    t = dt * frames
    acceleration = -(speed**2 / radius**2) * r_0
    v_0[:] += acceleration * dt
    r_0[:] = r_0 + v_0 * dt

    anim_plot.set_offsets(r_0)
    return (anim_plot,)


animation = FuncAnimation(
    fig, update, frames=500, init_func=init, interval=25, blit=True
)
plt.show()
