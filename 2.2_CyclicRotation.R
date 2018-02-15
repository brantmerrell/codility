
CyclicRotation <- function(A=list(3,8,9,7,6), K=1){
	# set N as zero
	A <- unlist(A); N = 0
	
	while(N < K){
		A <- c( A[ length(A) ], A[ -length(A) ])
		N <- N + 1
	}
	A
}
