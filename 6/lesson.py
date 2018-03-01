"""https://codility.com/media/train/4-Sorting.pdf"""

def selection_sort(array_a):
    """6.1 Selection Sort"""
    for k in enumerate(array_a):
        minimal = k[0]
        for j in range(k[0]+1, len(array_a)):
            if array_a[j] < array_a[minimal]:
                minimal = j
            array_a[k], array_a[minimal] = array_a[minimal], array_a[k]
        return array_a

def counting_sort(arg_a, int_k):
    """6.2 Counting Sort"""
    count = [0]*int_k
    for i, j in enumerate(arg_a):
        count[j] += 1
    var_p = 0
    for i in range(int_k + 1):
        for j in range(count[i]):
            arg_a[var_p] = i
            var_p += 1
    return arg_a

def distinct(arr_a):
    """6.4 The number of distinct values"""
    arr_a.sort()
    result = 1
    for k in range(1, len(arr_a)):
        if arr_a[k] != arr_a[k-1]:
            result += 1
    return result
