# compute number of distinct values in an array
# Assumptions:
## 0 <= N <= 100,000
## -1,000,000 <= A[i] <= 1,000,000
def Distinct(A):
	A = set(A)
	return(len(A))
# Console Testing
print(["Distinct([2,1,1,2,3,1]); expect 3: "]+[Distinct([2,1,1,2,3,1])])
# Codility Testing
## https://app.codility.com/programmers/lessons/6-sorting/distinct/
## performance: 100%
## correctness: 100%
## Difficulty: Painless
