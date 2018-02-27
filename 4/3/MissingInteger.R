# A function returning the first missing positive integer from an array / list.
# Tests & expected outcomes:
# For:
A1 <- list(1,3,6,4,1,2)
# Return 5, the smallest missing positive integer
# For:
A2 <- list(1,2,3)
# Return 4, the next positive integer
# For:
A3 <- list(-1,-3)
# Return 1, the next positive integer
# For:
A4 <- list(4,5,6,2)
# Return 1
# Assumptions
## -1,000,000 <= A[n] <= 1,000,000
## 1 <= N <= 100,000, where N is the length of A
MissingInteger <- function(A){
	A <- unique(unlist(A)) # convert list to vector, make unique
	A <- A[0<A] # remove negatives from list
	A <- sort(A) # sort any list too long for the unique() function
	N <- length(A) # define N as defined in problem
	if(N == 0){ # identify empty sets to avoid errors
		return(1) # return 1 for empty sets
	}
	if(A[1]!=1){ # return 1 for non-empty sets without 1
		return(1)
	}
	if(max(A)==N){ # return next number for sets filled from 1 to N
		return(N+1)
	}
	for(i in 1:(N-1)){ # crawl through index for(sets
		if(A[i+1] - A[i] > 1){ # test for increases greater than 1
			return(A[i]+1) # return smallest skipped number
		}
	}
}
		
print(c("MissingInteger([1,3,6,4,1,2]); Expect 5:",MissingInteger(list(1,3,6,4,1,2))))
print(c("MissingInteger([1,2,3]); Expect 4:",MissingInteger(list(1,2,3))))
print(c("MissingInteger([-1,-3]); Expect 5:",MissingInteger(list(-1,-3))))
print(c("MissingInteger([4,5,6,2]); Expect 5:",MissingInteger(list(4,5,6,2))))
# codility testing:
## https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
## R language not assessed
## Difficulty: Painless
