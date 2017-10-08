def reverse_words(s):
    """
    Take the string `s` and return a string made up of the same words (anything
    separated by a space) in the reverse order.

    Examples
    --------
    reverse_words('the quick brown fox') -> 'fox brown quick the'
    reverse_words('dog') -> 'dog'
    """

    words = []
    current_word = ''
    for c in s:
        if c == ' ':
            if len(current_word)>0:
                words.append(current_word)
                current_word = ''
        else:
            current_word = current_word + c
    if len(current_word) > 0:
        words.append(current_word)
    return ' '.join(words)


def count_characters(s):
    """
    Take the string `s` and return a dictionary where the keys are characters
    which appear in `s` and the values are the number of times those characters
    appear.

    Examples
    --------
    count_characters('fox') -> {'f': 1, 'o': ', 'x': 0}
    count_characters('supercalifragalicious') -> {'a': 3, 'i': 3, 's': 2, 'u': 2, 'r': 2, 'c': 2, 'l': 2, 'p': 1, 'e': 1, 'f': 1, 'g': 1, 'o': 1}
    """

    characters = {}
    for c in s:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters
