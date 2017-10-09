import random

import pytest

from class_excercise import add, subtract, multiply, divide


def test_add():
    maximum = 5e15
    minimum = -5e15
    for i in range(1000):
        a = random.uniform(minimum, maximum)
        b = random.uniform(minimum, maximum)
        assert add(a, b) == a + b


def test_subtract():
    maximum = 5e15
    minimum = -5e15
    for i in range(1000):
        a = random.uniform(minimum, maximum)
        b = random.uniform(minimum, maximum)
        assert subtract(a, b) == a - b


def test_multiply():
    maximum = 5e15
    minimum = -5e15
    for i in range(1000):
        a = random.uniform(minimum, maximum)
        b = random.uniform(minimum, maximum)
        assert multiply(a, b) == a * b


def test_divide():
    maximum = 5e15
    minimum = -5e15
    for i in range(1000):
        a = random.uniform(minimum, maximum)
        b = random.uniform(minimum, maximum)
        if b == 0:  # Minuscule but non-zero probability.
            continue
        assert divide(a, b) == a / b
    a = random.uniform(minimum, maximum)
    with pytest.raises(AssertionError):
        divide(a, 0)
