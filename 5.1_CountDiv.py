# compute number of integers divisible by K in range [A...B]

# Assumptions:
## 0 <= A < = 2,000,000,000
## 0 <= B < = 2,000,000,000
## 1 <= K < = 2,000,000,000
## A <= B

def CountDiv(A,B,K):
	# redefine A as lowest in-range number divisible by K
	while A % K !=0: 
		A += 1

	# redefine B as highest in-range number divisible by K
	while B % K !=0:
		B -= 1

	# if A and B are in range (A is still smaller than B),
	if A < B:
		# then their difference is divisible by K,
		# and (B-A)/K provides the "leaps" from A to B.
		# Thus, adding 1 to include A provides the result.
		return(round((B-A)/K)+1) # round to avoid class 'float'

	# if A==B, they correspond to the only in-range number which divides by K.
	if A == B:
		# Thus, only one in-range number divides by K.
		return(1)
	
	# if redefining A and B caused B < A, then no in-range number divides by K.
	if B < A: 
		return(0)

# Console Testing
print(["CountDiv(6,11,2); expect 3: "]+[CountDiv(6,11,2)])
print(["CountDiv(0,0,1); expect 1: "]+[CountDiv(0,0,1)])

# Codility Testing
## https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
## performance: 100%
## correctness: 100%

## Difficulty: Painless
