from classes.car import Car
import random
from tabulate import  tabulate
car_list = []

for i in range(10):
    # randomise max speed here
    max_speed = random.randint(100, 200)
    car = Car('ABC-' + str(i + 1), max_speed)
    car_list.append(car)

# race = game loop
race_distance = 0
while race_distance < 10000:
    for car in car_list:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

    # check for a winner
    # if one of the cars distance > 10000, set that to race_distance (or if while True, break)
    for car in car_list:
        if car.travelled_distance >= 10000:
            race_distance = car.travelled_distance

# print results in a nice table
car_list.sort(key=lambda car: car.travelled_distance, reverse=True)

cars_as_list = []
for car in car_list:
    cars_as_list.append(car.getlist())

print(tabulate(cars_as_list, headers = ['Registartion number', 'Max speed', 'Current speed', 'Travelled distance']))