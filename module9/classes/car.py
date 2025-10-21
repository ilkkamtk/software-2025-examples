class Car:
    def __init__(self, new_registration_number, new_max_speed):
        self.registration_number = new_registration_number
        self.max_speed = new_max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, value):
        self.current_speed = self.current_speed + value
        # if current speed > max speed, set to max speed
        # if current speed < 0, set speed to 0

    def drive(self, time):
        # use time and current speed to calculate driven distance
        # add driven distance to travelled distance
        pass