# return the minimal difference that can be acheived by splicing A and subtracting one splice from another

# Assumptions:
## 2 <= N <= 100,000
## -1,000 <= A[i] <= 1,000

def TapeEquilibrium(A):

	# define N and P  as specified in the exercise
	N = len(A)
	P = range(1, N)

	# splice A[0] from A, store their difference in array "Diff"
	sum1 = A[0]
	sum2 = sum(A[1:(N)])
	Diff = [abs(sum1-sum2)]

	# build "Diff" array
	for n in range(1, N):
		sum1 = sum1 + A[n]
		sum2 = sum2 - A[n]
		Diff.append(abs(sum1-sum2))

	# return minimum from Diff array
	return(min(Diff))

# console testing:
print(["TapeEquilibrium([3,1,2,4,3]); expect 1: "]+[TapeEquilibrium(prac)])

# Codility testing:
## https://app.codility.com/programmers/lessons/3-time-complexity/tape_equilibrium/
## performance:
## correctness:

