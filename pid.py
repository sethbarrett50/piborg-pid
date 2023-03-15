# Class Containing PID Controller

class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.last_error = 0
        self.integral = 0

    def update(self, error):
        derivative = error - self.last_error
        self.integral += error
        output = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)
        self.last_error = error
        return output