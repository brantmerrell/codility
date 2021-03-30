// rotate array A, k times
// Assumptions:
/// 1 <= N <= 100
/// 1 <= K <= 100
/// -1,000 <= Ai <= 1,000
function CyclicRotation(A, K) {
    // if A is length 0, return A; otherwise, rotate:
    if (A.length != 0) {
        // reduce K to minimal rotational impact
        while (A.length < K) {
            K = K - A.length;
        }
        // splice A into A & B along point K, with K counted from the end of A
        var B = A.splice(-1 * K);
        // concatenate A and B in reverse from how they were spliced
        A = B.concat(A);
    }
    return (A);
}
// console testing:
console.log("CyclicRotation([3,8,9,7,6], 3); expect 9,7,6,3,8: " + CyclicRotation([3, 8, 9, 7, 6], 3));
console.log("CyclicRotation([1,2,3,4], 4); expect 1,2,3,4: " + CyclicRotation([1, 2, 3, 4], 4));
// codility testing:
/// https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
/// note: function must be renamed to "solution" for testing
/// performance: not assessed
/// correctness: 100%
/// Difficulty: Painless
