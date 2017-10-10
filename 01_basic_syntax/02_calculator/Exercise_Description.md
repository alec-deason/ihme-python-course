In each exercise you will implement a mathematical operation and add it to a
simple calculator we have included in the exercise file. The exercise
descriptions all refer to the function you will need to add to the calculator.

The calculator in each exercise can be run from the command line like so:

```
> python A.py add 1 2
3
> python A.py multiply 4 4
16
```

##Exercise A:

Calculate the roots of a [quadratic equation](https://en.wikipedia.org/wiki/Quadratic_equation) 
given it's coefficients.

**Input Format**

Three numbers, `a`, `b`, and `c`, the coefficients of the equation:

`a x**2 + b x + c = 0`

**Expected Output**

The positive and negative roots of the quadratic equation represented by the coefficients, in that order.

**Example**

Say we're given the equation

`3 x**2 + 5 x - 7 = 0`

Then we should have
```
> quadratic(3, 24, 7)
(-0.30315449786352744, -7.696845502136473)
```


##Exercise B:

Implement floor division, which is division that rounds down to the nearest
whole number.

**Input Format**

Two numbers, the numerator `a` and the divisor `b`.

**Expected Output**

`a/b` rounded down to the nearest whole number.

**Example**

```
> floor_division(7, 2)
3
```

##Exercise C:

Calculate the sum of [prime factors](https://en.wikipedia.org/wiki/Prime_factor) of a number.

**Input Format**

One number `number`

**Expected Output**

The sum of all prime factors of `number`

**Example**

```
> sum_of_prime_factors(8)
3
> sum_of_prime_factors(12)
6
> sum_of_prime_factors(12000000)
11
```
