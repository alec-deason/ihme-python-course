def inplace_bubble_sort(l):
    """
    Implement an in place bubble sort. The bubble sort algorithm is a simple
    comparison sort. The algorithm works like this: step through the list to be
    sorted comparing every adjacent pair of values. If they are already in order
    you leave them and move forward, otherwise you swap their positions. You
    walk through the list repeatedly until you can walk the entire list without
    swapping any pairs which indicates the list is fully sorted. The sort is
    'in place' because you do it by moving elements within the original list
    rather than creating a new list to hold the sorted elements.

    This function should not return anything. It works by modifying the input
    list.

    This is an example of a list being sorted with bubble sort:
        [4, 3, 1, 2]
         |--|        # Consider the first pair
        [3, 4, 1, 2]
         |--|        # They are not in order, so swap
        [3, 4, 1, 2]
            |--|     # move to the next pair
        [3. 1, 4, 2]
            |--|     # swap
        [3, 1, 4, 2]
               |--|  # move
        [3, 1, 2, 4]
               |--|  # swap
        [3, 1, 2, 4]
         |--|        # move back to the begining
        [1, 3, 2, 4]
         |--|        # swap
        [1, 3, 2, 4]
            |--|     # move
        [1, 2, 3, 4]
            |--|     # swap
        [1, 2, 3, 4]
               |--|  # move
        [1, 2, 3, 4]
               |--|  # no swap is needed
        [1, 2, 3, 4]
         |--|        # move to the beginning


    Examples
    --------
    l = [3,2,2,1]
    inplace_bubble_sort(l)
    l == [1,2,2,3]

    l = [10,20,30]
    inplace_bubble_sort(l)
    l == [10,20,30]
    """

    pass
