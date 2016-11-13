
class PID(object):

	def __init__(self, kp, ki, kd):
		self.kp = kp;
		self.ki = ki;
		self.kd = kd;
    	self.last_sample = 0
    	self.last_process = 0

    #PID implementation
	def process(self, set_point, sample):
		error = set_point - sample
		delta_time = (millis() - self.last_process) / 1000.0
		self.last_process = millis()

		p = error * self.kp

		i = i + (error * self.ki) * delta_time

		d = (self.last_sample - sample) * self.kd / deltaTime
		self.last_sample = sample

		pid = p + i + d

		return pid


my_pid = PID(1.0, 0, 0)

pwm_control = 50

def loop(self):
	# reads the distance
	distance_from_goal = ???
	# sets the sample
	my_pid.sample(distance_from_goal)
	# converts to pwm
	pwm_control = (my_pid.process() + 50)
	# Saída do controle
	return pwm_control
