import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter number of sides on the die: "))
print(f"Rolling until {sides} appears....")

r = 0
while r != sides:
    r = roll_dice(sides)
    print(r)