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

**Q: Why is the output from these two different?**

```
>>> 5 + 3
```

```
>>> 5.0 + 3
```

**Q: Why is the output from these two different?**

## Variables
- A variable is just a name for a value,
    such as `x`, `my_variable`, or `variable_1`
- Python's variables must begin with a letter and are **case sensitive**
- We can create a new variable by assigning a value to it using `=`
```
x = 3
y = 'snakes!'
```


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
- _Note for R users_: Coming from R you could use `.` in variable names.  This is not the case in Python.
  The `.` character in python works as an operator to provide access to attributes of an object.  You
  will see a little of that in this part of the class and more of it in the `numpy` and `pandas` sections.
    
## Data Types

Python is a **dynamically typed** language.  

Q: Any ideas what this means?

Python does have a few basic data types you'll want to be 
familiar with:

- Numbers
- Booleans
- Strings
- Container types (lists, dicts, tuples, etc.)

## Comments

Comments in python come in two forms:

1. In-line comments.  These comments begin with a `#` and are usually written on a single line.
2. Docstrings and other multi-line comments.  These comments are surrounded by **triple-double quotes**.  
   They are most often used to document functions and classes and modules (and when they do, they are
   referred to as docstrings), however they can also be used for any other long bit of narrative documentation
   in your code.
   
   
## Whitespace
Python is a whitespace delimited language.  Practically, this means that the Python interpreter cares 
about indentation in a way that languages like R or Java do not.  Whereas R uses the curly braces `{}`
to denote the scope of something like a function or a for loop, this is done in python by indenting
in 4 spaces.  So a for loop in R might look like:
```
for (year in c(2010, 2011, 2012, 2013, 2014, 2015)){
  print(paste("The year is", year))
}
```
In Python we'd instead do
```
for year in [2010, 2011, 2012, 2013, 2014, 2015]:
    print("The year is".format(year))
```
There are things going on here that we'll talk about later (loops, lists, and string formatting),
the important thing to note is the lack of curly braces and the exact indentation level (4 spaces)
that lets Python know that the print statement is inside the for loop.
