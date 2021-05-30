# rotate array A, k times
# Assumptions:
## 1 <= N <= 100
## 1 <= K <= 100
## -1,000 <= A[i] <= 1,000
def CyclicRotation(A, K):
    if len(A)==0 or K == len(A) or K == 0:
        return A
    while K > len(A):
        K = K - len(A)
    M = len(A) - K
    return A[M:] + A[:M]

# console testing
print("CyclicRotation([3,8,9,7,6], 3); expect [9,7,6,3,8]: "+CyclicRotation([3,8,9,7,6], 3))
print("CyclicRotation([1,2,3,4], 4); expect [1,2,3,4]: "+CyclicRotation([1,2,3,4], 4))
# codility testing:
## https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
## note: function must be renamed to "solution" for testing
## performance: not assessed
## correctness: 100%
## Difficulty: Painless
