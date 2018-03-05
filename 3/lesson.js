// https://codility.com/media/train/3-PrefixSums.pdf

function prefix_sums(arr_a){
    // 5.1 Counting prefix sums
    var len_n = arr_a.length;
    var arr_res = [0];
    while(arr_res.length < len_n){
        arr_res.push(0);
    }
    for(var k=1; k<len_n+1; k++){
        arr_res[k] = arr_res[k - 1] + arr_a[k - 1];
    }
    return(arr_res);
}
function count_total(arr_p, int_x, int_y){
    // 5.2 total of one slice
    return(arr_p[int_y + 1] - arr_p[int_x]);
}
function mushrooms(arr_a, int_k, int_m){
    // 5.3 mushroom picker O(n+m)
    var int_n = arr_a.length;
    var result = 0;
    var arr_pref = prefix_sums(arr_a);
    console.log({'prefix':arr_pref});
    for(var ndx_p=0; ndx_p<Math.min(int_m, int_k) + 1; ndx_p++){
        var left_pos = int_k - ndx_p;
        var right_pos = Math.min(int_n - 1, Math.max(int_k, int_k + int_m - 2 * ndx_p));
        result = Math.max(result, count_total(arr_pref, left_pos, right_pos));
        console.log({'loop':1,'p':ndx_p, 'k':int_k, 'A[p]':arr_a[ndx_p], 'left':left_pos, 'right':right_pos, 'result':result});
    }
    for(ndx_p=0; ndx_p<Math.min(int_m + 1, int_n - int_k); ndx_p++){
        right_pos = int_k + ndx_p;
        left_pos = Math.max(0, Math.min(int_k, int_k - (int_m - 2 * ndx_p)));
        result = Math.max(result, count_total(arr_pref, left_pos, right_pos));
        console.log({'loop':2,'p':ndx_p,'k':int_k,'A[p]':arr_a[ndx_p], 'left':left_pos, 'right':right_pos, 'result':result});
    }
    return(result);
}
console.log({'array':[2,3,7,5,1,3,9],'k':4, 'm':6});
console.log(mushrooms([2,3,7,5,1,3,9], 4, 6));
