def find_two_smallest(L):
    """ (see above) """

    # Find the index of the minimum and remove that item.
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

    # Find the index of the new minimum.
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    # put the smallest item back in the list
    # if necessary, adjust the second index
    # return the two indices
