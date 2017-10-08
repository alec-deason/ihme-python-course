def reverse_string(s):
    """
    Take the string `s` and return a copy of it reversed.

    Example
    -------
    reverse_string('the quick brown fox') -> 'xof nworb kciuq eht'
    """

    result = ''
    for i in range(len(s)):
        result = result + s[len(s) - i - 1]
    return result


def count_occurrences(needle, haystack):
    """
    Return the number of times the string `needle` occures in the string
    `haystack`.

    Examples
    --------
    count_occurrences('fox', 'the quick brown fox') -> 1
    count_occurrences('fox', 'there are no predators in this hen house') -> 0
    """

    count = 0
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            count += 1
    return count
