# find the minimal nucleotide from a range of sequence DNA 
# Assumptions:
## 1 <= N <= 100,000
## 1 <= M <= 50,000
## 0 <= P <= N-1
## 0 <= Q <= N-1
## P[k] <= Q[k], where 0 <= k < M
## string S consists only of uppercase letters A, C, G, T
GenomicRangeQuery <- function(S,P,Q){
	# add 1 to P and Q because they are zero-index inputs
	P <- P + 1; Q <- Q + 1
	# split S string into vector of characters
	S <- unlist(strsplit(S,""))
	# convert A, C, G, T to 1, 2, 3, 4 respectively
	S[S=="A"] <- 1
	S[S=="C"] <- 2
	S[S=="G"] <- 3
	S[S=="T"] <- 4
	# create result vector of NAs
	res <- rep(NA, length(P))
	# loop to fill result vector 
	for(k in 1:length(res)){
		# minimum of range along S from P to Q
		res[k] <- min(S[P[k]:Q[k]])
	}
	return(res)
}
# console testing:
print(paste("GenomicRangeQuery('CAGCCTA',[2,5,0],[4,5,6]); expect [2,4,1]: ",
	paste(GenomicRangeQuery('CAGCCTA',c(2,5,0),c(4,5,6)),collapse=",")))
# Codility testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
## R Language not assessed
## Difficulty: Respectable
