# What is a function
A function is some block of organized code in a program that has been sectioned off and given a name. In Python
functions can take many arguments or no arguments and can likewise return many values or no values at all.
Python itself defines many functions like `range` or `len` that you've seen in the previous sections.
Additionally, we've been writing our code in functions since the start which illustrates how easy it 
is to define and use functions in Python.

# Why write functions?
Functions serve three primary purposes:
1. **Code re-use**.  When you separate a bit of logic into a function and give it a name, you and other people
    can now make a call to that function instead of repeating the code it contains over and over.  This also
    creates a single place you have to fix if you make a mistake or some other part of your code changes in
    a way that forces you to revise that bit of logic.
2. **Readability/Separation of Concerns**. The ability to give separate your program in to chunks and give
    those chunks descriptive names makes it much much easier for someone else looking at your code (or you at some
    later date) to understand what's going on.  It also helps you think about and reason about each function 
    individually and how they fit together.
3. **Testability**. One of the best reasons to break your code into functions is that it suddenly becomes 
    much, much easier to test.  You no longer have to consider all the different things that can go wrong in
    a big and complicated script, you need only verify that each of the functions work on their own and that
    they fit together reasonably. 

# How to write functions in python
The syntax rules for defining functions in Python are as follows:

1. Function blocks begin with the keyword def followed by the function name and parentheses.

```
def my_function():
```

2. The code block within every function starts with a colon (:) and is indented.

```
def my_function():
    # Code goes here, indented exactly four spaces. 
```

2. Any input parameters should be placed within these parentheses.
You can also set default arguments for the parameters.

```
def my_function_with_parameters(positional_parameter, keyword_parameter=default_argument):
    # Code goes here, indented exactly four spaces.
```  

3. The first statement of a function can be an optional statement - 
the documentation string of the function or docstring.

```
def my_function_with_a_oneline_docstring(a, b=5):
    """Does stuff to a and b."""
    # Code goes here, indented exactly four spaces.
```

```
def my_function_with_a_multi_line_docstring(a, b=5):
    """Does stuff to a and b.
    
    Parameters
    ----------
    a : str
        The a-est thing around.
    b : int
        Usually, but not always 5.
    
    Returns
    -------
    str
        The output of the stuff done to a and b.
    """
    # Code goes here, indented exactly four spaces.
```

5. The statement return {expression} exits a function, optionally passing 
back an expression to the caller. A return statement with no arguments is the same as return None.
```
def my_function_with_a_multi_line_docstring(a, b=5):
    """Does stuff to a and b.
    
    Parameters
    ----------
    a : str
        The a-est thing around.
    b : int
        Usually, but not always 5.
    
    Returns
    -------
    str
        Turns out I just strigify b and tack it on the end of a. 
    """
    return a + str(b)
```
