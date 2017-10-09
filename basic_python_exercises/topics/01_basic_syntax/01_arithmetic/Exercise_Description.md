##Exercise A:

Calculate the cosine of a number.

**Input Format**

A single number, in radians

**Expected Output**

The cosine of the given number.

**Example**

```
> cos(1.570796)  # About pi/2
3.2679489653813835e-07
```
Note that this number is very close to zero, which is what we expect.


##Exercise B:

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

Exercise C:

Calculate the count and sum of all [square numbers](https://en.wikipedia.org/wiki/Square_number) 
bigger than zero and less than a specified limit.

**Input Format** 

A single number `limit`, which is the maximum value of the potential perfect squares.

**Expected Output**

The count of perfect squares under the given limit followed by there sum.

**Example**

Say we're given the number 40, then we have

- 1*1 = 1
- 2*2 = 4
- 3*3 = 9
- 4*4 = 16
- 5*5 = 25
- 6*6 = 36
- 7*7 = 49  _# Too big_

So we then return `(6, 91)` since we have six perfect squares with values less than 40 
and 1 + 4 + 9 + 16 + 25 + 36 = 91.  E.g.

```
> perfect_squares(40)
(6, 91)
``` 
