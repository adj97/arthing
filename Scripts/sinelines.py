import matplotlib.pyplot as plt
import numpy as np

import main


def sineline():
    n = 100

    for i in range(n):
        x = np.linspace(0, 2 * np.pi, 10*n)
        y = i*np.sin(x)*np.exp(-x)
        plt.plot(x, y, c='black', linewidth=0.01)

    plt.axis('off')

    name = "sineline"

    plt.savefig(main.basepath + name + ".pdf")
