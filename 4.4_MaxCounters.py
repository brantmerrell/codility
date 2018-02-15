
# Definitions / Assumptions
## A: zero-indexed array
## M: length of input array
## N: length of counter
## 1 <= N <= 100,000
## 1 <= M <= 100,000
## 1 <= A[i] < N


# Test
A0 = [3,4,4,6,1,4,4]
N0 = 5

def MaxCounters(N,A):
	M = len(A)
	Counter = [0]*N
	B = 0 # define variable to track 
	C = 0 # define variable to track
	for i in range(0,M):
		if 1 <= A[i] <= N:
			if Counter[A[i]-1] < B:
				Counter[A[i]-1] = B
			Counter[A[i]-1] += 1
			if C < Counter[A[i]-1]:
				C = Counter[A[i]-1]
		if A[i]==N+1:
			B = C
	for i in range(0, N):
		if Counter[i] < B:
			Counter[i] = B
	return(Counter)

print(["expect [3,2,2,4,2]"]+[MaxCounters(N0,A0)])

# Correctness = 100%
# Performance = 40%
## 2120 max_counter operations - timeout
## 10,000 max_counter operations - timeout
## all max_counter operations - timeout (N=100,000 & M=100,000?)
