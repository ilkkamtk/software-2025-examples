consumption = float(input("Monthly consumption in kWh: "))

total = 0
first_50 = 50 * 0.1
next_150 = 150 * 0.08

if consumption >= 200:
    over_200 = (consumption - 200) * 0.06
    total = first_50 + next_150 + over_200
elif consumption > 50:
    over_50 = (consumption - 50) * 0.08
    total = first_50 + over_50
else:
    total = consumption * 0.1

print(f"Total cost: {total}€")