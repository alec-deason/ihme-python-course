# String Manipulation

Strings are the way that Python and many other languages handle textual data. String 
literals can be enclosed by either double or single quotes, although single quotes 
are more commonly used. Backslash escapes work the usual way within both 
single and double quoted literals -- e.g. `\n` `\'` `\"`. A double quoted string 
literal can contain single quotes without any fuss (e.g. `"I didn't do it"`) and
likewise single quoted string can contain double quotes. 

Python strings are "immutable" which means they cannot be changed after they are created.
Since strings can't be changed, we construct *new* strings as we go 
to represent computed values. So for example the expression (`'hello' + 'there'`) 
takes in the 2 strings `'hello'` and `'there'` and builds a new string `'hellothere'`.


Characters in a string can be accessed using the  `[ ]` syntax.
Python uses zero-based indexing, so if `str` is `'hello'`,  `str[1]` is `'e'`. 
If the index is out of bounds for the string, Python raises an error. 
The Python style is to halt if it can't tell what to do, rather than just make 
up a default value. The handy "slice" syntax (below) also works to extract any 
substring from a string. The `len(string)` function returns the length of a string. 
The `[ ]` syntax and the `len()` function actually work on any sequence type 
-- strings, lists, etc.. Python tries to make its operations work consistently 
across different types. 

Python newbie gotcha: don't use `"len"` as a variable name to avoid blocking out the 
`len()` function. The `+` operator can concatenate two strings. Notice in the code 
below that variables are not pre-declared -- just assign to them and go.

```
s = 'hi'
print(s[1])         # i
print(len(s))       # 2
print(s + ' there') # hi there
```

The `+` does not automatically convert numbers or other types to string form. 
The `str()` function converts values to a string form so they can be combined with other strings.

```
pi = 3.14
#text = 'The value of pi is ' + pi       # NO, does not work
text = 'The value of pi is '  + str(pi)  # yes
```


## String Methods

Here we let `s` be some variable holding a Python string.

| Method                   | Description                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|`s.lower()`/`s.upper()`   | Returns the lowercase or uppercase version of the string.                                                                                |
|`s.strip()`               | Returns a string with whitespace removed from the start and end.                                                                         |
|`s.find('other')`         | Searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found. |
|`s.replace('old', 'new')` | Returns a string where all occurrences of 'old' have been replaced by 'new'.                                                             |
|`s.split('delim')`        | Returns a list of substrings separated by the given delimiter.                                                                           |
|`s.join(iterable)`        | Joins the elements in the given list together using the string as the delimiter.                                                         |

More string methods can be found on the [Python website](https://docs.python.org/3/library/stdtypes.html#string-methods)

## Slicing
The "slice" syntax is a handy way to refer to sub-parts of sequences -- typically strings and lists. 
The slice `s[start:end]` is the elements beginning at start and extending up to but not including 
end. Suppose we have `s = "Hello"`

![Hello](https://developers.google.com/edu/python/images/hello.png)

- `s[1:4]` is `'ell'` -- chars starting at index 1 and extending up to but not including index 4
- `s[1:]` is `'ello'` -- omitting either index defaults to the start or end of the string
- `s[:]` is `'Hello'` -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
- `s[1:100]` is `'ello'` -- an index that is too big is truncated down to the string length

The standard zero-based index numbers give easy access to chars near the 
start of the string. As an alternative, Python uses negative numbers to give easy 
access to the chars at the end of the string: `s[-1]` is the last char `'o'`, `s[-2]` is `'l'` 
the next-to-last char, and so on. Negative index numbers count back from the end of the string:

- `s[-1]` is `'o'` -- last char (1st from the end)
- `s[-4]` is `'e'` -- 4th from the end
- `s[:-3]` is `'He'` -- going up to but not including the last 3 chars.
- `s[-3:]` is `'llo'` -- starting with the 3rd char from the end and extending to the end of the string.

It is a neat truism of slices that for any index `n`, `s[:n] + s[n:] == s`. 
This works even for `n` negative or out of bounds. Or put another way `s[:n]` and `s[n:]` 
always partition the string into two string parts, conserving all the characters. 
As we'll see in the list section later, slices work with lists too.


## String formatting

Python’s `str.format()` method of the string class allows you to do
variable substitutions and value formatting. This lets you concatenate
elements together within a string through positional formatting.
 
`str.format()` works by putting in one or more replacement fields or 
placeholders — defined by a pair of curly braces {} — into a string and 
calling the `str.format()` method. You’ll pass into the method the 
value you want to concatenate with the string. This value will be 
passed through in the same place that your placeholder is positioned when you run the program.

```
>> print("Sammy has {} balloons.".format(5))
Sammy has 5 balloons.
```

This is a very powerful method with it's own mini-language that you can
reference on the [Python website](https://docs.python.org/3.4/library/string.html#formatstrings)

