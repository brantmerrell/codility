# A function returning the squares a checker-queen can move from a given coordinate on a given board.

# setup for testing:
source("Manganum.R")

M <- Manganum(X1,Y1,T1)$board

hop <- function(X, Y, M, xdir=-1){
	dst <- 1
	while(M[X+(dst*xdir),Y+dst]=="" && dst <= abs(nrow(M) - Y)){
		dst <- dst + 1
	}
	if(M[X-(dst+1)*xdir, Y+dst+1]==""){
		pts <- ifelse(grepl("Q", M[X+(dst*xdir), Y + dst], ignore.case=T), 10, 1)
		dst <- dst + 1
		DF <- data.frame(X=X+(dst*xdir),
			Y = Y + dst)
		while(M[X+(dst*xdir), Y+dst]=="" && dst <= abs(nrow(M)-Y)){
			dst <- dst + 1
			DF <- rbind(DF,
				data.frame(X=X+(dst*xdir), Y = Y + dst)
		}
		DF[,"Points"] <- pts
	}else{} # Figure this out later
	pointsL <- ifelse(grepl("Q", M[X-Left1,Y+Left1], ignore.case=T), 10, 1)
	pointsR <- ifelse(grepl("Q", M[X+Right1, Y+Right1], ignore.case=T), 10, 1)

}
