prac <- list(3,1,2,4,3)
#names(prac) <- 0:4

TapeEquilibrium <- function(A){
	N <- length(A)
	A <- unlist(A)
	P <- 1:(length(A)-1)
	sum1 <- A[1]
	sum2 <- sum(A[2:length(A)])
	Diff <- abs(sum1-sum2)
	for(n in 2:N){
		sum1 <- sum1 + A[n]
		sum2 <- sum2 - A[n]
		Diff <- c(Diff, abs(sum1-sum2))
	}
	return(min(Diff))
}

print(c("prac: list(3,1,2,4,3)", TapeEquilibrium(prac)))
