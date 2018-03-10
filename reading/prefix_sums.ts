// https://codility.com/media/train/3-PrefixSums.pdf
function prefix_sums(arr_a){
    // 5.1 Counting prefix sums
    // define length
    var len_n = arr_a.length;
    // array result (arr_res) should have length len_n+1
    // (its first and last elements should respectively be the sum of none & of all)
    var arr_res = [0];
    while(arr_res.length < len_n){
        arr_res.push(0);
    }
    // iterate from 2nd index (1) to last (len_n+1)
    for(var k=1; k<len_n+1; k++){
        // add the most recent sum to arr_a's corresponding index
        // (arr_a's corresponding index is [k - 1])
        arr_res[k] = arr_res[k - 1] + arr_a[k - 1];
    }
    return(arr_res);
}
function count_total(arr_p, ndx_x, ndx_y){
    // 5.2 total of one slice
    // because arr_p was built as a sequential sum from arr_a,
    // the sum of a range in arr_a == the difference between two points of arr_p
    var result = arr_p[ndx_y + 1] - arr_p[ndx_x];
    return(result);
}
function mushrooms(arr_a, pos_k, mov_m){
    // 5.3 mushroom picker O(n+m)
    // store length of input array
    var len_n = arr_a.length;
    // define result as lowest theoretical possibility
    var result = 0;
    // generate array of prefix sums
    var arr_pref = prefix_sums(arr_a);
    //  LOOP 1: TRAVELLING LEFT THEN RIGHT
    //  define the maximum leftwards distance that can be travelled from pos_k
    //  max leftwards distance is limited by both the distance limit (mov_m)
    //  and by the number of elements that exist to the left of pos_k.
    var indexMax = Math.min(mov_m, pos_k);
    // pos_k - index_max must be the 1st index, which is zero. So add 1 to index_max
    indexMax += 1;
    //  iterate from 0 to index_max
    for(var ndx_p=0; ndx_p<indexMax; ndx_p++){
        // define index of left boundary of range as distance ndx_p to the left of pos_k
        var pos_left = pos_k - ndx_p;
        // define leftover allowed distance after travelling
        // from pos_k to pos_left and back (mov_m - 2 * ndx_p),
        // and add to pos_k to obtain rightwards range boundary
        var pos_right = pos_k + mov_m - 2 * ndx_p;
        // if this puts pos_right to the left of starting point, define as starting point
        pos_right = Math.max(pos_right, pos_k);
        // if pos_right is outside array boundary, redefine as last index
        pos_right = Math.min(pos_right, len_n - 1);
        // call count_total to generate the sum of elements within travel range
        // if the output of count_total is higher than result, redefine result
        result = Math.max(result, count_total(arr_pref, pos_left, pos_right));
    }
    // LOOP 2: TRAVELLING RIGHT THEN LEFT
    // store the maximum rightwards distance from pos_k through which to iterate
    // rightwards distance is limited by allowed travel distance (mov_m + 1),
    // as well as the distance from pos_k to the end of the array
    indexMax = Math.min(mov_m + 1, len_n - pos_k);
    // iterate from 0 to maximum rightwards distance
    for(ndx_p=0; ndx_p<indexMax; ndx_p++){
        // define rightwards range boundary as ndx_p indices to the right of pos_k
        pos_right = pos_k + ndx_p;
        // define leftover allowed distance after travelling
        // from pos_k to pos_right and back (mov_m - 2 * ndx_p),
        // and subtract from pos_k to obtain leftwards range boundary
        pos_left = pos_k - (mov_m - 2 * ndx_p);
        // if this puts pos_left to the right of starting point, define as starting point
        pos_left = Math.min(pos_left, pos_k);
        //  if pos_left is lower than zero, define as zero
        pos_left = Math.max(pos_left, 0);
        // call count_total to generate the sum of elements within travel range
        // if the output of count_total is higher than result, redefine result
        result = Math.max(result, count_total(arr_pref, pos_left, pos_right));
    }
    // return result
    return(result);
}
// eslint-disable-next-line no-unused-vars
var result = mushrooms([2,3,7,5,1,3,9], 4, 6);
