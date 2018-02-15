prac = [3,1,2,4,3]

def TapeEquilibrium(A):
	N = len(A)
	P = range(1, (N-1))
#	while 1000<len(P):
#		P = P[(len(P)*.25):(len(P)*.75)]
	sum1 = A[0]
	sum2 = sum(A[1:(N)])
	Diff = [abs(sum1-sum2)]
	for n in xrange(1, N):
		sum1 = sum1 + A[n]
		sum2 = sum2 - A[n]
		Diff.append(abs(sum1-sum2))
	return(min(Diff))
	#return(Diff)

print(["prac: [(3,1,2,4,3)]"]+[TapeEquilibrium(prac)])

