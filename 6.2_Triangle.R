# determine whether a triangle can be built from a given set of edges

# Assumptions:
## 0 <= N <= 100,000
## -2,147,483,648 <= A[i] <= 2,147,483,647

Triangle <- function(A){
	# sort array
	A = sort(A)
	# loop through array from 1 to length-3 (code calls i+2)
	for(i in seq(1,length(A)-2))
		# test each triplet for triangularity
		if(A[i+2] < (A[i]+A[i+1])) return(1)
	return(0)
	
}

# Console Testing
print(paste("Triangle(c(10,2,5,1,8,20)); expect 1: ",Triangle(c(10,2,5,1,8,20))))
print(paste("Triangle(c(10,50,5,1)); expect 0: ",Triangle(c(10,50,5,1))))

# Codility Testing
## https://app.codility.com/programmers/lessons/6-sorting/triangle/
## performance: 
## correctness: 
## Difficulty: Painless
