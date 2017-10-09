def print_descriptions_of_datasets():
    # print Dataset 1
    with open('data/dataset_1.txt') as f:
        rows = f.readlines()
    values = []
    for row in rows:
        values.append(float(row))

    sum_of_values = 0
    for value in values:
        sum_of_values += value

    mean_of_values = 0
    for value in values:
        mean_of_values += value/len(values)

    sorted_values = sorted(values)
    if len(sorted_values) % 2 == 0:
        midpoint = int(len(sorted_values) / 2)
        median_of_values = sorted_values[midpoint - 1] + sorted_values[midpoint]
        median_of_values /= 2
    else:
        midpoint = int(len(sorted_values) / 2)
        median_of_values = sorted_values[midpoint]

    sum_message = 'Sum of dataset_1 is: {}'.format(sum_of_values)
    print(sum_message)

    mean_message = 'Mean of dataset_1 is: {}'.format(mean_of_values)
    print(mean_message)

    median_message = 'Median of dataset_1 is: {}'.format(median_of_values)
    print(median_message)

    # Dataset # 2
    with open('data/dataset_2.txt') as f:
        values = [float(l) for l in f]

    sum_of_values = 0
    for value in values:
        sum_of_values += value

    mean_of_values = sum_of_values / len(values)

    sorted_values = sorted(values)
    if len(sorted_values) % 2 == 0:
        midpoint = int(len(sorted_values) / 2)
        median_of_values = sorted_values[midpoint - 1] + sorted_values[midpoint]
        median_of_values /= 2
    else:
        midpoint = int(len(sorted_values) / 2)
        median_of_values = sorted_values[midpoint]

    print('')
    print('Dataset 2:')
    print('Sum = {}'.format(sum_of_values))
    print('Mean = {}'.format(mean_of_values))
    print('Median = {}'.format(median_of_values))


    # Three
    with open('data/dataset_3.txt') as f:
        rows = f.readlines()
    values = []
    for row in rows:
        values.append(float(row))
    sum_of_values = sum(values)
    mean = sum_of_values / len(values)

    midpoint = int(len(values) / 2)
    if len(values) % 2 != 0:
        median = sorted(values)[midpoint]
    else:
        median = sorted(values)[midpoint - 1] + sorted_values[midpoint]
        median /= 2


    print('\n')
    print('Dataset 3 summary')
    print('sum {}, mean {}, median {}'.format(sum_of_values, mean, median))


if __name__ == '__main__':
    print_descriptions_of_datasets()
