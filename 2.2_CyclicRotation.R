# rotate array A, k times

# Assumptions:
## 1 <= N <= 100
## 1 <= K <= 100
## -1,000 <= A[i] <= 1,000

CyclicRotation <- function(A, K){
	# set N as zero
	A <- unlist(A); N = 0
	
	while(N < K){
		A <- c( A[ length(A) ], A[ -length(A) ])
		N <- N + 1
	}
	A
}

# console testing
print(paste("CyclicRotation(list(3,8,9,7,6), 3); expect [9,7,6,3,8]:",paste(CyclicRotation(list(3,8,9,7,6), 3),collapse=" ")))
print(paste("CyclicRotation(list(1,2,3,4), 4); expect [1,2,3,4]: ",paste(CyclicRotation(list(1,2,3,4), 4),collapse=" ")))

# Codility testing: 
## https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
## R language not scored
