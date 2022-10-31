# type:ignore
# create a rose curve in polar coordinates and
# add widgets that can control the curve parameters
# such as buttons and sliding bars

from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np


def update(val):
    # update the curve with the new parameters
    # and redraw the canvas
    print("update")
    n, d = int(slider1.val), int(slider2.val)
    theta = np.linspace(0, d/n*50*np.pi, 10000)
    r = np.cos(theta * n / d)
    line.set_data(theta, r)
    fig.canvas.draw_idle()


# main
fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(1, 1, 1, polar=True)
ax.set_title("Rose Curve", pad=20)

n, d = 3, 9
theta = np.linspace(0, d/n*50*np.pi, 10000)
r = np.cos(theta * n / d)
line, = ax.plot(theta, r, color='red')

plt.subplots_adjust(left=0.25, bottom=0.25)
slider1_ax = plt.axes([0.25, 0.15, 0.65, 0.03])
slider2_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
slider1 = Slider(slider1_ax, 'n value', 1, 13, valinit=n, valfmt="%i")
slider2 = Slider(slider2_ax, 'd value', 1, 12, valinit=d, valfmt="%i")
slider1.on_changed(update)
slider2.on_changed(update)


plt.show()
