# FrogJmp: count minimal number of jumps from X to Y

# Practice examples:
X <- 10 # initial position of frog along straight axis
Y <- 85 # destination position of frog along straight axis
D <- 30 # length frog can jump
# expect answer (85-10)/30 rounded up to 3 jumps

# Assumptions:
## Y <= X
## 1 <= X, Y, & D <= 1,000,000,000
## X, Y, & D are integers

FrogJmp <- function(X, Y, D){
	dist_ <- Y - X 
	jump_ <- dist_ / D # R converts integer to numeric when needed
	return(as.integer(ceiling(jump_))) # must return up-rounded integer
}

print(paste("practice example: X=10, Y=85, D=30. Expect 3:", FrogJmp(X,Y,D), sep="        "))

print(paste("large text: X = 10000, Y=85000, D=30000. Expect 3:",FrogJmp(10000,85000,30000), sep="        "))

print(paste("suppose Y=X? X=85, Y=85, D=30. Expect 0:",FrogJmp(85,85,30), sep="        ")) # expect 0

print(paste("suppose (Y-X)<D? X=6, Y=8, D=3. Expect 1:",FrogJmp(6,8,3), sep="        "))

