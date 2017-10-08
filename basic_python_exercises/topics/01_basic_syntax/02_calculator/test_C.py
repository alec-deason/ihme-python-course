from itertools import product

from C import calculator

def test_prime_factors():
    for a in range(0, 100):
        prime_factors = []
        for i in range(2, a+1):
            if a % i == 0:
                is_prime = True
                for p in prime_factors:
                    if i % p == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_factors.append(i)
        assert calculator('prime_factors', [a]) == sum(prime_factors) + 1


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
