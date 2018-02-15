# FrogJmp: count minimal number of jumps from X to Y

# Practice examples:
X = 10 # initial position of frog along straight axis
Y = 85 # destination position of frog along straight axis
D = 30 # length frog can jump
# expect answer (85-10)/30 rounded up to 3 jumps

# Assumptions:
## Y <= X
## 1 <= X, Y, & D <= 1,000,000,000
## X, Y, & D are integers

def FrogJmp(X, Y, D):
	dist_ = Y - X # float not essential: assumptions include integers
	jump_ = float(dist_) / D # float now essential: must round up, never down
	from math import ceil # round up requires function 'ceil'
	return(int(ceil(jump_))) # must return up-rounded integer


print(["practice example: X=10, Y=85, D=30. Expect 3:"]+[FrogJmp(X,Y,D)]) # can only concatenate list (not int) to list

print(["large text: X = 10000, Y=85000, D=30000. Expect 3:"]+[FrogJmp(10000,85000,30000)])

print(["suppose Y=X? X=85, Y=85, D=30. Expect 0:"]+[FrogJmp(85,85,30)]) # expect 0

print(["suppose (Y-X)<D? X=6, Y=8, D=3. Expect 1:"]+[FrogJmp(6,8,3)])

# Codility score: 100% (=(Correctness+Performance)/2)
