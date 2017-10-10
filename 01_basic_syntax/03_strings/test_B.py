import re

from B import reverse_string, swap_characters


def test_reverse_string():
    for s in ['thing', 'foo bar', 'b'*100000, '']:
        assert reverse_string(s) == ''.join(reversed(s))


def test_swap_characters():
    for s in ['thing', 'foo bar', 'b'*100000, '']:
        swapped = ''.join([s[i+1]+s[i] for i in range(0,len(s)-1,2)])
        if len(s) % 2 != 0:
            swapped = swapped+s[-1]
        assert swap_characters(s) == swapped
