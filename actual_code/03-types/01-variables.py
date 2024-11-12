print("Hello, world!")


# every variable has a value and a type.
user_first_name = "Bachir"  # all lower case, separated by underscores
print("Hello, " + user_first_name)
print(type(user_first_name))  # str -> string -> text
print(user_first_name.find("a"))

# 012345
# Bachir

print(user_first_name.find("ach"))  # returns the index where the string starts
print(user_first_name.find("banana"))  # returns -1 when it can't be found





user_first_name = 7337
print(user_first_name)
print(type(user_first_name))  # int -> integer -> whole number

user_first_name = 73.37
print(user_first_name)
print(type(user_first_name))  # float -> floating point number -> decimal number/non-whole number

name = "Kevin"
print("Hello, " + name)

name = "Zoe"
print("Hello, " + name)
