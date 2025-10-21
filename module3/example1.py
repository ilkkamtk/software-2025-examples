age = int(input("What is your age: "))

if age < 18:
    print("You are not old enough to vote.")
    difference = 18 - age
    print(f"You have {difference} years to legal age.")
else:
    print("You are old enough to vote.")
