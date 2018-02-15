// rotate array A, k times
// see also https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

function CyclicRotation(A, K){

	if(A.length!=0){

		while(A.length < K){
			K = K-A.length
		}

		var B = A.splice(-1*K);

		A = B.concat(A);
	}
	return(A);
}

//testing
console.log("CyclicRotation([3,8,9,7,6], 3); expect [9,7,6,3,8]: "+CyclicRotation([3,8,9,7,6], 3))
console.log("CyclicRotation([1,2,3,4], 4); expect [1,2,3,4]: "+CyclicRotation([1,2,3,4], 4))
