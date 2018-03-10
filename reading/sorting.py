"""https://codility.com/media/train/4-Sorting.pdf"""
def selection_sort(arr_a):
    """6.1 Selection Sort - O(n^2)"""
    # define length of array
    len_n = len(arr_a)
    # iterate through array
    for ndx_k in range(len_n):
        # define minimum index
        minimal = ndx_k
        # iterate through indices through which ndx_k loop has not iterated
        for j in range(ndx_k+1, len_n):
            # test for elements smaller than the minimal element so far
            if arr_a[j] < arr_a[minimal]:
                # redefine minimal index
                minimal = j
            # switch smallest element with index k
            arr_a[ndx_k], arr_a[minimal] = arr_a[minimal], arr_a[ndx_k]
        # return sorted array
        return arr_a
print selection_sort([5, 2, 8, 14, 1, 16])
def counting_sort(arg_a, int_k):
    """6.2 Counting Sort - O(n+k)"""
    count = [0]*int_k
    for i, j in enumerate(arg_a):
        count[j] += 1
    var_p = 0
    for i in range(int_k + 1):
        for j in range(count[i]):
            arg_a[var_p] = i
            var_p += 1
    return arg_a
print counting_sort([5, 2, 8, 14, 1, 16], 5)
def distinct(arr_a):
    """6.4 The number of distinct values - O(n log n)"""
    arr_a.sort()
    result = 1
    for k in range(1, len(arr_a)):
        if arr_a[k] != arr_a[k-1]:
            result += 1
    return result
print distinct([5, 2, 8, 14, 1, 16])
