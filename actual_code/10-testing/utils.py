# Test Driven Development - TDD
# Red->Green->Refactor

def add(a, b):
    if type(a) not in (int, float):
        raise TypeError("a must be a number")
    if type(b) not in (int, float):
        raise TypeError("b must be a number")
    return a + b
