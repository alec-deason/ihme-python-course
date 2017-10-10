import re

from B import reverse_string, count_occurrences


def test_reverse_string():
    for s in ['thing', 'foo bar', 'b'*100000, '']:
        assert reverse_string(s) == ''.join(reversed(s))


def test_count_occurrences():
    for haystack in ['there are three fish in the fishy fish bowl', 'a'*10000, '', 'foobar']:
        for needle in ['fish', 'foo', 'a', 'whumpus']:
            assert count_occurrences(needle, haystack) == len(re.findall(needle, haystack))
