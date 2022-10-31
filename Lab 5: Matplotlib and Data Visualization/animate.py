
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
plt.title("Graph Animation")

x = np.arange(0, 2*np.pi, 0.01)
plt.xlim(0, 2*np.pi)
plt.ylim(-3, 3)
sin, = ax.plot(x, np.sin(x), color='red')
cos, = ax.plot(x, np.cos(x), color='green')
diagnal, = ax.plot(x, np.sin(x), color='blue')
topsin, = ax.plot(x, np.sin(x), color='red')
topcos, = ax.plot(x,  np.cos(x), color='green')


def animate(i):
    sin.set_ydata(np.sin(x * i / 20 + i / 10) - 2)
    cos.set_ydata(np.cos(x + i / 10) - 2)
    diagnal.set_ydata(np.sin(x * 10 + (i / 5)) + x - 4)
    topsin.set_ydata(np.sin(x * i / 20 + i / 10) + 2)
    topcos.set_ydata(np.cos(x + i / 10) + 2)

    return sin, cos, topsin, topcos, diagnal


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)

plt.show()
