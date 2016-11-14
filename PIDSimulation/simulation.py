""" Graphical demonstration of a PID controller
    to find the adequate constants values.
"""

import numpy as np
import matplotlib.pyplot as plt
import pid_controller as pid

pid_controller = pid.PIDController(10, 0, 0)

target_distance = 1000
actual_time = 0
dt = 5
steps = 101
set_point = 0
sample = target_distance
# Create vectors with the same quantity of steps, filled with zeros.
# np.zeros(): https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html
cart_positions = np.zeros(steps)
times = np.zeros(steps)
p_term = np.zeros(steps)
i_term = np.zeros(steps)
d_term = np.zeros(steps)


for i in range(steps) :
    if i == 0:
        cart_positions[i]= set_point
        times[i] = actual_time
        p_term[i] = 0
        i_term[i] = 0
        d_term[i] = 0
    else:
        actual_time += dt
        pid, p_term[i], i_term[i], d_term[i] = pid_controller.process(set_point, target_distance, actual_time)
        print pid

        # suponha que o carrinho andou 10cm
        target_distance -= 10
        cart_positions[i] = cart_positions[i-1] + 10

        times[i] = actual_time

    print cart_positions[i]

plt.subplot(511)
plt.plot(times, cart_positions)
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.grid()

plt.subplot(512)
plt.plot(times, p_term)
plt.xlabel("time (s)")
plt.ylabel("p term (m)")
plt.grid()

plt.subplot(513)
plt.plot(times, i_term)
plt.xlabel("time (s)")
plt.ylabel("i term")
plt.grid()

plt.subplot(514)
plt.plot(times, d_term)
plt.xlabel("time (s)")
plt.ylabel("d term")
plt.grid()

plt.show()
