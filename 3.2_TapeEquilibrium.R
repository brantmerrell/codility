# return the minimal difference that can be acheived by splicing A and subtracting one splice from another

# Assumptions:
## 2 <= N <= 100,000
## -1,000 <= A[i] <= 1,000


TapeEquilibrium <- function(A){
	# convert A to numeric vector
	A <- unlist(A)

	# define N and P as specified in exercise
	N <- length(A)
	P <- 1:(length(A)-1)

	# compare first sum1 and sum2 of A
	sum1 <- A[1]
	sum2 <- sum(A[2:length(A)])

	# store difference in object Diff
	Diff <- abs(sum1-sum2)

	# Agggregate all other sum differences into vector Diff
	for(n in 2:N){
		sum1 <- sum1 + A[n]
		sum2 <- sum2 - A[n]
		Diff <- c(Diff, abs(sum1-sum2))
	}

	# return minimum of vector Diff
	return(min(Diff))
}

# Console Testing:
print(c("TapeEquilibrium(list(3,1,2,4,3)); expect 1: ", TapeEquilibrium(list(3,1,2,4,3))))

# Codility testing: 
## https://app.codility.com/programmers/lessons/3-time-complexity/tape_equilibrium/
## R language not scored
