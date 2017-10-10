# Control Flow

In the previous section we introduced the building blocks for constructing the flow of control in 
your computer programs.  We've seen looping statements using the `for` keyword and branching statements
using `if`, `elif`, and `else`.  Over the course of the next several months, one of the primary skills you 
will learn is how to take an arbitrarily complicated problem and translate it into this language of branches
and loops.  In order to be effective at this, you first need a bit of background in Boolean Algebra.  If those
sound like scary words, fear not.  It takes a bit of work to get, but it is no more complicated than the 
arithmetic you learned in elementary school.

Boolean algebra is a mathematical system.  Like all mathematical systems, it is defined by a set of 
elements that it talks about and some number of operations that tell us how those elements interact.

What does this mean?

Let's push on this analogy with arithmetic a bit and see where it goes.  In elementary school math,
you were taught about numbers and counting and then later about addition and multiplication and more complicated
things you could do with those numbers.  When we talk about arithmetic as a mathematical system, its elements
are the numbers, be they the integers or fractions or the real numbers.  The operations of arithmetic 
are addition, subtraction, multiplication, and division.  Additionally you were told about some properties 
you've internalized but maybe forgotten the names of: associativity, commutativity, and the distribution of 
multiplication over addition.  Maybe the most critical thing to understand about this system is that if we
start out with any two elements (i.e. numbers), every operation we've defined on those elements produces
another element in the system.  If this seems like a trivial statement to you, I urge you to think a bit 
about where fractions and real numbers and complex numbers came from.

In Boolean algebra, the elements of our system are just the values `True` and `False`.  We then have three 
operations: `and`, `or`, and `not`.  `and` and `or` are what's called binary operators.  They take in 
to input elements from the set {`True`, `False`} and output a single element from the same set.  `not` 
on the other hand is what's called a unary operator.  That is, it is an operator that takes a single
input from our set of elements and produces a single output from that set.  This is analogous to the way
putting a minus sign in front of a number turns it into its additive inverse.  I am belaboring the point a
bit here, but only because this system which should feel common-sensicle often becomes very difficult 
to think through when you have to apply it to real world examples.  Let's look at a few toy problems first:

### Class Questions

Let `a`, `b`, `c`, `d`, and `e` be elements of the set {`True`, `False`}.

1. `not (a or b) =` 
    1. `(not a) or (not b)`
    2. `((not a) or b) and (a or (not b))`
    3. `(not a) and (not b)`
    4. `(not a) or b`
    
    
2. `a and not (b or c) =`
    1. `(a and b) or (a and c)`
    2. `(a or b) and (a or c)`
    3. `not((not a) and b or c)`
    4. `(a and (not b)) or (a and (not c))`
    
3. `not(a or b and (not(c) and d)) or e =`
    1. `((not a) and (not b) or not(not(c) and d)) or e`
    2. `((not a) and (not b) or (c or (not d)) or e`
    3. `not(a or b and ((not c) and d) and (not e))` 
    4. `(not a) and (not b) or not((not c) and d and (not e))`

In this next section we are going to move away from the simple examples 
of the first section and introduce variations on a problem with a more complicated and realistic control
flow needs. Let's start with our class exercise.
