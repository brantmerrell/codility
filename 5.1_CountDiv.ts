// compute number of integers divisible by K in range A...B

// Assumptions:
// 0 <= A < = 2,000,000,000
// 0 <= B < = 2,000,000,000
// 1 <= K < = 2,000,000,000
// A <= B

function CountDiv(A,B,K){

	// redefine A as lowest in-range number divisible by K
	while(A  % K !=0){
		A = A + 1
	}

	// redefine B as highest in-range number divisible by K
	while(B % K !=0){
		B = B - 1
	}

	// if A and B are in range (A is still smaller than B),
	if(A < B){
		// then their difference is divisible by K,
		// and (B-A)/K provides the "leaps" from A to B.
		// Thus, adding 1 to include A provides the result.
		return((B-A)/K+1)
	}

	// if A and B are the same, they correspond to only in-range number which divides by K.
	if(A == B){
		// Thus, only one in-range number divides by K.
		return(1)
	}
	// if redefining A and B caused B < A, then no in-range number divides by K.
	if(B < A ){return(0)}
}

// console testing:
console.log("CountDiv(6,11,2); expect 3: "+CountDiv(6,11,2))
console.log("CountDiv(0,0,1); expect 1: "+CountDiv(0,0,1))
console.log("CountDiv(11,345,17); expect 20: "+CountDiv(11,345,17))
console.log("CountDiv(1,1,11); expect 0: "+CountDiv(1,1,11))
console.log("CountDiv(10,10,7); expect 0: "+CountDiv(10,10,7))


// Codility testing:
/// https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
/// Performance: 100%
/// Correctness: 100%
/// Note: the intuitive for-loop yielded results of 0% and 100%, respectively.

/// Difficulty: Painless
