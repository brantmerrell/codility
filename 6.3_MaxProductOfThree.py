# maximize A[P]*A[Q]*A[R] for any triplet (P,Q,R)
# Assumptions:
## 3 <= N <= 100,000
## -1,000 <= A[i] <= 1,000
def MaxProductOfThree(A) :
    # sort array
    A = sorted(A)
    # multiply three largest numbers in array
    return (A[len(A) - 1] * A[len(A) - 2] * A[len(A) - 3])

# Console Testing
print(["MaxProductOfThree([-3,1,2,-2,5,6]); expect 60: "] + [MaxProductOfThree([-3, 1, 2, -2, 5, 6])]);
# Codility Testing
## https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
## performance: 
## correctness: 
## Difficulty: Painless
