import argparse


def quadratic(a, b, c):
    """
    Calculate and return the roots of the quadratic function specified by
    the supplied coefficients:

        ax^2 + bx + c = 0

    Add your implementation to the `calculator` function below so it can be
    used like the other arithmetic operators implemented here.
    """

    positive_root = 0
    negative_root = 0
    return postive_root, negative_root


############################################################################
# These are examples of other calculator operations. Take a look at them but
# you don't need to modify them.
############################################################################

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return 'cannot divide by zero'
    return a / b


###########################################################################
# End calculator operations
###########################################################################

def calculator(operation, parameters):
    """
    This function implements a basic calculator by taking the name of an
    operation and one or more parameters and then calling the function which
    implements the operation with the parameters.

    Parameters
    ----------
    operation : str
        The name of the operation to use.
    parameters : [number]
        A list of parameters to supply to the operation.
    """

    if operation == 'add':
        return add(parameters[0], parameters[1])
    elif operation == 'subtract':
        return subtract(parameters[0], parameters[1])
    elif operation == 'multiply':
        return multiply(parameters[0], parameters[1])
    elif operation == 'divide':
        return divide(parameters[0], parameters[1])
    else:
        raise ValueError('Unknown operation "{}"'.format(operation))

if __name__ == '__main__':
    """
    This block is what is run when you execute this file as a script. It
    defines what command line arguments the script should take, those arguments
    in and uses them to call the `calculator` function above.

    You can run this script from the command line like this:

    >> python A.py add 1 2
    3

    Note
    ----
    It is possible to write a script without the `if __name__ == '__main__':`
    guard around it's entry point code like this but it's bad style. Having
    the guard allows the module to be imported by other code without causing
    unexpected side effects. Also it makes it very clear to other programmers
    how the script is intended to be run.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('operation')
    parser.add_argument('parameters', nargs='+', type=float)
    args = parser.parse_args()

    result = calculator(args.operation, args.parameters)

    print(result)
