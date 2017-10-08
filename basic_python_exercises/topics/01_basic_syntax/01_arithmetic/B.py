import math

def quadratic(a, b, c):
    """
    Calculate and return the roots of the quadratic function specified by
    the supplied coefficients:

        ax^2 + bx + c = 0

    In the cases where the roots are not define return the string 'roots undefined'
    """
    if a == 0 or b*b - 4*a*c < 0:
        return 'roots undefined'

    positive_root = (-b+math.sqrt(b*b - 4*a*c))/(2*a)
    negative_root = (-b+math.sqrt(b*b - 4*a*c))/(2*a)

    return positive_root, negative_root
