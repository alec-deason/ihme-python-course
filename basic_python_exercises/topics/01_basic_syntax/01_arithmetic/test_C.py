from .C import perfect_squares

def test_perfect_squares():
    for limit in range(0, 200):
        squares = set()
        i = 0
        while True:
            square = i*i
            if square < limit:
                squares.add(square)
                i += 1
            else:
                break
        assert perfect_squares(limit) == (len(squares), sum(squares))
