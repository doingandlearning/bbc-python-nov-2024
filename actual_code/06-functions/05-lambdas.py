def square(n):
    # can do lots of things here!
    return n * n

my_func_2 = lambda x: x * x

def cube(n):
    return n ** 3

cube = lambda n: n ** 3


list_of_num = [1,2,3,4,5,6,7]

print(list(map(lambda x: x ** 4, list_of_num)))

# the problem - i'm creating function only so I can pass it as an argument to something else!
# lambda - anonymous functions!

my_func = lambda: print("Hello!")
my_func_3 = lambda name, greeting: f"{greeting}, {name} - glad you're here!"
print(my_func_2(4))
print(my_func_3("Meriem", "Gutentag"))

## Take a function from the last lab - and try to turn into a lambda.