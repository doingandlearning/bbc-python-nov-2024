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
