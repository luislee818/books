def find_two_smallest(L):
    """ (see above) """

    # Find the index of the minimum and remove that item.
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

    # Find the index of the new minimum.
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    # put smallest back into L
    # Fix min2 in case it was affected by the re-insertion:
    # if min1 comes before min2, add 1 to min2
    # return the two indices
