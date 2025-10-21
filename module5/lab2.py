import random

numbers = []

no = input('Enter number, empty to stop: ')

while no != '':
    numbers.append(int(no))
    no = input('Enter number, empty to stop: ')

numbers.sort()

printed = numbers[-1] + 1
for number in numbers:
    if printed != number and number > 100:
        print(number)
        printed = number


























