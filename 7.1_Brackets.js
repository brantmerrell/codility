// Determine whether a given string of parentheses is properly nested
function Brackets(S) {
    // split string into array
    var S = S.split('');
    // create object to match lefts and rights
    var match = { "]": "[", "}": "{", ")": "(" };
    // create stack to track bracket matches
    var stack = [];
    // loop through S
    for (var i = 0; i < S.length; i++) {
        // test for leftness (as opposed to rightness)
        if (match[S[i]] == undefined) {
            // if left, add to stack
            stack.push(S[i]);
            // if right, make sure stack already has an element
        }
        else if (stack.length != 0) {
            // remove an element from stack
            var POP = stack.pop();
            // removed element should equal S[i]
            if (match[S[i]] != POP) {
                // if not, return zero
                return (0);
            }
        }
    }
    // if stack.length==0 after loop finishes, the lefts and right 'balance'
    if (stack.length == 0) {
        return (1);
        // otherwise, they do not
    }
    else {
        return (0);
    }
}
// Bash Testing:
var args = process.argv[2];
// args = args.replace(/^\[|\]$/g, "").split(",").map(function (item) { return (parseInt(item)); });
var time1 = Date.now();
var result = Brackets(args);
var time2 = Date.now();
console.log("result: " + result + " ; milliseconds: " + (time2 - time1));
// Codility Testing:
/// https://app.codility.com/demo/results/trainingJ3BU8D-N8G/
/// Correctness: 100% 
/// Performance: 80%
/// Difficulty: Painless
