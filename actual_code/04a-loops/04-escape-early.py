# continue

# break
stop_number = int(input("What number should we stop at?"))

for i in range(100):
    print(i)
    if i == stop_number:
        break  # exits the loop - for/while - early!

print("I will run after the break!")

num = 1
while num <= 10:
    if num % 5 == 0:
        num += 1
        continue  # skips the rest of hte current cycle and jumps but up to the test
    print(num)
    num += 1


