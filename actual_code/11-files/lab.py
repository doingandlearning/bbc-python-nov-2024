from datetime import datetime

print(datetime.today())

with open("date.txt", "a") as f:
    print("Writing today's date")
    f.write(f"{datetime.today()}\n")

with open("date.txt") as f:
    for line in f.readlines():
        date_string = line.strip()
        print(date_string)
        print(type(date_string))

        date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")
        print(type(date))
