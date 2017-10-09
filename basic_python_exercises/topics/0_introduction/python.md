# Introduction to Python
## Getting Started

## Course materials

### [github.com/ihmeuw/ihme-python-course](https://github.com/ihmeuw/ihme-python-course)

First, you're going to want to get a copy of this repository onto your
machine. Simply fire up ``git`` and clone it:

1.  Open up a shell (e.g. ``git.exe``, ``cmd.exe``, or ``terminal.app``)

2.  Navigate to where you'd like to save this. 
    - We recommend ``~/repos/`` (e.g. ``C:/Users/<user>/repos/`` on Windows, 
    ``/Users/<user>/repos/`` on Mac, or ``/home/<user>/repos/`` on Unix).

3.  Clone this repo:
        git clone https://github.com/ihmeuw/ihme-python-course.git
        
If you need help with setting up `git`, see 
[this page](https://help.github.com/articles/set-up-git/#setting-up-git) or 
simply download the repo as a [zip file](https://github.com/IHME/ihme-python-course/archive/master.zip) for now...

![I wrote 20 short programs in Python yesterday. It was wonderful. Perl, I'm leaving you.](http://imgs.xkcd.com/comics/python.png)

via [xkcd](https://xkcd.com/353/) (see also [xkcd in python](https://pypi.python.org/pypi/xkcd/) 
and [xkcd for matplotlib](http://matplotlib.org/xkcd/examples/showcase/xkcd.html))

# What is Python?

[Python](http://www.python.org/) is a widely used high-level, general-purpose, 
interpreted, dynamic programming language.

## Broadly:

Officially, Python is an interpreted scripting language (meaning that it is not 
compiled until it is run) for the C programming language; in fact, Python itself is 
coded in C (though there are other non-C implementations). It offers the power and 
flexibility of lower level (*i.e.* compiled) languages, without the steep learning 
curve and associated programming overhead. The language is very clean and readable, 
and it is available for almost every modern computing platform.

## Advantages:

* Ease of programming, minimizing the time required to develop, debug and maintain code
* Well-designed language that encourages good programming practices:
    * Modular and object-oriented programming, good system for packaging and re-use of code
    * Documentation tightly integrated with the code
* A large standard library with many extensions

## Disadvantages:

* Since Python is an interpreted and dynamically typed programming language, the execution 
of python code can be slow compared to compiled statically typed programming languages, such as C and Fortran
* Somewhat decentralized, with different environments, packages and documentation spread out at different places

# Scientific Computing in Python


## Why do we use Python at IHME?

- Powerful and easy to use
- Interactive
- Extensible
- Large third-party library ecosystem
- Free and open

## Powerful and easy to use

- Python is simultaneously powerful, flexible and easy to learn and use 
(in general, these qualities are traded off for a given programming language)
- Anything that can be coded in C, FORTRAN, or Java can be done in Python, 
almost always in fewer (and more readable) lines of code, and with fewer debugging headaches
- Its standard library is extremely rich, including modules for string 
manipulation, regular expressions, file compression, mathematics, profiling and debugging (*etc*)
- Python is object-oriented, which is an important programming paradigm 
particularly well-suited to scientific programming, which allows data 
structures to be abstracted in a natural way

## Interactive 

- Python may be run interactively on the command line, 
in much the same way as R
- Notebooks offer convenient prototyping, mixing code in 
with outputs such as graphs and direct viewing of data structures
- Rather than compiling and running a particular program, 
commands may entered serially which is often useful for mathematical programming and debugging

## Extensible

- Often referred to as a “glue” language, meaning that it is a useful in a mixed-language environment 
    - (such as at IHME, where we often have to combine R, Stata, C++, etc)
- Python was designed to interact with other programming languages, both through 
interfaces like [rpy2](http://rpy2.bitbucket.org/) and by compiling directly 
into Python extensions using e.g. [Cython](http://cython.org/)
- New interfaces coming out all the time, such as for GPU computing

## Large third-party library ecosystem

There are modules available for just about anything you could want to do in Python,
 with nearly 100,000 available on [PyPI](https://pypi.python.org/pypi) alone. Some notable packages:

- [**NumPy**](http://www.numpy.org/): Numerical Python (NumPy) is a set of extensions that provides 
the ability to specify and manipulate array data structures. It provides array manipulation and 
computational capabilities similar to those found in Matlab or Octave. 
- [**SciPy**](http://www.scipy.org/): An open source library of scientific tools for Python, 
SciPy supplements the NumPy module. SciPy gathering a variety of high level science and 
engineering modules together as a single package. SciPy includes modules for graphics and 
plotting, optimization, integration, special functions, signal and image processing, 
genetic algorithms, ODE solvers, and others.
- [**Matplotlib**](http://matplotlib.org/): Matplotlib is a python 2D plotting library 
which produces publication-quality figures in a variety of hardcopy formats and interactive 
environments across platforms. Its syntax is very similar to Matlab. 
- [**Pandas**](http://pandas.pydata.org/): A module that provides high-performance, 
easy-to-use data structures and data analysis tools. In particular, the `DataFrame` class is 
useful for spreadsheet-like representation and mannipulation of data. Also includes 
high-level plotting functionality.
- [**IPython**](https://ipython.org/): An enhanced Python shell, designed to increase 
the efficiency and usability of coding, testing and debugging Python. It includes both 
a Qt-based console and an interactive HTML notebook interface, both of which 
feature multiline editing, interactive plotting and syntax highlighting.

## Free and open

- Python is released on all platforms under an open license 
(Python Software Foundation License), meaning that the language and its source is freely distributable
- Keeps costs down for scientists and universities operating under a limited budget
- Frees programmers from licensing concerns for any software they may develop
