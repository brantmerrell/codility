// maximize A[P]*A[Q]*A[R] for any triplet (P,Q,R)
// Assumptions:
/// 3 <= N <= 100,000
/// -1,000 <= A[i] <= 1,000
function MaxProductOfThree(A) {
    // sort array
    A = A.sort(function (a, b) { return (a - b); });
    // determine whether the product of the two smallest is greater than their positive competitors
    if((A[A.length-2]*A[A.length-3]) < (A[0]*A[1])){
	// if so, multiply two smallest by the largest
	return (A[0] * A[1] * A[A.length-1])
    }else{
        // if not, multiply the three largest numbers
	return (A[A.length - 1] * A[A.length - 2] * A[A.length - 3])
    }
}
/// Console Testing
console.log("MaxProductOfThree([-3,1,2,-2,5,6]); expect 60: " + MaxProductOfThree([-3, 1, 2, -2, 5, 6]));
console.log("MaxProductOfThree([-10,-2,-5,5,5,5]); expect 250: " + MaxProductOfThree([-10,-2,-5,5,5,5]));
// Codility Testing
/// https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
/// performance: 40%
	/// got 997002000 expected 999000000
	/// got 50000 expected 5000000
	/// got 1 expected 4
/// correctness: 50%
	/// got 84 expected 105
	/// got 60 expected 120
	/// got -100 expected 125
/// Difficulty: Painless

