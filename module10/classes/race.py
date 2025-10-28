import random
from tabulate import tabulate

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        # print results in a nice table
        self.cars.sort(key=lambda car: car.travelled_distance, reverse=True)

        cars_as_list = []
        for car in self.cars:
            cars_as_list.append(car.getlist())

        print(tabulate(cars_as_list, headers=['Registartion number', 'Max speed', 'Current speed', 'Travelled distance']))

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)