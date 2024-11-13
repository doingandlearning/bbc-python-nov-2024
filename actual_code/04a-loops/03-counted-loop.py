for something in range(10):
    print(10 - something)

print(0)
print("Blast off!")

# n = int(input("How many squares to you want to see? "))
# for i in range(1, n + 1):  # 1 to n (0 to n-1)
#     print(i**2, end=" ")

rows = int(input("How many rows do you want? "))

for i in range(rows, 0, -1):
    print("*" * i)

for i in range(rows):
    print("*" * i)