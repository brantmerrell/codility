"""https://codility.com/media/train/6-Leader.pdf"""
def slow_leader(arr_a):
    """O(n^2)"""
    # define length of array
    len_n = len(arr_a)
    # define length of array
    # begin leader definition as 'none' (-1)
    leader = -1
    # iterate through array
    for ndx_k in range(len_n):
        # set each element as a candidate for leader
        candidate = arr_a[ndx_k]
        # begin each count as 0
        count = 0
        # iterate through array again to count candidate's recurrence
        for ndx_i in range(len_n):
            # test each element for equivalence with candidate
            if arr_a[ndx_i] == candidate:
                # if equivalent, add to count of candidate's recurrence
                count += 1
            # if candidate's recurence is more than half of array length,
            if count > len_n // 2:
                # it is the leader
                leader = candidate
    # return leader
    return leader
slow_leader([6, 8, 4, 6, 8, 6, 6])
def fast_leader(arr_a):
    """O(n log(n))"""
    # define length of array
    len_n = len(arr_a)
    # begin leader definition as 'none' (-1)
    leader = -1
    # sort array
    arr_a.sort()
    # because a leader by definition is more than half array size,
    # it will be in the center of a sorted array (if it exists)
    candidate = arr_a[len_n // 2]
    # begin count at zero
    count = 0
    #  iterate through array
    for ndx_i in range(len_n):
        # for each element that matches candidate,
        if arr_a[ndx_i]:
            # add to count
            count += 1
    # if count comprises more than half of array,
    if count > len_n // 2:
        # leader is candidate
        leader = candidate
    # return leader
    return leader
fast_leader([6, 8, 4, 6, 8, 6, 6])
def golden_leader(arr_a):
    """O(n)"""
    # define length of array
    len_n = len(arr_a)
    # begin size at zero
    size = 0
    # iterate through array
    for ndx_k in range(len_n):
        if size == 0:
            size += 1
            value = arr_a[ndx_k]
        else:
            if value != arr_a[ndx_k]:
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for ndx_k in range(len_n):
        if arr_a[ndx_k] == candidate:
            count += 1
    if count > len_n // 2:
        leader = candidate
    return leader
# debugging
golden_leader([6, 8, 4, 6, 8, 6, 6])
