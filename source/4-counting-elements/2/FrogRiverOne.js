// A function returning the distance along an array/list required to acquire integers 1 through X
// Definitions
/// A = zero-indexed array
/// N = length of A
/// k = indices of array A (0 through (N - 1))
/// X = steps needed to jump
// Assumptions
/// 1 <= X <= 100000
/// 1 <= N <= 100000
/// 1 <= Ak <= X
function FrogRiverOne(X, A) {
    var i = [];
    while (i.length <= X) {
        i.push(0);
    }
    var Count = 0;
    for (var n = 0; n < A.length; n++) {
        if (A[n] != i[A[n] - 1]) {
            i[A[n] - 1] = A[n];
            Count = Count + 1;
            if (Count == X) {
                return (n);
            }
        }
    }
    return (-1);
}
// console testing:
console.log("FrogRiverOne(5, [1,3,1,4,2,3,5,4]). Expect 6:" + FrogRiverOne(5, [1, 3, 1, 4, 2, 3, 5, 4]));
console.log("FrogRiverOne(1, [1]). Expect 0:" + FrogRiverOne(1, [1]));
console.log("FrogRiverOne(5,[3]). Expect -1:" + FrogRiverOne(5, [3]));
// Codility Testing:
/// https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
/// Correctness: 100%
/// Performance: 100%
/// Difficulty: Painless
