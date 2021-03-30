// Find an index of an array such that its value occurs at more than half of indices in the array.
function dominator(arr_a){
    // create objects to track recurrences of each element in array
    var counts = {};
    // iterate through array
    for (var ndx_i = 0; ndx_i < arr_a.length; ndx_i++) {
        // test whether counts object lists element ? if so, add one : if not, set at one
        counts[arr_a[ndx_i]] = counts[arr_a[ndx_i]] ? counts[arr_a[ndx_i]] + 1 : 1;
        // test whether more than half the array matches the count of elements
        if(arr_a.length < counts[arr_a[ndx_i]] * 2){
            // if so, return ndx_i
            return(ndx_i);
        }
    }
    return(-1);
}
// Debugging:
ARGS_A = [3,4,3,2,3,-1,3,3];
dominator(ARGS_A);
// Bash testing:
var ARGS_A = process.argv[2]; // read arguments from command line
ARGS_A = ARGS_A.replace(/\[|\]/g,''); // remove brackets
ARGS_A = ARGS_A.split(/, */); // split by commas
ARGS_A = ARGS_A.map(Number);
// eslint-disable-next-line no-console
console.log(dominator(ARGS_A));
// Codility testing:
// https://app.codility.com/demo/results/trainingP29RER-XEA/
// Correctness: 100%
// Performance: 100%
// Difficulty: Painless
