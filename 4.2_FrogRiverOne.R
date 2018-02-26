# A function returning the distance along which an array/list A (of integers) must be traveled to encounter integers 1 through X
# Definitions
## A = zero-indexed array
## N = length of A
## k = indices of array A (0 through (N - 1))
## X = steps needed to jump
# Assumptions
## 1 <= X <= 100000
## 1 <= N <= 100000
## 1 <= A[k] <= X
# Example
A0 <-	list(1,3,1,4,2,3,5,4)
names(A0) <-0:(length(A0)-1)
X0 <-	5
FrogRiverOne <- function(X, A){
	N <- length(A)
	i <- rep(0,X)
	Count <- 0
	for(n in 1:N){
		if(A[[n]][1]!=i[A[[n]][1]]){
			i[A[[n]][1]] <- A[[n]][1]
			Count <- Count+1
			if(Count==X){return(n)}
		}
	}
	return(-1)
}
# Console Testing:
print(paste("FrogRiverOne(5, [1,3,1,4,2,3,5,4]). Expect 7:",FrogRiverOne(5, list(1,3,1,4,2,3,5,4))))
print(paste("FrogRiverOne(1, [1]). Expect 1:",FrogRiverOne(1, list(1))))
print(paste("FrogRiverOne(5,[3]). Expect -1:",FrogRiverOne(5,list(3))))
# Codility Testing:
## https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
## R language not assessed
## Difficulty: Painless
