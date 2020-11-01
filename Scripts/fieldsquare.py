import matplotlib.pyplot as plt
import numpy as np

import main

s = 10
n = 40


def fieldsquare():
    xrange = np.linspace(1, s + 1, n)
    yrange = np.linspace(1, s + 1, n)

    xx, yy = np.meshgrid(xrange, yrange)

    z = fn(xx, yy)
    z = z / np.max(z)

    for xi in range(0, n):
        for yi in range(0, n):
            colour = np.array([[1, 1, 1]]) * z[xi, yi]
            plt.scatter(xrange[xi], yrange[yi], c=colour, s=2)

    plt.axis('off')

    name = "fieldsquare"

    plt.savefig(main.basepath + name + ".pdf")


def fn(xx, yy):
    # return np.abs((xx ** 2) * np.sin((yy ** 3) / xx))
    return np.abs(np.sin(xx)+ np.exp(yy))
