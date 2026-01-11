import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x = np.linspace(0, 5 * np.pi, 100)
y = np.sin(x)

fig, axis = plt.subplots()
axis.set_xlim(min(x), max(x))
axis.set_ylim(-1.5, 1.5)
axis.grid(True)
(anim_plot,) = axis.plot([], [])


def update(frames):
    anim_plot.set_data(x[:frames], y[:frames])
    return (anim_plot,)


animation = FuncAnimation(fig, update, len(x), interval=40)
plt.show()
