## Conditional Statements

Conditional statements are how we allow our code to make decisions.  The structure 
of these statements in Python is very simple:
```
if {BOOLEAN EXPRESSION}:
    {STATEMENTS}
``` 
Where `{BOOLEAN EXPRESSION}` is something that evaluates to `True` or `False` and `{STATEMENTS}` 
is the code you want to execute when `{BOOLEAN EXPRESSION}` evaluates to `True`.

Important things to note about `if` statements:
    
1. The colon (:) is significant and required. It separates the header of the compound statement from the body.
2. The line after the colon must be indented. It is standard in Python to use four spaces for indenting.
3. All lines indented the same amount after the colon will be executed whenever the BOOLEAN_EXPRESSION is true.

Let's look at an example:

```
food = 'spam'

if food == 'spam':
    print('Ummmm, my favorite!')
    print('I feel like saying it 100 times...')
    print(100 * (food + '! '))
```

**Q: Can anyone tell me what this code does?**

The boolean expression after the if statement is called the condition. 
If it is true, then all the indented statements get executed.

## Comparison Operators
Boolean expression often take the form of relationships between two values.  These
relationships are written using Python's comparison operators:

Assume we have two variables: `a` which holds the value 10 and `b` which holds the value 21.

| **Operator**              | **Description**                                                                                                  | **Example**                    |
|---------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------|
| Equality:`==`             | If the values of two operands are equal, then the condition becomes true.                                        | `(a == b) is not True.`        |
| Inequality:`!=`           | If values of two operands are not equal, then condition becomes true.                                            | `(a != b) is True.`            |
| Strictly Greater Than:`>` | If the value of left operand is greater than the value of right operand, then condition becomes true.            | `(a > b) is not True.`         |
| Strictly Less Than:`<`    | If the value of left operand is less than the value of right operand, then condition becomes true.               | `(a < b) is True.`             |
| Greater Than:`>=`         | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.| `(a >= b) is not True.`        |
| Less Than:`<=`            | If the value of left operand is less than or equal to the value of right operand, then condition becomes true.   | `(a <= b) is True.`            |

We will talk more about complex conditional statements in the Section 2 of the course. 
 
## The `else` statement 
It is frequently the case that you want one thing to happen when a condition it true, and something else 
to happen when it is false. For that we have the if else statement.

```
if food == 'spam':
    print('Ummmm, my favorite!')
else:
    print("No, I won't have it. I want spam!")
```

## The `elif` statement
Sometimes there are more than two possibilities and we need more than two branches. 
One way to express a computation like that is using the `elif` statement.
```
if choice == 'a':
    print("You chose 'a'.")
elif choice == 'b':
    print("You chose 'b'.")
elif choice == 'c':
    print("You chose 'c'.")
else:
    print("Invalid choice.")
```

## Nested Conditionals
One conditional can also be nested within another. 
```
if x < y:
    STATEMENTS_A
else:
    if x > y:
        STATEMENTS_B
    else:
        STATEMENTS_C
```


