// N voracious fish are moving along a river. Calculate how many fish are alive.
function Fish(arr_a, arr_b) {
    // begin with a fish_count of zero
    var fish_count = 0;
    // keep track of fish traveling downstream
    var fish_down = [];
    // loop through indices of arrays
    for (var ndx_i = 0; ndx_i < arr_a.length; ndx_i++) {
        // test whether fish is traveling downstream
        if (arr_b[ndx_i] == 1) {
            // if so, append to fish_down
            fish_down.push(arr_a[ndx_i]);
        }
        else {
            // test whether there are any fish it will meet
            while (fish_down.length != 0) {
                // if so, test whether it will eat the nearest downstream fish
                if (fish_down[fish_down.length - 1] < arr_a[ndx_i]) {
                    // if so, remove downstream fish from downstream list
                    fish_down.pop();
                    // if the downstream fish will eat the index fish,
                }
                else {
                    break;
                }
            }
            // if it meets none or eats all, add it to fish count:
            if (fish_down.length == 0) {
                // add index fish to survival count
                fish_count += 1;
            }
        }
    }
    // downstream fish who remained in the fish_down array have not been 'popped', so add to fish_count
    fish_count += fish_down.length;
    return (fish_count);
}
// Bash Testing:
// import { } from 'node';
// var myPattern = new RegExp('\\], *\\[');
// var ARGS_A = process.argv[2]
// ARGS_A = ARGS_A.replace(/^\[|\]$/g, '')
// ARGS_A = ARGS_A.split(RegExp('\\],* *\\['));
// var ARGS_B = ARGS_A[1].split(RegExp(', *')).map(function (item) { return (parseInt(item)); });
// ARGS_A = ARGS_A[0].split(RegExp(', *')).map(function (item) { return (parseInt(item)); });
var ARGS_A = [7947, 21515, 15142, 25406, 4233, 14639, 21604, 4975, 23853, 26088];
var ARGS_B = [1, 1, 0, 0, 1, 1, 0, 1, 1, 0];
var result = Fish(ARGS_A, ARGS_B);
// var result = Fish([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]);
// var time2 = Date.now();
// eslint-disable-next-line no-console
console.log('result: ' + result); //+ ' ; milliseconds: ' + (time2 - time1));
// Codility Testing:
/// https://app.codility.com/demo/results/trainingD5299M-NNJ/
/// training42TT5X-QKF/
/// Correctness: 100%
/// Performance: 100%
/// trainingXFRTM3-GER - continuous while loop issue
/// Difficulty: Painless
