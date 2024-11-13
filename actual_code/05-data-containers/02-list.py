# mutable, ordered, growable

empty_list = []
print(empty_list)
print(type(empty_list))

beatle_list = ["John", "Paul", "George", "Ringo"]
print(beatle_list[0])
print(beatle_list[1:2])
print(beatle_list[-2:])  # this doesn't change the original list! [start:end:step]
print(beatle_list)
#
print(beatle_list.append("Zoe"))  # adds a single item to the end of the list
print(beatle_list)

print(beatle_list.extend(["Jakob", "Louise"]))  # adds multiple items to my list
print(beatle_list)

print(beatle_list.insert(2, "Shoba"))  # computationally expensive!
print(beatle_list)

print(beatle_list.remove("George"))
print(beatle_list)

if "Daniel" in beatle_list:
    print("Woohoo!")
else:
    print("Awh...")

user_input = ""
favourite_programmes = []  #
while user_input != "done":
    user_input = input("What is a favourite program? (enter done if finished): ")
    favourite_programmes.append(user_input)

print(f"You named {len(favourite_programmes)} programmes - the first was {favourite_programmes[0]}.")

# [] => creates a list
# () => create a tuple

#    tup[0] indexes all of them
#    list[0]