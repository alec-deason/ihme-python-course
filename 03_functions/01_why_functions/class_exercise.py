def sum_of_datasets():
    """
    Print the sum of all rows in dataset_1, dataset_2 and dataset_3.
    """

    sum_of_all_data = 0

    with open('data/dataset_1.txt') as f:
        rows = f.readlines()
    for r in rows:
        sum_of_all_data += float(r)

    with open('data/dataset_2.txt') as f:
        rows = f.readlines()
    for r in rows:
        sum_of_all_data += float(r)

    with open('data/dataset_3.txt') as f:
        rows = f.readlines()
    for r in rows:
        sum_of_all_data += float(r)

    print(sum_of_all_data)


if __name__ == '__main__':
    sum_of_datasets()
