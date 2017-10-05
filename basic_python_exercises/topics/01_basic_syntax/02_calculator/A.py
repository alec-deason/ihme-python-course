import argparse


def quadratic(a, b, c):
    pass


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


def calculator(operation, a, b=None):
    if operation == '+':
        return add(a, b)
    elif operation == '-':
        return subtract(a, b)
    elif operation == '*':
        return multiply(a, b)
    elif operation == '/':
        return divide(a, b)
    else:
        raise ValueError('Unknown operation "{}"'.format(operation))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('operation')
    parser.add_argument('parameters', nargs='+', type=float)
    args = parser.parse_args()

    print(calculator(args.operation, *args.parameters))
