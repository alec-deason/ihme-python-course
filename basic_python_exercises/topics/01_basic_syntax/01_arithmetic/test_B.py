from itertools import product

from B import quadratic


def test_quadratic():
    for a, b, c in product(range(0, 10), range(0, 10), range(0, 10)):
        if a == 0:
            assert quadratic(a, b, c) == 'a cannot be zero'
        else:
            x1 = (-b+math.sqrt(b*b - 4*a*c))/(2*a)
            x2 = (-b+math.sqrt(b*b - 4*a*c))/(2*a)
            assert set(quadratic(a, b, c)) == set((x1, x2))
