fruits = []

for _ in range(3):
    fruit = input('Name of the fruit: ')
    amount = float(input('Amount in kg: '))
    date = input('Date of picking: ')
    fruits.append(
        {
            "name": fruit,
            "amount": amount,
            "date": date
        }
    )

print(fruits)