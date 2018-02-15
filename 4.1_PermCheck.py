# A function for testing whether a list / array is a permutation

# Assumptions:
## 1 <= N <= 100,000
## N is an integer
## 1 <= min(A) 
## max(A) <= 1,000,000,000


# Example:
A1 = [4,1,3,2] # is permutation
A0 = [4,1,3] # is not permutation

def PermCheck(A):
	if not type(A) is list:
		return(0)
	N = len(A)
	if N<max(A):
		return(0)
	else:
		return(int(len(set(A))==N))

	

# testing
print(["Is a list of integer 1 ([1]) a permutation? Expect 1:"] + [PermCheck([1])]) 
print(["Is a list of 1 integer ([51423]) a permutation? Expect 0:"] + [PermCheck([51423])])
print(["Is a large integer (1000000000) a permutation? expect 0:"] + [PermCheck(1000000000)]) 
print(["Is [4,1,3,2] a permutation? Expect 1:"]+[PermCheck(A1)])
print(["Is [4,1,3] a permutation? Expect 0:"]+[PermCheck(A0)])
print(["repeat values: is [4,4,3,2] a permutation? Expect 0:"]+[PermCheck([4,4,3,2])])
print(["Are two consecutive numbers [53,54] a permutation? Expect 0:"] + [PermCheck([53,54])])

# Codility score: 100% ((Correctness+Performance)/2) (2nd attempt)
# First attempt failed to note that a permutation must begin with the integer 1
