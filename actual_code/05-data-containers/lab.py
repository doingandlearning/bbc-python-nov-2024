readings = []

while True:
    input_string = input('Please enter a temperature reading (-1 to end): ')
    if input_string == '-1':
        break
    # TODO: make negatives work!
    elif input_string.count('.') > 1 or not input_string.replace('.', '').isdigit():  # defensive programming
        print('Must be a positive floating point number')
    else:
        reading = float(input_string)
        readings.append(reading)

summary_stats = {
    "length": len(readings),
    "sum": sum(readings),
    "average": sum(readings)/len(readings),
    "min": min(readings),
    "max": max(readings)
}

print(f"You entered {summary_stats["length"]} readings.")
print(f"Your readings totalled {summary_stats["sum"]}.")
print(f"The average: {summary_stats["average"]}")
print(f"The max was {max(readings)} and the min was {min(readings)}")


