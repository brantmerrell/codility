# builds array of length N based on inputs from array A
## adds 1 to newArray[A[k]] when 1<= A[k] <= N
## sets all newArray values to max(newArray) when A[k] = N+1
# Definitions / Assumptions
## A: zero-indexed array
## M: length of input array
## N: length of newArray
## 1 <= N <= 100,000
## 1 <= M <= 100,000
## 1 <= A[i] < N
def MaxCounters(N,A):
	M = len(A)
	newArray = [0]*N
	B = 0 # define variable to track 
	C = 0 # define variable to track
	for i in range(0,M):
		if 1 <= A[i] <= N:
			if newArray[A[i]-1] < B:
				newArray[A[i]-1] = B
			newArray[A[i]-1] += 1
			if C < newArray[A[i]-1]:
				C = newArray[A[i]-1]
		if A[i]==N+1:
			B = C
	for i in range(0, N):
		if newArray[i] < B:
			newArray[i] = B
	return(newArray)
# console testing:
print(["MaxCounters(5,[3,4,4,6,1,4,4]); expect [3,2,2,4,2]"]+[MaxCounters(5,[3,4,4,6,1,4,4])])
# codility testing:
## https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
## Correctness = 100%
## Performance = 100%
## Difficulty: Respectable
