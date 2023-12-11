from math import *

import matplotlib.pyplot as plt


class vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


"""parameters and constants"""

Ixx = 1
Iyy = 2
Izz = 3


"""Define functions"""


def find_omega_dot(w):  # function for finding omegadot using Euler's equations
    wx_dot = (Iyy - Izz) * w.y * w.z / Ixx
    wy_dot = (Izz - Ixx) * w.z * w.x / Iyy
    wz_dot = (Ixx - Iyy) * w.x * w.y / Izz
    w_dot = vector(wx_dot, wy_dot, wz_dot)
    return w_dot


def update_omega(w, wdot):  # updating angular momentum
    w.x = w.x + dt * wdot.x
    w.y = w.y + dt * wdot.y
    w.z = w.z + dt * wdot.z

    return w


t = 0
dt = 0.001
omega = vector(0.1, 4, 0.1)
omega1_list, omega2_list, omega3_list, t_list = list(), list(), list(), list()

while t < 60:
    omega_dot = find_omega_dot(omega)
    w = update_omega(omega, omega_dot)
    omega1_list.append(w.x)
    omega2_list.append(w.y)
    omega3_list.append(w.z)
    t_list.append(t)
    t += dt

# Plot the data
plt.plot(t_list, omega1_list, label="omega1")
plt.plot(t_list, omega2_list, label="omega2")
plt.plot(t_list, omega3_list, label="omega3")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (rad/s)")
plt.legend()
plt.savefig("flip.png")
plt.show()
