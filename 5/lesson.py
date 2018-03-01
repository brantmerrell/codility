"""https://codility.com/media/train/3-PrefixSums.pdf"""
def prefix_sums(arr_a):
    """5.1 Counting prefix sums"""
    len_n = len(arr_a)
    arr_res = [0] * (len_n + 1)
    for k in range(1, len_n + 1):
        arr_res[k] = arr_res[k - 1] + arr_a[k - 1]
    return arr_res
def count_total(arr_p, int_x, int_y):
    """5.2 total of one slice"""
    return arr_p[int_y + 1] - arr_p[int_x]
def mushrooms(arr_a, int_k, int_m):
    """5.3 mushroom picker"""
    result = 0
    arr_pref = prefix_sums(arr_a)
    for ndx_p in range(min(int_m, int_k) + 1):
        left_pos = int_k - ndx_p
        right_pos = min(len(arr_a) - 1, max(int_k, int_k + int_m - 2 * ndx_p))
        result = max(result, count_total(arr_pref, left_pos, right_pos))
    for ndx_p in range(min(int_m + 1, len(arr_a) - int_k)):
        right_pos = int_k + ndx_p
        left_pos = max(0, min(int_k, int_k - int_m - 2 * ndx_p))
        result = max(result, count_total(arr_pref, left_pos, right_pos))
        