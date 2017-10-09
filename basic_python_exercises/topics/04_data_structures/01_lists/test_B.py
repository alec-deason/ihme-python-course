import string
import random

from B import cesar_cypher_reader, cesar_cypher_writer

ALPHABET = string.ascii_lowercase + ' '

def _cypher(message, key):
    key_map = dict(zip(ALPHABET, key))
    return ''.join([key_map[c] for c in message])

def test_cesar_cypher_reader():
    key = list(ALPHABET)
    for _ in range(100):
        random.shuffle(key)
        for message in ['the quick brown fox', 'test', '', 'abc'*1000]:
            assert cesar_cypher_reader(_cypher(message, key), key) == message

def test_cesar_cypher_writer():
    key = list(ALPHABET)
    for _ in range(100):
        random.shuffle(key)
        for message in ['the quick brown fox', 'test', '', 'abc'*1000]:
            assert cesar_cypher_writer(message, key) == _cypher(message, key)
