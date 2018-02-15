// returns the missing element of numeric array A

// Assumptions:
/// 0 <= N <= 100,000
/// the elements of A are all distinct
/// 1<= A[i] <= N+1

function PermMissingElem(A){

	// if set is missing 1 (including if empty),
	if((A.length==0) || (Math.min.apply(Math,A)!=1)){

	// then 1 is the missing element
		return(1)
	
 	// if no skips exist in set (and it begins at 1),
	}else if(Math.max.apply(Math,A)==A.length){

	// missing element is at end of set
		return(A.length+1) 
	
	// otherwise missing element is within set
	}else{

		// therefore, first sort the set
		A = A.sort()

		// then crawl along array and test each element
		//for n in range(0, N):
		for(n=0; n<=A.length; n++){

			// A[n] will correspond to n+1 until skipped element
			if(A[n]>n+1){

				// then, retun n+1
				return(n+1)
			}
		}
	}
}
// Console Testing:
console.log(["Empty list - []; expect 1: "]+[PermMissingElem([])])
console.log(["Single element - [1]; expect 2: "]+[PermMissingElem([1])])
console.log(["Missing first - [3,2,5,4]; expect 1: "]+[PermMissingElem([3,2,5,4])])
console.log(["Missing last - [1,2,4,3]; expect 5: "]+[PermMissingElem([1,2,4,3])])
console.log(["Double - [1,3]; expect 2: "]+[PermMissingElem([1,3])])
console.log(["Practice - [2,3,1,5]; expect 4: "]+[PermMissingElem([2,3,1,5])])

// Codility testing: 
/// https://app.codility.com/programmers/lessons/3-time-complexity/perm_missing_elem/
/// accuracy = 
/// performance = 


