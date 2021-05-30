// rotate array A, k times
// Assumptions:
/// 1 <= N <= 100
/// 1 <= K <= 100
/// -1,000 <= Ai <= 1,000
function CyclicRotation(A, K) {
	if(A.length === 0 | K === A.length | K === 0) {
		return (A)
	}
	while (K > A.length) {
		K = K - A.length
	}
	M = A.length - K;
	let second = A.slice(0,M)
	let first = A.slice(M)
	return(first.concat(second))
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
