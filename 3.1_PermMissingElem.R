# returns the missing element of numeric array A

# Assumptions:
## 0 <= N <= 100,000
## the elements of A are all distinct
## 1<= A[i] <= N+1

PermMissingElem <- function(A){
	A <- as.numeric(unlist(A))	# convert to numeric vector
	N <- length(A)			# define N as length of A, as given
	if(N==0 | min(A)!=1){		# if set is missing 1 (including if empty),
		return(1)			# then missinge element is 1
	}else if(max(A)==N){		# if no skips exist in set (assume it begins at 1),
		return(max(A)+1)		# then missing integer is at end of (sorted) set
	}else{				# otherwise missing element is between max and min, so:
		A <- sort(A)			# 1) sort the set
		for(n in 1:N){			# 2) crawl through the set
			if(A[n]>n){		# 3) A[n] > n when crawl skips an integer
				return(n)		# then n = missing integer
			}
		}
	}
}

# Console Testing:
print(c("Empty list - list()", PermMissingElem(list())))
print(c("Single element - list(3)", PermMissingElem(list(3))))
print(c("Single element - list(1)", PermMissingElem(list(1))))
print(c("Missing first - list(3,2,5,4)", PermMissingElem(list(3,2,5,4))))
print(c("Missing last - list(1,2,4,3)", PermMissingElem(list(1,2,4,3))))
print(c("Double - list(1,3)", PermMissingElem(list(1,3))))
print(c("Practice - list(2,3,1,5)", PermMissingElem(list(2,3,1,5))))

# Codility testing: 
## https://app.codility.com/programmers/lessons/3-time-complexity/perm_missing_elem/
## R language not scored
## Difficulty: Painless
