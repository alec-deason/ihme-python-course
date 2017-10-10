from itertools import product
import math

from A import calculator


def test_quadratic_roots():
    for a, b, c in product(range(0, 10), range(0, 10), range(0, 10)):
        if a == 0 or b*b - 4*a*c < 0:
            assert calculator('quadratic_roots', [a, b, c]) == 'roots undefined'
        else:
            x1 = (-b+math.sqrt(b*b - 4*a*c))/(2*a)
            x2 = (-b+math.sqrt(b*b - 4*a*c))/(2*a)
            assert set(calculator('quadratic_roots', [a, b, c])) == set((x1, x2))


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
