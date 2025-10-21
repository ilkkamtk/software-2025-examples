phone_book = {}

while True:
    action = input("add, search, quit: ")
    if action == "add":
        name = input("Contact's name: ")
        phone = input("Contact's phone number: ")
        phone_book[name] = phone
    elif action == "search":
        name = input("Contact's name: ")
        if name in phone_book:
            print(f"{name}'s phone number is {phone_book[name]}.")
        else:
            print("Name not found")
    else:
        print("Program quit")
        break