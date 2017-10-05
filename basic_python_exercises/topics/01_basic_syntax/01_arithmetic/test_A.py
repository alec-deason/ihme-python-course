from A import add


def test_add():
    for a, b in product(range(-100, 100), range(-100, 100)):
        assert add(a, b) == a + b

