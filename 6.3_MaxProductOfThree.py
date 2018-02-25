# maximize A[P]*A[Q]*A[R] for any triplet (P,Q,R)
# Assumptions:
## 3 <= N <= 100,000
## -1,000 <= A[i] <= 1,000
def MaxProductOfThree(A) :
    # sort array
    A = sorted(A)
    # determine whether the product of the two smallest is greater than their positive competitors
    if (A[len(A)-2]*A[len(A)-3]) < (A[0]*A[1]) and (0<A[len(A)-1]):
	# if so, multiply two smallest by the largest
	return (A[0] * A[1] * A[len(A)-1])
    else:
        # if not, multiply the three largest numbers
	return (A[len(A) - 1] * A[len(A) - 2] * A[len(A) - 3])
    

# Console Testing
print(["MaxProductOfThree([-3,1,2,-2,5,6]); expect 60: "] + [MaxProductOfThree([-3, 1, 2, -2, 5, 6])]);
print(["MaxProductOfThree([-10,-2,-5,5,5,5]); expect 250: "] + [MaxProductOfThree([-10,-2,-5,5,5,5])]);
print(["MaxProductOfThree([-5,-6,-4,-7,-10]); expect -120: "] + [MaxProductOfThree([-5, -6, -4, -7, -10])]);
# Codility Testing
## https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
## performance: 100%
## correctness: 100%
## Difficulty: Painless
