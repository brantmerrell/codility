// compute number of distinct values in an array
// Assumptions:
/// 0 <= N <= 100,000
/// -1,000,000 <= A[i] <= 1,000,000
function Distinct(A){
	A = A.filter(function(value,index,self){return(self.indexOf(value)==index)})
	return(A.length)
}
// Console Testing
console.log("Distinct([2,1,1,2,3,1]); expect 3: "+Distinct([2,1,1,2,3,1]))
// Codility Testing
/// https://app.codility.com/programmers/lessons/6-sorting/distinct/
/// performance: 33%
/// correctness: 100%
/// Difficulty: Painless
