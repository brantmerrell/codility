// returns single non-replicated element of numeric array
// see also https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

// assumptions:
// 1 <= A.length <= 1,000,000
// 1 <= A[i] <= 1,000,000,000
// all but 1 integers occur an even number of times

function OddOccurrencesInArray(A){

	// if A is just one number, return it
	if(A.length==1){return(A[0])}

	// sort A	
	A = A.sort()

	for(i=0; i<A.length; i=i+2){
		if(A[i] != A[i+1]){return(A[i])}
	}
}

// testing
console.log("OddOccurrencesInArray(3); expect 3: "+OddOccurrencesInArray([3]))
console.log("OddOccurrencesInArray([9,3,9,3,9,7,9]); expect 7: "+OddOccurrencesInArray([9,3,9,3,9,7,9]))

// correctness: 100%
// performance: 50%

