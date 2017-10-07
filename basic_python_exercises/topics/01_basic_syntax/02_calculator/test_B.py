from itertools import product

from B import calculator

def test_floor_division():
    for a, b in product(range(-100, 100), range(-100, 100)):
        if b == 0:
            assert calculator('flood_division', a, b) == 'cannot divide by zero'
        else:
            assert calculator('floor_division', a, b) == a // b
