import re

def _load_text():
    with open('data/The_mysterious_affair_at_styles.txt') as f:
        text = f.read()
    return text


def cat_to_murder_ratio(text):
    """
    Calculates the ratio of the number of times 'murder' vs 'cat' is mentioned
    in a text.

    Note
    ----
    Case is ignored as are word breaks. So 'catty' is considered a reference to
    'cat'.

    Example
    -------
    cat_to_murder_ratio('This cat is the most murderous murderer') -> 0.5
    cat_to_murder_ratio('Murder is the only thing on the cat's mind.') -> 1.0
    """

    murder_count = len(re.findall('murder', text))
    cat_count = len(re.findall('cat', text))

    return cat_count / murder_count


def line_count(text):
    """
    Counts the number of line returns in a piece of text.

    Example
    -------
    line_count('this\nhas\nthree\nlines') -> 3
    """

    line_count = len(re.findall('\n', text))
    return line_count

if __name__ == '__main__':
    text = _load_text()
    print('Cat to Murder ratio: {}'.format(cat_to_murder_ratio(text)))
    print('Line count: {}'.format(line_count(text)))
