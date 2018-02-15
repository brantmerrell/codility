# 

binary_gap <- function(N){
	gp <- gsub("^0+|0+$","", paste(as.integer(rev(intToBits(N))), collapse=""))
	gp <- unlist(strsplit(gp, "1"))
	max(nchar(gp))
}
