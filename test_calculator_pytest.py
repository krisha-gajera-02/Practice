# pytest

import pytest
import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(5, 2) == 3

@pytest.fixture
def numbers():
    return (10, 5)

def test_multiply(numbers):
    a, b = numbers
    assert calculator.multiply(a, b) == 50

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(10, 0)

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (-1, 1, 0),
    ]
)
def test_add_param(a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.skip(reason="Feature not implemented yet")
def test_skip_example():
    assert True

@pytest.mark.skipif(1 < 0, reason="Condition is false")
def test_skip_if():
    assert calculator.add(1, 1) == 2
