from itertools import product

from B import calculator

def test_floor_division():
    for a, b in product(range(-100, 100), range(-100, 100)):
        if b == 0:
            assert calculator('floor_division', [a, b]) == 'cannot divide by zero'
        else:
            assert calculator('floor_division', [a, b]) == a // b


def test_add():
    for a, b in product(range(-100, 100), range(-100, 100)):
        assert calculator('add', [a, b]) == a + b


def test_subtract():
    for a, b in product(range(-100, 100), range(-100, 100)):
        assert calculator('subtract', [a, b]) == a - b


def test_multiply():
    for a, b in product(range(-100, 100), range(-100, 100)):
        assert calculator('multiply', [a, b]) == a * b


def test_divide():
    for a, b in product(range(-100, 100), range(-100, 100)):
        if b == 0:
            assert calculator('divide', [a, b]) == 'cannot divide by zero'
        else:
            assert calculator('divide', [a, b]) == a / b
