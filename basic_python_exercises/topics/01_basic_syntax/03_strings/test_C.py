from collections import Counter

from C import reverse_words, count_characters


def test_reverse_words():
    for s in ['test', 'the quick brown fox', 'a'*10000, ' '.join(['foo', 'bar']*100000), '']:
        assert reverse_words(s) == ' '.join(s.split(' '))

def test_count_characters():
    for s in ['thing', 'test test test', 'a'*100000, '', '*3..7ethsno(0e']:
        assert count_characters(s) == dict(Counter(s))
