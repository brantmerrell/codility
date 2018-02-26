// count the number of passing cars on the road.
// zeros travel up the array (east), ones travel down (west).
// PassingCars() indicates how many zeros & ones pass each other.
// Assumptions:
/// 1 <= N <= 100,000
/// Ai == 1 OR 0
function PassingCars(A) {
    // define add function
    function add(a, b) { return (a + b); }
    // count west-travelling cars
    var west = A.reduce(add);
    // subtract to count uncounted east-travelling cars
    var east = A.length - west;
    // start pairs of passing cars at zero
    var pairs = 0;
    // loop through array of cars
    for (var i = 0; i < A.length; i++) {
        // if the car is travelling east,
        if (A[i] == 0) {
            // subtract now-counted car from east
            east = east - 1;
            // add west-travelling cars for this car to pairs of passing cars
            pairs = pairs + west;
            // if pairs exceeds 1B, return -1
            if (1000000000 < pairs) {
                return (-1);
            }
            // if the car is travelling west, subtract now-counted car from west
        }
        else {
            west = west - 1;
        }
    }
    return (pairs);
}
// Bash Testing:
var args = process.argv[2];
args = args.replace(/^\[|\]$/g, "").split(",").map(function (item) { return (parseInt(item)); });
console.log(PassingCars(args));
// Codility testing:
/// https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
/// Performance: 100%
/// Correctness: 100%
/// Difficulty: Painless
