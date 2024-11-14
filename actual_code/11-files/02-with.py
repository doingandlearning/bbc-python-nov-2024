# context handler - automatically closes
try:
    with open("file2.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Oops - looks like that file isn't there! Are you in the right directory?")

