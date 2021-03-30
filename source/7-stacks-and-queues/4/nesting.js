// Determine whether a given string of parentheses (single type) is properly nested.
function nesting(str_s) {
    // set the balance of parentheses at zero
    var balance = 0;
    // iterate through the string of parentheses
    for (var ndx_i = 0; ndx_i < str_s.length; ndx_i++) {
        // test whether it's a left parenthesis
        if (str_s.charAt(ndx_i) == '(') {
            // add to balance for left parentheses
            balance += 1;
        }
        else {
            // subtract from balance for right parentheses
            balance -= 1;
            // there should never be more right parentheses
            if (balance < 0) {
                // if there are, return zero
                return (0);
            }
        }
    }
    // a balance of zero indicates balance
    if (balance == 0) {
        return (1);
    }
    // any other balance score indicates imbalance
    return (0);
}
// Debugging:
// nesting('())');
// nesting('(()(())())');
// Bash Testing:
var ARGS_S = process.argv[2];
// eslint-disable-next-line no-console
console.log(nesting(ARGS_S));
// Codility Testing:
// https://app.codility.com/demo/results/training9SXBGM-RC4/
// Correctness: 100%
// Performance: 100% 
// Difficulty: Painless
