function equi_leader(arr_a){
    // start equi_count at zero
    var equi_count = 0;
    // start left and rightelement counts at empty
    var obj_r = {};
    var obj_l = {};
    // iterate through array
    for(var ndx_i = 0; ndx_i < arr_a.length; ndx_i++){
        // within obj_r, set a key for each element and add for each duplicate element
        obj_r[arr_a[ndx_i]] = obj_r[arr_a[ndx_i]] ? obj_r[arr_a[ndx_i]] + 1 : 1;
        // begin all keys for left-slice tracking at value zero
        obj_l[arr_a[ndx_i]] = 0;
    }
    // iterate through array
    for(ndx_i = 0; ndx_i < arr_a.length; ndx_i++){
        // subtract from and add to right-slice & left-slice counts
        obj_r[arr_a[ndx_i]] -= 1;
        obj_l[arr_a[ndx_i]] += 1;
        // iterate through right-slice counter
        for(var key in obj_r){
            // test whether key leads right-slice
            var test = obj_r[key] * 2 > arr_a.length - 1 - ndx_i;
            // test whether key leads left-slice
            test = test && obj_l[key] * 2 > ndx_i + 1;
            // if all tests are true, add to equi_count
            if(test){
                equi_count += 1;
            }
        }
    }
    return(equi_count);
}
// debugging
// var ARR_A = [4, 3, 4, 4, 4, 2];
// equi_leader(ARR_A);
// Bash testing:
var ARGS_A = process.argv[2]; // read arguments from command line
ARGS_A = ARGS_A.replace(/\[|\]/g,''); // remove brackets
var ARGS_B = ARGS_A.split(/, */); // split by commas
var ARGS_C = ARGS_B.map(Number);
// eslint-disable-next-line no-console
console.log(equi_leader(ARGS_C));
// Codility testing:
// https://app.codility.com/demo/results/trainingS6AGA2-SPT/
// Performance: 75%
// Correctness: 100%
