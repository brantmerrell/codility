# https://codility.com/media/train/3-PrefixSums.pdf

prefix_sums <- function(arr_a){
    # define length
    len_n <- length(arr_a)
    # array result (arr_res) should have length len_n+1
    # (its first and last elements should respectively be the sum of none & of all)
    arr_res <- rep(0, len_n + 1)
    # iterate from 2nd index (1) to last (len_n+1)
    for(k in 2:(len_n + 1)){
        # add the most recent sum to arr_a's corresponding index
        # (arr_a's corresponding index is [k - 1])
        arr_res[k] <- arr_res[k - 1] + arr_a[k - 1]
    }
    # return array result
    return(arr_res)
}
count_total <- function(arr_p, int_x, int_y){
    # 5.2 total of one slice
    # because arr_p was built as a sequential sum from arr_a,
    # the sum of a range in arr_a == the difference between two points of arr_p
    result <- arr_p[int_y + 1] - arr_p[int_x]
    return(result)
}
mushrooms <- function(arr_a, pos_k, mov_m){
    # store length of input array
    len_n <- length(arr_a)
    # define result as lowest theoretical possibility
    result <- 0
    # generate array of prefix sums
    arr_pref <- prefix_sums(arr_a)
    # LOOP 1: TRAVELLING LEFT THEN RIGHT
    # define the maximum leftwards distance that can be travelled from pos_k
    # max leftwards distance is limited by both the distance limit (mov_m)
    # and by the number of elements that exist to the left of pos_k.
    index_max <- min(mov_m, pos_k)
    # iterate from 1 to index_max
    for(ndx_p in seq(index_max)){
        # define index of left boundary of range as distance ndx_p to the left of pos_k
        pos_left <- pos_k - ndx_p
        # define leftover allowed distance after travelling
        # from pos_k to pos_left and back (mov_m - 2 * ndx_p),
        # and add to pos_k to obtain rightwards range boundary
        pos_right <- pos_k + mov_m - 2 * ndx_p
        # if this puts pos_right to the left of starting point, define as starting point
        pos_right <- max(pos_right, pos_k)
        # if pos_right is outside array boundary, redefine as last index
        pos_right <- min(pos_right, len_n)
        # call count_total to generate the sum of elements within travel range
        # if the output of count_total is higher than result, redefine result
        result <- max(result, count_total(arr_pref, pos_left, pos_right))
    }
    # LOOP 2: TRAVELLING RIGHT THEN LEFT
    # store the maximum rightwards distance from pos_k through which to iterate
    # rightwards distance is limited by allowed travel distance (mov_m + 1),
    # as well as the distance from pos_k to the end of the array
    index_max <- min(mov_m + 1, len_n - pos_k)
    # iterate from 0 to maximum rightwards distance
    for(ndx_p in seq(index_max)){
        # define rightwards range boundary as ndx_p indices to the right of pos_k
        pos_right <- pos_k + ndx_p
        # define leftover allowed distance after travelling
        # from pos_k to pos_right and back (mov_m - 2 * ndx_p),
        # and subtract from pos_k to obtain leftwards range boundary
        pos_left <- pos_k - (mov_m - 2 * ndx_p)
        # if this puts pos_left to the right of starting point, define as starting point
        pos_left <- min(pos_left, pos_k)
        # if pos_left is lower than zero, define as zero
        pos_left <- max(pos_left, 0)
        # call count_total to generate the sum of elements within travel range
        # if the output of count_total is higher than result, redefine result
        result <- max(result, count_total(arr_pref, pos_left, pos_right))
    }
    # return result
    return(result)
}
RESULT <- mushrooms(c(2, 3, 7, 5, 1, 3, 9), 4, 6)
