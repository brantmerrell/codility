
function temp(A){

	// remove negatives, zeros, and duplicates from array
	A = A.filter(function(item,pos){
		return(A.indexOf(item)==pos && 0<item)
	})
	return(A)
}


// console testing:
console.log(["temp([1,1,2,3]); Expect [1,2,3]:"] + [temp([1,2,2,3])])
console.log(["temp([-1,0,-3]); Expect []:"] + [temp([-1,0,-3])])

