file = open("file1.txt")  # file handle!


print(file.read())  # get whole of the file as a string
file.seek(0)

lines = file.readlines()  # a list where each element is a line in the file
print(lines)
for line in lines:
    print(line.strip())  # removes whitespace (from the start and end), newline characters
file.seek(0)

print(file.readline().strip())
print(file.readline().strip())
print(file.readline().strip())
print(file.readline().strip())
print(bool(file.readline().strip()))

file.seek(0)
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()


file.close()

# utf-8