# A function returning the distance along an array/list required to acquire integers 1 through X

# Definitions
## A = zero-indexed array
## N = length of A
## k = indices of array A (0 through (N - 1))
## X = steps needed to jump

# Assumptions
## 1 <= X <= 100000
## 1 <= N <= 100000
## 1 <= A[k] <= X

# Note: Module numpy cannot be imported in python exercise

def FrogRiverOne(X, A):
	N = len(A)
	i = [0]*X
	Count = 0
	for n in xrange(0,N):
		if not A[n]==i[A[n]-1]:
			i[A[n]-1] = A[n]
			Count = Count+1
			if Count==X:
				return(n)
	return(-1)
# Console Testing:
print(["FrogRiverOne(5, [1,3,1,4,2,3,5,4]). Expect 6:"]+[FrogRiverOne(5,[1,3,1,4,2,3,5,4])])
print(["FrogRiverOne(1, [1]). Expect 0:"]+[FrogRiverOne(1, [1])])
print(["FrogRiverOne(5,[3]). Expect -1:"]+[FrogRiverOne(5,[3])])

# Codility Testing:
## https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
## Correctness: 100%
## Performance: 0%
