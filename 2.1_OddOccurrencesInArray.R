# returns non-replicated element of numeric array

# assumptions:
## 1 <= A.length <= 1,000,000
## 1 <= A[i] <= 1,000,000,000
## all but 1 integers occur an even number of times


OddOccurrencesInArray <- function(A){

	# unlist the array
	# table() counts recurrence of each value
	A <-table(unlist(A))

	# return non-even values 
	return(as.numeric(names(A[A %% 2 == 1])))
}

# console testing:
print(paste("OddOccurrencesInArray(3); expect 3:",OddOccurrencesInArray(list(3))))
print(paste("OddOccurrencesInArray([9,3,9,3,9,7,9]); expect 7: ",
		OddOccurrencesInArray(list(9,3,9,3,9,7,9))))

# Codility testing: 
## https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
## R language not scored
