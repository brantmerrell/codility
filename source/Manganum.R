# Given positions of all opposing checkers and your checker-queen, return the maximum number of points you can capture (checker=1, queen=10)

# Captures provide queen with repeat-capture opportunity

# Definitions Given
## X: array/list of x-coordinates
## Y: array/list of y-coordinates
## T: string of piece values
	## p = opposing pawn
	## q = opposing queen
	## X = capturing queen
## k: position corresponding to X, Y, and T for a piece

# Assumptions Given:
## X, Y, and T have the same length N
## 1 <= N <= 100,000,000
## No two pieces have the same coordinates
## Each piece is located on a black field (0,0 is black)
## each character in T is either p, q, or X
## X occurs only once in string T

# Assumptions gleaned:
## Tests with multiple q's will occur
## Tests in which X jumps into negative integers will occur
## X[k] + Y[K] will always be even
## Queen can only travel upwards (left and right)
## Queen can only travel directly towards and over pawn

# Example  Test 1:
X1 <- list(3,5,1,6)
Y1 <- list(1,3,3,8)
T1 <- "Xpqp"
Exp1 <- 10


# Example Test 2: 
X2 <- list(0,3,5,1,6)
Y2 <- list(4,1,3,3,8)
T2 <- "pXpqp"
Exp2 <- 2

# Example Test 3
X3 <- list(0,6,2,5,3,0)
Y3 <- list(4,8,2,3,1,6)
T3 <- "ppqpXp"
Exp3 <- 12

Manganum <- function(X,Y,T_){
	# Remove X and Y from list form
	X <- unlist(X); Y <- unlist(Y)

	# Define N and K as defined in challenge
	N <- length(X); k <- 1:N

	# split T_ string into elements
	T_ <- unlist(strsplit(toupper(T_),""))

	# define domain
	dom <- (X[T_=="X"]-(max(Y)-min(Y))):(X[T_=="X"]+(max(Y)-min(Y)))

	# Build matrix of checkerboard
	M <- matrix("",	nrow = max(Y)-min(Y)+1,
			ncol = length(dom), 
			dimnames = list(max(Y):min(Y), dom))

	# Place pieces on checkerboard
	for(n in k){
		M[as.character(Y[n]),as.character(X[n])] <- T_[n]
	}

	DF <- data.frame(X=X, Y=Y, T=T_, pts=NA)

	DF[DF$T=="p","pts"] <- 1
	DF[DF$T=="q","pts"] <- 10

	# Make sure pieces are placed correctly
	return(list(board=M,pieces=DF))
}

# Test 1:
print(list("expect:"=Exp1, Manganum(X1,Y1,T1)))

#print(paste("Capturer at (3,1), Monarch at (1,3), checkers at [(0,4),(5,3),(6,8)]. Expect 2:", 
#		paste(Manganum(c(0,3,5,1,6),c(4,1,3,3,8),"pXpqp"), collapse=";"), sep="    "))

#print(paste("Capturer: (3,1); Monarch: (2,2), checkers: [(0,4),(6,8),(5,3),(0,6)]. Expect 12:", 
#		paste(Manganum(c(0,6,2,5,3,0),c(4,8,2,3,1,6),"ppqpXp"),collapse=";"),sep="    "))



