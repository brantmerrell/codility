"""https://codility.com/media/train/3-PrefixSums.pdf"""

prefix_sums <- function(arr_a){
    len_n = length(arr_a)
    arr_res = rep(0, len_n + 1)
    for(k in 1:(len_n + 1)){
        arr_res[k] = arr_res[k - 1] + arr_a[k - 1]
    }
    return(arr_res)
}
count_total <- function(arr_p, int_x, int_y){
    return arr_p[int_y + 1] - arr_p[int_x]
}
def mushrooms(arr_a, int_k, int_m):
    """5.3 mushroom picker O(n+m)"""
    int_n = len(arr_a)
    result = 0
    arr_pref = prefix_sums(arr_a)
    for ndx_p in range(min(int_m, int_k) + 1):
        left_pos = int_k - ndx_p
        right_pos = min(int_n - 1, max(int_k, int_k + int_m - 2 * ndx_p))
        result = max(result, count_total(arr_pref, left_pos, right_pos))
        print({"loop":1, "A[p]":arr_a[ndx_p], "left":left_pos, "right":right_pos, "result":result})
    for ndx_p in range(min(int_m + 1, int_n - int_k)):
        right_pos = int_k + ndx_p
        left_pos = max(0, min(int_k, int_k - (int_m - 2 * ndx_p)))
        result = max(result, count_total(arr_pref, left_pos, right_pos))
        print({"loop":2, "left":left_pos, "right":right_pos, "result":result})
    return result
