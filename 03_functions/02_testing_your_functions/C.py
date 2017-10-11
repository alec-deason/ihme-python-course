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

    murder_count = text.count('murder')
    cat_count = text.count('cat')

    return cat_count / murder_count


def line_count(text):
    """
    Counts the number of line returns in a piece of text.

    Note
    ----
    Python (and most other programming languages) uses the special character
    sequence '\n' to represent new lines.

    Example
    -------
    line_count('this\nhas\nthree\nlines') -> 3
    """

    line_count = text.count('\n')
    # There will always be one more line than there are line breaks because
    # of the first line, so account for that.
    line_count += 1

    return line_count

if __name__ == '__main__':
    text = _load_text()
    print('Cat to Murder ratio: {}'.format(cat_to_murder_ratio(text)))
    print('Line count: {}'.format(line_count(text)))
