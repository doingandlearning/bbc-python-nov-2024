import pytest
from utils import add

def test_adding_two_positive_numbers_works():
    # Given
    a = 1
    b = 2
    want = 3
    # When
    got = add(a, b)
    # Then
    assert want == got

def test_adding_two_numbers():
    assert add(1, 2) == 3

def test_adding_two_negative_numbers():
    assert add(-1, -2) == -3

@pytest.mark.parametrize("input1, input2, expected", [
    (1,1,2),
    (0,2,2),
    (-2, 2, 0),
    (1.3, 1.2, 2.5),
    (-0.2, 0.1, -0.1)
])
def test_adding_pairs_of_numbers_works_correctly(input1, input2, expected):
    assert add(input1, input2) == expected

def test_fails_when_trying_to_add_strings():
    with pytest.raises(TypeError):
        add("a", "b")

@pytest.mark.parametrize("input1, input2", [
    ([], []),
    (True, ()),
    ({}, [])
])
def test_fails_when_trying_to_add_anything_not_a_number(input1, input2):
    with pytest.raises(TypeError):
        add(input1, input2)

from utils import multiply

def test_multiplying_two_numbers():
    assert multiply(3, 2) == 6

@pytest.mark.parametrize("input1, input2, expected", [
    (5, 2, 10),
    (0, 5, 0),
    (-1, 3, -3)
])
def test_multiply_various_numbers(input1, input2, expected):
    assert multiply(input1, input2) == expected

def test_multiply_raises_type_error_on_invalid_input():
    with pytest.raises(TypeError):
        multiply("a", "b")


from utils import divide
def test_dividing_two_numbers():
    assert divide(6, 2) == 3

@pytest.mark.parametrize("input1, input2, expected", [
    (10, 2, 5),
    (-6, 2, -3),
    (0, 1, 0)
])
def test_divide_various_numbers(input1, input2, expected):
    assert divide(input1, input2) == expected

def test_divide_raises_type_error_on_invalid_input():
    with pytest.raises(TypeError):
        divide("a", "b")

def test_divide_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)