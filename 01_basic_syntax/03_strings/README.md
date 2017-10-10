# String Manipulation

## Making strings

Strings are the data structure Python uses for storing text. They represented
in code as text surrounded by single quotes or double quotes. You can use
either but they must be matched:

```
> 'this is a string' # Good
> "this is also a string" # Good
> 'this is not a string" # Not Good
SyntaxError: EOL while scanning string literal
```

Having two kinds of quotes is useful if you need to write a string which has
quotes inside of it:

```
> 'I said to the interpreter, 'make me a string'' # Not Good
SyntaxError: invalid syntax
> 'It said to me, "Sure, whatever."' # Good
```

Normally strings can't have line breaks in them but you can have multiline
strings by using tripled quotes like this:

```
> '''This is a string.
It has a line break in it.'''
> """This
one
has
several!
"""
```

Strings can contain characters in any language, including mathematical symbols
and characters, like `=`, which are normally reserved. In fact Python makes no
attempt to interpret the contents of strings. The exception to that rule is:

## String Formatting

Python has a built in string interpolation or templating system, refered to as
string formatting, that lets you create new strings out of variables in your
code. The system works by replacing special character sequences in the string
with the content of variables in your code.

```
> name = 'Python'
> message = 'My name is {}.'
> message.format(name)
'My name is Python.'
```

This is the standard formatting style in which '{}' is replaced by the contents
of `name`. You can have multiple replacements:

```
> name = 'Python'
> title = 'Programming Language'
> "My name is {} and I'm a {}".format(name, title)
'My name is Python and I'm a Programming Language'
```

You'll occasionally see a different version of formatting in older code:

```
> age = 'old'
> 'This is the %s way of doing things.' % age
'This is the old way of doing things.'
```

You may also see the newer way which is the standard starting with the latest
version of Python:

```
> age = 'bleeding edge'
> f'This is the {age} way of doing things.' # Only valid in Python 3.6+
'This is the bleeding edge way of doing things.'
```

# Other String Tools

There is a rich tool box of string manipulation in tools in Python. Here are
a couple of good places to look in the docs:
* [basic string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
* [regular expressions (complex search and replace)](https://docs.python.org/3/library/re.html)

Here's a few especially useful tools:

|**Method**           | **Description**                                                                                                  | **Example**                                                            |
|---------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| split               | Breaks a string up into substrings separated by a character like space.                                          | `'two words'.split(' ') = ['two', 'words']`                            |
| join                | Combines a list of strings into a single string with the substrings separated by the string `join` is called on. | `'_'.join(['a','1','b','2']) = 'a_1_b_2'`                              |
| endswith/startswith | Tests if the string ends or starts with a substring.                                                             | `'a string'.startswith('a') = True`                                    |
| in                  | The `in` operator tests if a substring is present in a string.                                                   | `'fish' in 'fishbowl' = True`                                          |
| replace             | Search and replace.                                                                                              | `'Cats are the best'.replace('Cats', 'Snails') = 'Snails are the best' |
