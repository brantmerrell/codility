// compute number of integers divisible by K in range [A...B]

// Assumptions:
// 0 <= A < = 2,000,000,000
// 0 <= B < = 2,000,000,000
// 1 <= K < = 2,000,000,000
// A <= B

function CountDiv(A,B,K){

	// start count at zero
	var Count = 0

	// loop from A to B
	for(i=A; i<=B; i++){

		// test divisibility
		if(i % K == 0){
			// add to count
			Count=Count+1
		}
	}
	return(Count)
}

// console testing:
console.log(["CountDiv(6,11,2); expect 3: "]+[CountDiv(6,11,2)])
console.log(["CountDiv(0,0,1); expect 0 or 1? "]+[CountDiv(0,0,1)])

// Codility testing:
/// https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
/// Performance: 0%
/// Correctness: 50%
