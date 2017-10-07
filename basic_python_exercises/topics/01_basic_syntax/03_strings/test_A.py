from A import every_other_character, every_other_character_capitalized

def test_every_other_character():
    for s in ['test', 'two words', 'a'*1000, '']:
        assert every_other_character(s) == [c for i, c in enumerate(s) if i%2 != 0]


def test_every_other_character_capitalized():
    for s in ['test', 'two words', 'a'*1000, '']:
        assert every_other_character(s) == [c if i%2 == 0 else c.upper() for i, c in enumerate(s)]
