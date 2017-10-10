### String Methods

| Method                   | Description                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|`s.lower()`/`s.upper()`   | Returns the lowercase or uppercase version of the string.                                                                                |
|`s.strip()`               | Returns a string with whitespace removed from the start and end.                                                                         |
|`s.find('other')`         | Searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found. |
|`s.replace('old', 'new')` | Returns a string where all occurrences of 'old' have been replaced by 'new'.                                                             |
|`s.split('delim')`        | Returns a list of substrings separated by the given delimiter.                                                                           |
|`s.join(iterable)`        | Joins the elements in the given list together using the string as the delimiter.                                                         |


## Slicing

![Hello](https://developers.google.com/edu/python/images/hello.png)

- `s[1:4]` is `'ell'` -- chars starting at index 1 and extending up to but not including index 4
- `s[1:]` is `'ello'` -- omitting either index defaults to the start or end of the string
- `s[:]` is `'Hello'` -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
- `s[1:100]` is `'ello'` -- an index that is too big is truncated down to the string length
- `s[-1]` is `'o'` -- last char (1st from the end)
- `s[-4]` is `'e'` -- 4th from the end
- `s[:-3]` is `'He'` -- going up to but not including the last 3 chars.
- `s[-3:]` is `'llo'` -- starting with the 3rd char from the end and extending to the end of the string.
- `s[:n] + s[n:] == s`

## `str.format()`

```
>> print("Sammy has {} balloons.".format(5))
Sammy has 5 balloons.
```
