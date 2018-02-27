# returns maximum binary gap of integer
## binary gap: adjacent zeros in a binary number (excluding trailing zeros)
## maximum binary gap: maximum character count of binary gap
# Assumptions:
## 1 <= N <= 1,147,483,647
binary_gap <- function(N){
	gp <- gsub("^0+|0+$","", paste(as.integer(rev(intToBits(N))), collapse=""))
	gp <- unlist(strsplit(gp, "1"))
	max(nchar(gp))
}
# console testing:
print(paste("binary_gap(9); expect 2: ",binary_gap(9)))
print(paste("binary_gap(529); expect 4: ",binary_gap(529)))
print(paste("binary_gap(20); expect 1: ",binary_gap(20)))
print(paste("binary_gap(15); expect 0: ",binary_gap(15)))
# codility testing: not available for R language
## https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
## Difficulty: Painless
