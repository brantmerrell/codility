# A function returning the first missing positive integer from an array / list.
# Assumptions
## -1,000,000 <= A[n] <= 1,000,000
## 1 <= N <= 100,000, where N is the length of A
# Numpy module cannot be imported for codility test
def MissingInteger(A):
	# make list unique
	A = set(A) 
	# remove negatives from list
	A = [item for item in A if 0 < item] 
	# sort any list too long for the set() function
	A = sorted(A) 
	# define N as defined in problem
	N = len(A) 
	# identify empty sets to avoid errors
	if N == 0: 
		# return 1 for empty sets
		return(1) 
	# return 1 for non-empty sets without 1
	if not A[0]==1: 
		return(1)
	# return next number for sets filled from 1 to N
	if max(A)==N: 
		return(N+1)
	# crawl through index for sets
	for i in range(0, N-1): 
		# test for increases greater than 1
		if A[i+1] - A[i] > 1: 
			# return smallest skipped number
			return(A[i]+1) 
		
# console testing:
print(["MissingInteger([1,3,6,4,1,2]); Expect 5:"] + [MissingInteger([1,3,6,4,1,2])])
print(["MissingInteger([1,2,3]); Expect 4:"] + [MissingInteger([1,2,3])])
print(["MissingInteger([-1,-3]); Expect 1:"] + [MissingInteger([-1,-3])])
print(["MissingInteger([4,5,6,2]); Expect 1:"] + [MissingInteger([4,5,6,2])])
# codility testing:
## https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
## performance: 100%
## correctness: 100%
## Difficulty: Painless
