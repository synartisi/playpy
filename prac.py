import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision = 4)

c = 1

x = np.linspace(0, np.pi, 81)
h = x[1] - x[0]

tf = 2
n_time = 160
k = tf / n_time

lam2 = (c * k / h) ** 2
print(f"lambda ** 2 : {lam2}")

u = np.piecewise(x, [x < np.pi / 2, x >= np.pi / 2], [lambda x: x, lambda x: np.pi - x])

u_next = np.zeros(u.shape)
u_old = np.zeros(u.shape)

t = 0

for it in range(0, n_time):
    t += k
    for ix in range(1, len(x) - 1):
        if it == 0:
            u_next[ix] = lam2 / 2 * u[ix - 1] + (1 - lam2) * u[ix] + lam2 / 2 * u[ix + 1]
        else:
            u_next[ix] = lam2 * u[ix - 1] + 2 * (1 - lam2) * u[ix] + lam2 * u[ix + 1] - u_old[ix]
    u_old = np.copy(u)
    u = np.copy(u_next)
    
print(f"t값 : {t}")
print(f"f값 : {u}")