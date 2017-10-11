
def _read_column(name):
    """
    Read data for a single column on disk.
    """
    with open('data/{}.data'.format(name)) as f:
            return [float(l.strip()) for l in f]


def column_sum(column_data):
    total = 0
    for r in column_data:
        total += int(r)
    return total


def column_mean(column_data):
    return sum(column_data)/len(column_data)


if __name__ == '__main__':
    a = _read_column('a')
    b = _read_column('b')

    print('A mean: {}'.format(column_mean(a)))
    print('B sum: {}'.format(column_sum(b)))
