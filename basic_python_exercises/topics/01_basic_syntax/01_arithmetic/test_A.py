import math

from A import cos


def test_cos():
    for a in range(-100, 100):
        a /= 2
        assert cos(a) == math.cos(a)

