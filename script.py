import numpy as np
import matplotlib.pyplot as plt
import sys

# cas
T = 5
# dekla kroku
h = 0.005

# qB/m
c = 10

# array([x, dx/dt, y, dy/dt])
u = np.array([0.0, 0.0, 0.0, 0.02])
uPrew = np.zeros(4)

# logovaci mnoziny
x = []
y = []
time = []


def f(a):
    w = np.zeros(4)
    w[0] = a[1]
    w[1] = c * a[3]
    w[2] = a[3]
    w[3] = -c * a[1]

    return w


# eulerova metoda
def euler(u, h):
    if h <= 0:
        raise Exception("h is not valid")

    return u + h * f(u)


# metoda Leap-Frog
def leapfrog(uPrew, u, h):
    if h <= 0:
        raise Exception("h is not valid")

    return uPrew + 2 * h * f(u)


# Bulirsch-Stoerova Metoda
def bulirsch_stoer(uPrew, u, h):
    if h <= 0:
        raise Exception("h is not valid")

    u_1 = leapfrog(uPrew, u, h)
    u_2 = leapfrog(uPrew, u, 2 * h)

    return (4 / 3) * u_1 - (1 / 3) * u_2


fig, axs = plt.subplots(2, figsize=(15, 4.5))

# pocatecni parametry smycky
t = 0
i = 0

while t < T:
    t = t + h

    uPrew1 = uPrew
    uPrew = u

    if i == 0:
        u = euler(u, h)
    else:
        u = bulirsch_stoer(uPrew1, u, h)

    i = i + 1

    x.append(u[0])
    y.append(u[2])
    time.append(t)

try:
    axs[0].plot(x, y)
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("y")

    axs[1].scatter(time, x, s=2)
    axs[1].set_xlabel("t")
    axs[1].set_ylabel("x")

    plt.show()
except:
    raise Exception("Plot error")

