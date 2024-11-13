def print_and_return_square(num):
    # print(num**2)
    return num ** 2

print(print_and_return_square(7) + 1)

# encapsulating

def get_user_readings():
    readings = []

    while True:
        input_string = input('Please enter a positive temperature reading (-1 to end): ')
        if input_string == '-1':
            break
        elif input_string.count('.') > 1 or not input_string.replace('.', '').isdigit():  # defensive programming
            print('Must be a positive floating point number')
        else:
            reading = float(input_string)
            readings.append(reading)

    return readings

def find_average(input_list):
    if type(input_list) is list:
        return sum(input_list)/len(input_list)
    else:
        print("Sorry - can't do that!")

# This is all I have to write!
# user_readings = get_user_readings()
# print(find_average(user_readings))

# Is this readable??
print(find_average(get_user_readings()))
