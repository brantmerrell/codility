# FrogJmp: count minimal number of jumps from X to Y

# Assumptions:
## Y <= X
## 1 <= X, Y, & D <= 1,000,000,000
## X, Y, & D are integers

def FrogJmp(X, Y, D):

	# float not essential: assumptions include integers
	dist_ = Y - X 

	# float now essential (must round up while default is down)
	jump_ = float(dist_) / D 

	# round up requires function 'ceil'
	from math import ceil 

	# return up-rounded integer
	return(int(ceil(jump_))) 

# console testing:
## expect answer (85-10)/30 rounded up to 3 jumps
print(["practice example: X=10, Y=85, D=30. Expect 3:"]+[FrogJmp(10,85,30)]) 
print(["large text: X = 10000, Y=85000, D=30000. Expect 3:"]+[FrogJmp(10000,85000,30000)])
print(["suppose Y=X? X=85, Y=85, D=30. Expect 0:"]+[FrogJmp(85,85,30)]) 
print(["suppose (Y-X)<D? X=6, Y=8, D=3. Expect 1:"]+[FrogJmp(6,8,3)])

# Codility testing: 
## https://app.codility.com/programmers/lessons/3-time-complexity/frog_jmp/
## performance: 100%
## correctness: 100%
