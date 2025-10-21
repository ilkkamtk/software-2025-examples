number = int(input("Enter a number: "))
prime = 'Is a '


if number <= 2:
    prime = 'Not a '
else:
     for i in range(2, number):
        if number % i == 0:
            prime = 'Not a '
            break


print(f"{prime} prime number")