import matplotlib.pyplot as plt
import numpy as np
import main


def circle(n=10, b=5):

    x_off = []
    y_off = []

    for x in range(b):
        for y in range(b):
            x_off.append(2*x)
            y_off.append(2*y)

    for i in range(b*b):
        x = np.random.rand(n) + x_off[i]
        y = np.random.rand(n) + y_off[i]
        c = np.random.rand(n, 3)
        s = [2**p for p in range(len(x))]
        plt.scatter(x, y, c=c, s=s, alpha=0.7, edgecolors='none')

    plt.axis('off')

    name = "test2"

    plt.savefig(main.basepath + name + ".pdf")
