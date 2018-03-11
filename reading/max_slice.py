"""https://codility.com/media/train/7-MaxSlice.pdf"""
def slow_max_slice(arr_a):
    """Maximal Slice - O(n^3)"""
    # define length of array
    len_n = len(arr_a)
    # begin result at zero
    result = 0
    # iterate through indices
    for ndx_p in range(len_n):
        # iterate from index to end of array
        for ndx_q in range(ndx_p, len_n):
            # begin sum_track at zero
            sum_track = 0
            # iterate from 1st to 2nd index (+1)
            for ndx_i in range(ndx_p, ndx_q + 1):
                # add element to sum_track
                sum_track += arr_a[ndx_i]
            # if result of ndx_q is greater than current result, redefine result
            result = max(result, sum_track)
    return result
# quadratic_max_slice(arr_a, pre_fix)
def quadratic_max_slice(arr_a):
    """Maximal Slice - O(N^2)"""
    # define length of array
    len_n = len(arr_a)
    # begin result at zero
    result = 0
    # iterate through indices
    for ndx_p in range(len_n):
        # begin sum_track at zero
        sum_track = 0
        # iterate from 1st to 2nd index (+1)
        for ndx_q in range(ndx_p, len_n):
            # add element to sum_track
            sum_track += arr_a[ndx_q]
            # if result of ndx_q is greater than current result, redefine result
            result = max(result, sum_track)
    return result
def golden_max_slice(arr_a):
    """Maximal Slice - O(n)"""
    # begin max_ending and max_slice at zero
    max_ending = max_slice = 0
    # iterate through elements
    for elem in arr_a:
        # if max_ending - elem > 0, define as 0
        max_ending = max(0, max_ending + elem)
        # define max slice as max(max_slice, max_ending)
        max_slice = max(max_slice, max_ending)
    # return max_slice
    return max_slice
# debugging:
ARR_A = [5, -7, 3, 5, -2, 4, -1]
slow_max_slice(ARR_A)
quadratic_max_slice(ARR_A)
golden_max_slice(ARR_A)
