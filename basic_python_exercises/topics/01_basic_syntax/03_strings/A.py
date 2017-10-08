def every_other_character(s):
    """
    Take the string `s` and return a new string made up of every other
    character from `s`.

    Example
    -------
    every_other_character('the quick brown fox') -> 'teqikbonfx'
    """

    result = ''
    for i in range(len(s)):
        if i % 2 != 0:
            result = result + s[i]
    return result



def every_other_character_capitalized(s):
    """
    Take the string `s` and return a new string which is identical except
    that every other character is capitalized.

    Example
    -------
    every_other_character_capitalized('the quick brown fox') -> 'tHe qUiCk bRoWn fOx'
    """

    result = ''
    for i in range(len(s)):
        if i % 2 != 0:
            result = result + s[i].upper()
        else:
            result = result + s[i]

    return result
