valid_data = False

while not valid_data:
    age = input("Please enter your age: ")
    if not age.isnumeric():
        print("You need to give me a number which is greater than zero.")
    else:
        age = int(age)
        if age < 0 or age > 120:  # Invalid  Invalid
            print("Invalid age")
        else:
            valid_data = True

print("All done!")