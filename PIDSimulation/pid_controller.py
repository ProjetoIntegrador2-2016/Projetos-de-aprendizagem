#***********************************************************************
# Author: Tainara Santos Reis
# Purpose: Simulate a PID Controller to choose the kp, ki and kd values
#***********************************************************************

class PIDController(object):

    def __init__(self, kp, ki, kd):
		self.kp = kp;
		self.ki = ki;
		self.kd = kd;
    	self.last_error = 0

    #PID implementation
	def process(self, set_point, sample):
        actual_error = set_point - sample
        delta_time = actual_time - previous_time
        error_sum += actual_error * delta_time
        error_derivative = (actual_error - self.last_error) /  delta_time

        pid = self.kp * actual_error + self.ki * error_sum + self.kd * error_derivative

        self.last_error = actual_error

        return actual_error
