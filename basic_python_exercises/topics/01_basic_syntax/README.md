# Introduction to Python syntax

## The REPL

Like the command terminal (cmd.exe) or a bash shell, the python command prompt is
a Read-Eval-Print Loop (REPL).  Try typing the following into your python console:

```
>>> 'hello world'
```

```
>>> print('hello world')
```

Q: Why is the output from these two different?

```
>>> 5 + 3
```

```
>>> 5.0 + 3
```

Q: Why is the output from these two different?

## Variables
 - A variable is just a name for a value,
    such as `x`, `my_variable`, or `variable_1`
- Python's variables must begin with a letter and are **case sensitive**
- We can create a new variable by assigning a value to it using `=`-


### Naming

- Variable names in Python can contain alphanumerical characters `a-z`, `A-Z`, `0-9` and some special characters such 
    as `_`. Normal variable names must start with a letter. 
- By convention, variable names start with a lower-case letter, and Class names start with a capital letter. 
- In addition, there are a number of Python keywords that cannot be used as variable names. These keywords are:

        and, as, assert, break, class,
        continue, def, del, elif, else, 
        except, exec, finally, for, from,
        global, if, import, in, is, lambda, 
        not, or, pass, print, raise, 
        return, try, while, with, yield

- _Note_: Be aware of the keyword `lambda`, which could easily be a natural variable name in a scientific program. But 
    being a keyword, it cannot be used as a variable name.
    
## Data Types

Python is a **dynamically typed** language.  

Q: Any ideas what this means?

Python does have a few basic data types you'll want to be 
familiar with:

- Numbers
- Booleans
- Strings
- Container types (lists, dicts, tuples, etc.)
