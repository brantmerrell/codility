# maximize A[P]*A[Q]*A[R] for any triplet (P,Q,R)
# Assumptions:
## 3 <= N <= 100,000
## -1,000 <= A[i] <= 1,000
MaxProductOfThree <- function(A){
    # sort array
    A = sort(A)
    # determine whether the product of the two smallest is greater than their positive competitors
    if ((A[length(A)-1]*A[length(A)-2]) < (A[1]*A[2])){
	# if so, multiply two smallest by the largest
	return (prod(A[c(1,2,length(A))]))
    }else{
        # if not, multiply the three largest numbers
	return (prod(A[length(A)-(0:2)]))
    }
}

# Console Testing
print(paste("MaxProductOfThree(c(-3,1,2,-2,5,6)); expect 60: ",MaxProductOfThree(c(-3, 1, 2, -2, 5, 6))));
print(paste("MaxProductOfThree(c(-10,-2,-5,5,5,5)); expect 250: ",MaxProductOfThree(c(-10,-2,-5,5,5,5))));
# Codility Testing
## https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
## R language not assessed
## Difficulty: Painless
