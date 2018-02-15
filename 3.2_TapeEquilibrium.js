// return the minimal difference that can be acheived by splicing A and subtracting one splice from another

// Assumptions:
/// 2 <= N <= 100,000
/// -1,000 <= A[i] <= 1,000

function TapeEquilibrium(A){

	// splice A[0] from A, store their difference in array "Diff"
	var sum1 = A[0]
	var sum2 = A.reduce(add,0);function add(a,b){return(a+b)}
	sum2 = sum2 - A[0]
	Diff = [Math.abs(sum1-sum2)]

	// build "Diff" array
	for(n=1; n<=A.length; n++){
		sum1 = sum1 + A[n]
		sum2 = sum2 - A[n]
		Diff.push(Math.abs(sum1-sum2))
	}
	// return minimum from Diff array
	return(Math.min.apply(Math,Diff))
}
// console testing:
console.log(["TapeEquilibrium([3,1,2,4,3]); expect 1: "]+[TapeEquilibrium([3,1,2,4,3])])

// Codility testing:
/// https://app.codility.com/programmers/lessons/3-time-complexity/tape_equilibrium/
/// performance:
/// correctness:

