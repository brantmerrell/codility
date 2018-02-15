# A function returning the first missing positive integer from an array / list.

# Tests & expected outcomes:
# For:
A1 = [1,3,6,4,1,2]
# Return 5, the smallest missing positive integer

# For:
A2 = [1,2,3]
# Return 4, the next positive integer

# For:
A3 = [-1,-3]
# Return 1, the next positive integer

# For:
A4 = [4,5,6,2]
# Return 1

# Assumptions
## -1,000,000 <= A[n] <= 1,000,000
## 1 <= N <= 100,000, where N is the length of A

# Numpy module cannot be imported for codility test

def MissingInteger(A):
	A = set(A) # make list unique
	A = [item for item in A if 0 < item] # remove negatives from list
	A = sorted(A) # sort any list too long for the set() function
	N = len(A) # define N as defined in problem
	if N == 0: # identify empty sets to avoid errors
		return(1) # return 1 for empty sets
	if not A[0]==1: # return 1 for non-empty sets without 1
		return(1)
	if max(A)==N: # return next number for sets filled from 1 to N
		return(N+1)
	for i in xrange(0, N-1): # crawl through index for sets
		if A[i+1] - A[i] > 1: # test for increases greater than 1
			return(A[i]+1) # return smallest skipped number

		

print(["Expect 5:"] + [MissingInteger(A1)])
print(["Expect 4:"] + [MissingInteger(A2)])
print(["Expect 1:"] + [MissingInteger(A3)])
print(["Expect 1:"] + [MissingInteger(A4)])

# Score = 100%
