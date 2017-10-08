def perfect_squares(limit):
    """
    Return the count and sum of all perfect squares less than `limit`.
    """
    i = 0
    count = 0
    sum_of_squares = 0
    while i*i < limit:
        count += 1
        sum_of_squares += i*i
        i += 1
    return count, sum_of_squares
