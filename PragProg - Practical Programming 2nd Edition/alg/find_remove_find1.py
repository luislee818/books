def find_two_smallest(L):
    """ (list of float) -> tuple of (int, int)

    Return a tuple of the indices of the two smallest values in list L.

    >>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
    (6, 7)
    """

    # find the index of the minimum item in L
    # remove that item from the list
    # find the index of the new minimum item in the list
    # put the smallest item back in the list
    # if necessary, adjust the second index
    # return the two indices
