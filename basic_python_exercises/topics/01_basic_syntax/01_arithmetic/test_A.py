from A import sqrt


def test_sqrt():
    for a in range(1, 100):
        a /= 2
        assert sqrt(a*a) == a
    assert sqrt(-1) == 'cannot take the square root of a negative'

