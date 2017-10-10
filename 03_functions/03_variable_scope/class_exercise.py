
x = 35
banana = ['a', 'b', 'c']

def function_a(x, y, z):

    range = "I'm a string"
    range += " but maybe a poorly named one."
    banana.append(x)
    banana.append(range)

    def inner_function(x, banana):
        for i in range(3, 10):
            print('x: {} y: {} z: {}'.format(x, y, z))
            print('banana: {}, range: {}'.format(banana, range))

    inner_function(banana, x)


if __name__ == '__main__':
    print('x: {}'.format(x))
    print('banana: {}'.format(banana))

    function_a(5, 'hello', ['snakes', 'in', 'a', 'list'])
