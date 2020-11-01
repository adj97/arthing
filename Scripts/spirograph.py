import matplotlib.pyplot as plt
import numpy as np
import main


def spirograph():
    tf = 500
    nt = tf*100

    l = 10

    r1 = 5
    w1 = np.random.rand()
    r2 = np.random.rand()+1
    w2 = np.random.rand()

    fx = -(r1+r2+1)
    fy = 0

    for t in np.linspace(0, tf, nt):
        cx = r1 * np.cos(2 * np.pi * t * w1)
        cy = r1 * np.sin(2 * np.pi * t * w1)

        cx += r2 * np.cos(2 * np.pi * t * w2)
        cy += r2 * np.sin(2 * np.pi * t * w2)

        vx = fx - cx
        vy = fy - cy

        modv = np.sqrt(vx ** 2 + vy ** 2)

        ux = vx / modv
        uy = vy / modv

        if t > 0:
            dx_old = dx
            dy_old = dy

        dx = cx + l * ux
        dy = cy + l * uy

        if t > 0:
            x = [dx_old, dx]
            y = [dy_old, dy]
            plt.plot(x, y, c='k', linewidth=0.1)

    plt.plot(fx,fy, c='k')

    plt.axis('off')

    name = "spirograph2"

    plt.savefig(main.basepath + name + ".pdf")
