#***********************************************************************
# Author: Tainara Santos Reis
# Purpose: Simulate a PID Controller to choose the kp, ki and kd values
#***********************************************************************

class PIDController(object):

    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.last_error = 0
        self.previous_time = 0
        self.error_sum = 0

    #PID implementation
    def process(self, set_point, sample, actual_time):
        """  Update the Pid loop

        Parameters:
            actual_error      Error since last call = Distance to the set_point
            delta_time        Change in time since last call, in seconds.
            error_sum         Integral of the errors.
            error_derivative  Tax of change
        """
        actual_error = set_point - sample
        delta_time = actual_time - self.previous_time
        self.error_sum += actual_error * delta_time
        error_derivative = (actual_error - self.last_error) /  delta_time

        p = self.kp * actual_error
        i = self.ki * self.error_sum
        d = self.kd * error_derivative

        pid = p + i + d

        self.last_error = actual_error

        return pid, p, i, d
