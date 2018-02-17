# rotate array A, k times

# Assumptions:
## 1 <= N <= 100
## 1 <= K <= 100
## -1,000 <= A[i] <= 1,000

def CyclicRotation(A, K){

	if 0 < len(A):

		N = 0
		while N < K:
			A = [A[len(A)-1]]+A[0:(len(A)-1)]
		N = N + 1

	return(A)
}

# console testing
print("CyclicRotation([3,8,9,7,6], 3); expect [9,7,6,3,8]: "+CyclicRotation([3,8,9,7,6], 3))
print("CyclicRotation([1,2,3,4], 4); expect [1,2,3,4]: "+CyclicRotation([1,2,3,4], 4))

# codility testing:
## https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
## note: function must be renamed to "solution" for testing
## performance: not assessed
## correctness: 100%

## Difficulty: Painless
