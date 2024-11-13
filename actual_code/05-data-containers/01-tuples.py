# immutable, ordered, indexed

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

print(empty_tuple.count("Kevin"))
#          0  1  2  3  4  5
tuple_1 = (1, 3, 5, 7, 9, 11)
print(tuple_1)
print(type(tuple_1))
print(tuple_1[0])
print(tuple_1[1:3])  # [start:end]  [inclusive:exclusive]
print(tuple_1[1:5:3])
print(len(tuple_1))

print(4 in tuple_1)
print(5 in tuple_1)

for number in tuple_1:
    print(number)

# user_input = int(input("Give me a positive integer less than 12: "))
# if user_input < 12:
#     if user_input in tuple_1:
#         print("That is an odd number")
#     else:
#         print("That is an even number")
# else:
#     print("Sorry that number is too big.")

tuple_2 = (tuple_1, ("Meriem", "Bachir", "Harry"), (True, 1, "Anything"))
print((tuple_2[2][2], tuple_2[1][2]))
