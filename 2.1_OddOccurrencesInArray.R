
# see also https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
A <- list(9, 3, 9, 3, 9, 7, 9, 7, 7)
#names(A) <- as.character(0:length(A))

OddOccurrencesInArray <- function(A){
	A <-table(unlist(A))
	return(as.numeric(names(A[A %% 2 == 1])))
}
print(OddOccurrencesInArray(A))
