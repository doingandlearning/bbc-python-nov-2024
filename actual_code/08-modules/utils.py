"""
This is a utility module containing helpful tools for this project.
"""


def printer(some_object):
    print("Printer:")
    print(some_object)
    print("All done!")


class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Shape[{self.name}]"


default_shape = Shape("square")

print(f"The __name__ of utils.py is {__name__}")
if __name__ == "__main__":
    print(f"The __name__ of utils.py is {__name__}")
    print("I am in the utils.py file")
    printer(default_shape)
    print("I am about to leave the utils.py file")
