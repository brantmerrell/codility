"""https://codility.com/media/train/2-CountingElements.pdf"""
def counting(arr_a, int_m):
    """4.1 counting elements"""
    count = [0]*(int_m + 1)
    for k in enumerate(arr_a):
        count[k[1]] += 1
    return count
def slow_solution(arr_a, arr_b):#  , int_m):
    """4.2 swap the elements - slow solution"""
    len_n = len(arr_a)
    sum_a = sum(arr_a)
    sum_b = sum(arr_b)
    for ndx_i in range(len_n):
        for ndx_j in range(len_n):
            change = arr_b[ndx_j] - arr_a[ndx_i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b -= change
    return False
def fast_solution(arr_a, arr_b, int_m):
    """4.3 swap the elements - fast solution"""
    len_n = len(arr_a)
    sum_a = sum(arr_a)
    sum_b = sum(arr_b)
    diff = sum_b - sum_a
    if diff % 2 == 1:
        return False
    diff //= 2
    count = counting(arr_a, int_m)
    for ndx_i in range(len_n):
        test = arr_b[ndx_i] >= 0
        test = test and arr_b[ndx_i] - diff <= int_m
        test = test and count[arr_a[ndx_i] - diff] > 0
        if test:
            return True
    return False
