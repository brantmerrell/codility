// Return starting number for minimal slice

// Assumptions:
/// 2 <= N <= 100,000
/// -10,000 <= A[i] <= 10,000

function MinAvgTwoSlice(A){
	// Define N as defined in exercise

	// let ndx be a candidate index that redefines as necessary through a loop of A:
		// track the sum of P:Q to efficiently calculate new averages
		// track the length of P:Q to efficiently calculate new averages
		// test to see whether smaller average is possible for pair of list
			// set minimal average lower for current index
		// test whether n acheives a smaller average with 1 consecutive index
			// if so, redefine i, sum, and average
}
// Console Testing:
console.log({"MinAvgTwoSlice([4,2,2,5,1,5,8]); expect 1": MinAvgTwoSlice([4,2,2,5,1,5,8])})
console.log({"MinAvgTwoSlice([8,4]); expect 0": MinAvgTwoSlice([8,4])})

// Codility Testing:
/// https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
/// Correctness: 
/// Performance: 
/// Difficulty: Respectable
