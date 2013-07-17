def find_two_smallest(L):
    """ (see above) """

    # Get a sorted copy of the list so that the two smallest items are at the
    # front.
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]

    # find their indices in the original list L
    # return the two indices
