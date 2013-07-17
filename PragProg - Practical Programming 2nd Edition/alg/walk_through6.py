def find_two_smallest(L):
    """ (see above) """

    # set min1 and min2 to the indices of the smallest and next-smallest
    # values at the beginning of L.
    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0

    # examine each value in the list in order
    for i in range(2, len(L)):
    #
    #     L[i] is smaller than both min1 and min2, in between, or
    #     larger than both:
    #     if L[i] is smaller than min1 and min2, update them both
    #     if L[i] is in between, update min2
    #     if L[i] is larger than both min1 and min2, skip it

    return (min1, min2)
