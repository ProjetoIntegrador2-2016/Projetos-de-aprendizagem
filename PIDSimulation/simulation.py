""" Graphical demonstration of a PID controller
    to find the adequate constants values.
"""

import numpy as np
import matplotlib.pyplot as plt
import pid_controller as pid

pid_controller = pid.PIDController(10, 0, 0)

TARGET_INITIAL_DISTANCE = 100
target_distance = TARGET_INITIAL_DISTANCE
actual_time = 0
dt = 5
steps = 101
# Create vectors with the same quantity of steps, filled with zeros.
# np.zeros(): https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html
cart_position = np.zeros(steps)
times = np.zeros(steps)
p_term = np.zeros(steps)
i_term = np.zeros(steps)
d_term = np.zeros(steps)
set_point = np.zeros(steps)
process_value = np.zeros(steps)
ratio = np.zeros(steps)

for i in range(steps) :
    if i == 0:
        set_point[0]= 0
        cart_position[0]= 0
        process_value[0]= 0
        times[0] = actual_time
        p_term[0] = 0
        i_term[0] = 0
        d_term[0] = 0
    else:
        #Atualize time
        actual_time += dt
        times[i] = actual_time

        #Get pid
        pid, p_term[i], i_term[i], d_term[i] = pid_controller.process(set_point[i], target_distance, actual_time)
        print pid

        #Update cart distance to the target and cart's position
        #Suponha que o carrinho andou 10cm
        target_distance -= 1
        cart_position[i] = cart_position[i-1] + 1

        #The objective is to make the set_point equal to the process_value
        #So the ratio must equal 1.
        set_point[i] =  TARGET_INITIAL_DISTANCE
        process_value[i] = cart_position[i]
        ratio [i] = set_point[i]/process_value[i]

    print cart_position[i]

plt.subplot(511)
plt.plot(times, cart_position)
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

plt.subplot(515)
plt.plot(times, ratio)
plt.xlabel("time (s)")
plt.ylabel("Set Point/Process Value")
plt.grid()

plt.show()

plt.plot(times, cart_position)
plt.plot(times, p_term)
plt.plot(times, i_term)
plt.plot(times, d_term)
plt.legend(['Cart position', 'P', 'I', 'D'], loc='best')
plt.xlabel("time (s)")
plt.ylabel("?")
plt.grid()

plt.show()
