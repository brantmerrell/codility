// A function for testing whether a list / array is a permutation

// Assumptions:
/// 1 <= N <= 100,000
/// N is an integer
/// 1 <= A[i] <= 1,000,000,000


function PermCheck(A){
	if(A.length < Math.max.apply(Math,A)){
		return(0)
	}else{
		// test whether A is free of duplicates
		var A_unique = A.filter(function(item,pos){return(A.indexOf(item)==pos)})
		return((A_unique.length==A.length) >>> 0)
	}
}
	

// Console testing:
console.log(["PermCheck([1]); Expect 1: "] + [PermCheck([1])]) 
console.log(["PermCheck([51423]); Expect 0: "] + [PermCheck([51423])])
console.log(["PermCheck([4,1,3,2]); Expect 1: "]+[PermCheck([4,1,3,2])])
console.log(["PermCheck([4,1,3]); Expect 0:"]+[PermCheck([4,1,3])])
console.log(["PermCheck([4,4,3,2]); Expect 0:"]+[PermCheck([4,4,3,2])])
console.log(["PermCheck([53,54]); Expect 0:"] + [PermCheck([53,54])])

// Codility Testing:
/// https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
/// Correctness: 100%
/// Performance: 33%
