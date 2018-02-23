// maximize A[P]*A[Q]*A[R] for any triplet (P,Q,R)
// Assumptions:
/// 3 <= N <= 100,000
/// -1,000 <= A[i] <= 1,000
function MaxProductOfThree(A) {
    // sort array
    A = A.sort(function (a, b) { return (a - b); });
    // multiply three largest numbers in array
    return (A[A.length - 1] * A[A.length - 2] * A[A.length - 3]);
}
/// Console Testing
console.log("MaxProductOfThree([-3,1,2,-2,5,6]); expect 60: " + MaxProductOfThree([-3, 1, 2, -2, 5, 6]));
// Codility Testing
/// https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
/// performance: 
/// correctness: 
/// Difficulty: Painless
