from itertools import product
import math

from A import calculator

def test_quadratic():
    for a, b, c in product(range(0, 10), range(0, 10), range(0, 10)):
        if a == 0:
            assert calculator('quadratic', a, b, c) == 'a cannot be zero'
        else:
            x1 = (-b+math.sqrt(b*b - 4*a*c))/(2*a)
            x2 = (-b+math.sqrt(b*b - 4*a*c))/(2*a)
            assert set(calculator('quadratic', a, b, c)) == set((x1, x2))
