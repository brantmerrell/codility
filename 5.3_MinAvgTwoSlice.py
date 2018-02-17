# Return starting number for minimal slice

# Assumptions:
## 2 <= N <= 100,000
## -10,000 <= A[i] <= 10,000

def MinAvgTwoSlice(A):
	N = len(A) # Define N as defined in exercise

	# let ndx be a candidate index that redefines as necessary through a loop of A:
	ndx = {"i":0, "sum": A[0] +A[1], "length":2, "av.min":float(A[0] +A[1])/2}
	if N==2:
		return(0)
	for n in xrange(1, N-1):
		# track the sum of P:Q to efficiently calculate new averages
		ndx["sum"] += A[n+1]
		# track the length of P:Q to efficiently calculate new averages
		ndx["length"] += 1
		# test to see whether smaller average is possible for pair of list
		if float(ndx["sum"])/ndx["length"] < ndx["av.min"]:
			# set minimal average lower for current index
			ndx["av.min"] = float(ndx["sum"]) / ndx["length"]
		# test whether n acheives a smaller average with 1 consecutive index
		if float(A[n] + A[n+1])/2 < ndx["av.min"]:
			# if so, redefine i, sum, and average
			ndx={"i":n,"sum":A[n]+A[n+1],"length":2,"av.min":float(A[n]+A[n+1])/2}
	return(ndx["i"])
# Console Testing:
print({"MinAvgTwoSlice([4,2,2,5,1,5,8]); expect 1": MinAvgTwoSlice([4,2,2,5,1,5,8])})
print({"MinAvgTwoSlice([8,4]); expect 0": MinAvgTwoSlice([8,4])})

# Codility Testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
## Correctness: 40%
	## "the best slice has length 3"? Got 2 expected 5
	## "the best slice has length 3"? Got 3 expected 2
	## increasing, decreasing, and small functional. Got 0 expected 3

## Performance: 60%
	## Numbers from -1 to 1, N= ~100,000. Got 0, expected 40,002
	## Many sequences, N = 100,000. Got 1 expected 4.
## Difficulty: Respectable
