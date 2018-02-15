# A function for testing whether a list / array is a permutation

# Assumptions:
## 1 <= N <= 100,000
## N is an integer
## 1 <= min(A) 
## max(A) <= 1,000,000,000


# Example:
A1 <- list(4,1,3,2) # is permutation
names(A1) <- 0:(length(A1)-1) # check zero-indexed inputs
A0 <- list(4,1,3) # is not permutation
names(A0) <- 0:(length(A0)-1) # check zero-indexed inputs

PermCheck <- function(A){
	A <- unlist(A) 
	N <- length(A)
	if(N<max(A)){
		return(0)
	}else{
		return(as.integer(length(unique(A))==N))
	}
}
	

# testing
print(paste("Is a list of integer 1 list(1) a permutation? Expect 1:       ",PermCheck(list(1))))
print(paste("Is a list of 1 integer list(51423) a permutation? Expect 0:       ",PermCheck(list(51423))))
print(paste("Is a large integer 1000000000 a permutation? expect 0        ",PermCheck(1000000000))) 
print(paste("Is zero-indexed list(4,1,3,2) a permutation? Expect 1        ",PermCheck(A1)))
print(paste("Is zero-indexed list(4,1,3) a permutation? Expect 0        ", PermCheck(A0)))
print(paste("repeat values: is list(4,4,3,2) a permutation? Expect 0        ", PermCheck(list(4,4,3,2))))
print(paste("Are two consecutive numbers list(53,54) a permutation? Expect 0        ",PermCheck(list(53,54))))

# Codility score: 100% ((Correctness+Performance)/2) (2nd attempt)
# First attempt failed to note that a permutation must begin with the integer 1
