# define
def greet():
    print("Hello, how are you?")


greet()  # invoke!
greet()
greet()

def find_average(input_list):
    """
    This is a function to find the average - you must pass a list.
    """
    if type(input_list) is list:
        print(sum(input_list)/len(input_list))
    else:
        print("Sorry - can't do that!")

list_of_lists = [
    [1,2,3,445],
    [12,4,4,6],
    [123,123,124,564],
    [123,123,645,24],
    "This isn't a list!"
]

for value in list_of_lists:
    find_average(value)


def greet(name, custom_greeting):
    print(f"Hello, {name}, how are you? {custom_greeting}")
    # repeat tasks, group together behaviour, share code between different projects

greet("Jena", "Hope you're feeling better - thanks for the typo corrections!")
greet("Daniel", "Do you miss the warmer weather?")

# function func
find_average()
