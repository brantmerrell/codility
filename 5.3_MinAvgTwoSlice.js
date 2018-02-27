// Return starting number for minimal slice
// Assumptions:
/// 2 <= A.length <= 100,000
/// -10,000 <= A[i] <= 10,000
function MinAvgTwoSlice(A) {
    // set minimal average at the beginning of the array
    var av_min = (A[0] + A[1]) / 2;
    // define a compare variable (as anything, really)
    var compare = av_min;
    // set corresponding index at the beginning of the array
    var index_min = 0;
    // loop through the array
    for (var n = 0; n < A.length; n++) {
        // restrict 3-element assessment for indices at least 1 element from array's end
        if (n + 1 < A.length) {
            // create two-element comparison for average slice
            compare = (A[n] + A[n + 1]) / 2;
            // test whether comparison is smaller than current estimate
            if (compare < av_min) {
                // if so, redefine current estimate as comparison
                av_min = compare;
                // and redefine current index as comparison
                index_min = n;
            }
            // restrict 3-element assessment for indices at least 2 elements from array's end
        }
        if (n + 2 < A.length) {
            // create three-element comparison for average slice
            compare = (A[n] + A[n + 1] + A[n + 2]) / 3;
            // test whether comparison is smaller than current estimate
            if (compare < av_min) {
                // if so, redefine current estimate as comparison
                av_min = compare;
                // and redefine current index as comparison
                index_min = n;
            }
        }
    }
    // return smallest index
    return (index_min);
}
// Bash Testing:
var args = process.argv[2];
args = args.replace(/^\[|\]$/g, "").split(",").map(function (item) { return (parseInt(item)); });
var time1 = Date.now()
var result = MinAvgTwoSlice(args);
var time2 = Date.now()
console.log("result: "+result+" ; milliseconds: "+ (time2-time1))
// Codility Testing:
/// https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
/// Correctness: 100%
/// Performance: 100%
/// Difficulty: Respectable
