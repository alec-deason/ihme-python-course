from individual_exercise import between_sets


def test_1():
    A = (2, 4)
    B = (16, 32, 96)
    assert between_sets(A, B) == 3


def test_2():
    A = (100, 99, 98, 97, 96, 95, 94, 93, 92, 91)
    B = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert between_sets(A, B) == 0


def test_3():
    A = (2, )
    B = (20, 30, 12)
    assert between_sets(A, B) == 1


def test_4():
    A = (3, 9, 6)
    B = (36, 72)
    assert between_sets(A, B) == 2


def test_5():
    A = (1, )
    B = (100, )
    assert between_sets(A, B) == 9


def test_6():
    A = (51, )
    B = (50, )
    assert between_sets(A, B) == 0


def test_6():
    A = (2, 3, 6)
    B = (42, 84)
    assert between_sets(A, B) == 2


def test_7():
    A = (1, )
    B = (72, 48)
    assert between_sets(A, B) == 8
