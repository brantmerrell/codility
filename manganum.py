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

X = [3,5,1,6]
Y = [1,3,3,8]
T = "Xpqp"

def Manganum(X,Y,T):
	N = len(X)
	k = [""]*N
	T = list(T)
	for n in range(0,N):
		k[n] = T[n] + "," + str(X[n]) + ","+ str(Y[n])
	return(k)

# Test 1:
print(["Capturer at (3,1), Monarch at (1,3), checkers at [(5,3),(6,8)]. Expect 10:"]+[Manganum([3,5,1,6],[1,3,3,8],"Xpqp")])

print(["Capturer at (3,1), Monarch at (1,3), checkers at [(0,4),(5,3),(6,8)]. Expect 2:"]+[Manganum([0,3,5,1,6],[4,1,3,3,8],"pXpqp")])

print(["Capturer at (3,1), Monarch at (2,2), checkers at [(0,4),(6,8),(5,3),(0,6)]. Expect 12:"]+[Manganum([0,6,2,5,3,0],[4,8,2,3,1,6],"ppqpXp")])
