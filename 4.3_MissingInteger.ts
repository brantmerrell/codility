// A function returning the first missing positive integer from an array / list.
// Assumptions
/// -1,000,000 <= An <= 1,000,000
/// 1 <= N <= 100,000, where N is the length of A
function MissingInteger(A){
	// remove negatives, zeros, and duplicates from array
	A = A.filter(function(item,pos){
		return(A.indexOf(item)==pos && 0<item)
	}) 
	// sort array
	A = A.sort(function(a,b){return(a-b)})
	// return 1 for empty sets, and for non-empty sets without 1
	if(A.length == 0 || A[0]!=1){
			return(1)
	}
	// return next number for sets filled from 1 to N
	if(A.length==Math.max.apply(Math,A)){
		return(A.length+1)
	}
	// crawl through index for sets
	for(var i=0; i<A.length; i++){
		// test for increases greater than 1
		if(A[i+1] - A[i] > 1){
			// return smallest skipped number
			return(A[i]+1)
		} 
	}
}
// console testing:
console.log("MissingInteger([1,3,6,4,1,2]); Expect 5:" + MissingInteger([1,3,6,4,1,2]))
console.log("MissingInteger([1,2,3]); Expect 4:" + MissingInteger([1,2,3]))
console.log("MissingInteger([-1,-3]); Expect 1:" + MissingInteger([-1,-3]))
console.log("MissingInteger([4,5,6,2]); Expect 1:" + MissingInteger([4,5,6,2]))
// codility testing:
/// https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
/// performance: 25% - timeout errors
/// correctness: 100%
/// Difficulty: Painless
