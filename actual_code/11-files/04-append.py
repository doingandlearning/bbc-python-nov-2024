import datetime

try:
    with open("log.txt", mode="a") as f:
        f.write(f"{datetime.datetime.now()}: This is a log message.\n")
except:
    print("Problem opening file.")