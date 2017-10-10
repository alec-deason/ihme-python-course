from functools import reduce


def between_sets(A, B):
    d = 0
    def lcm(a, b):
        def gcd(a, b):
            while is_even(a) and is_even(b):
                a = a/2
                b = b/2
                d = d + 1
            while a != b:
                is_even = (a % 2 == 0)
                if is_even:
                    a = a/2
                elif b % 2 == 0:
                    b = b/2
                elif a > b:
                    a = (a - b)/2
                else:
                    b = (b - a)/2
            return a * 2**d

        def is_even(a):
            return a % 2 == 0

        return a*b // gcd(a, b)
    start = reduce(lcm, A)
    stop = reduce(gcd, B)

    return len([d for d in range(start, stop+1, start) if stop % d == 0])


