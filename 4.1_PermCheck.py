# A function for testing whether a list / array is a permutation

# Assumptions:
## 1 <= N <= 100,000
## N is an integer
## 1 <= min(A) 
## max(A) <= 1,000,000,000

def PermCheck(A):
	if not type(A) is list:
		return(0)
	N = len(A)
	if N<max(A):
		return(0)
	else:
		return(int(len(set(A))==N))

	

# Console testing:
print(["PermCheck([1]); Expect 1: "] + [PermCheck([1])]) 
print(["PermCheck([51423]); Expect 0: "] + [PermCheck([51423])])
print(["PermCheck([4,1,3,2]); Expect 1: "]+[PermCheck(A1)])
print(["PermCheck([4,1,3]); Expect 0:"]+[PermCheck(A0)])
print(["PermCheck([4,4,3,2]); Expect 0:"]+[PermCheck([4,4,3,2])])
print(["PermCheck([53,54]); Expect 0:"] + [PermCheck([53,54])])

# Codility Testing:
## https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
## Correctness: 100%
## Performance: 100%
## Difficulty: Painless
