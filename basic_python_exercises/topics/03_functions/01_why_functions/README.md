# What is a function
A function is some section of a program that has been sectioned off and given a name. In Python
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
# TODO: Describe functions with no args, functions with args, kwargs, and functions with and without returns
