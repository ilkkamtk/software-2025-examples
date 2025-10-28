from classes.race import Race
from classes.car import Car
import random

cars = [Car(f"C{i+1}", random.randint(100, 200)) for i in range(10)]

race = Race("Grand Demolition Derby", 8000, cars)
hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print('-------------------- STATUS ------------------')
        race.print_status()

print("\n🏁 Race finished!")
race.print_status()