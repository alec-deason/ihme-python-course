import random

from C import inplace_bubble_sort

def test_inplace_bubble_sort():
    for i in range(100):
        l = list(range(i))
        random.shuffle(l)
        sorted_l = sorted(list(l))
        inplace_bubble_sort(l)
        assert l == sorted_l
