numbers = set()

no = int(input('Enter number, 0 to stop: '))

while no != 0:
    numbers.add(no)
    no = int(input('Enter number, 0 to stop: '))

print(numbers)