from classes.car import Car

car_list = []

for i in range(10):
    # randomise max speed here
    max_speed = 0
    car = Car('ABC-' + str(i + 1), max_speed)
    car_list.append(car)

# race = game loop
race_distance = 0
while race_distance < 10000:
    for car in car_list:
        # accelerate car with random value -15 to 10
        # drive one hour

    # check for a winner
    # if one of the cars distance > 10000, set that to race_distance (or if while True, break)


# print results in a nice table
# google for table libraries