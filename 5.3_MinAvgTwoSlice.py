# Return starting number for minimal slice

# Assumptions:
## 2 <= N <= 100,000
## -10,000 <= A[i] <= 10,000

def MinAvgTwoSlice(A):
	N = len(A) # Define N as defined in exercise
	if N==2:
		return(0)

	# create objects to track minimum slice for lengths of 2 and 3 along array
	ndx2 = {"i":0, "sum": A[0] +A[1], "length":2, "av.min":float(A[0] +A[1])/2}
	ndx3 = {"i":0, "sum": A[0] +A[1] + A[2], "length":3, "av.min":float(A[0] + A[1] + A[3])/3}

	for n in range(0, N):

		# restrict assessment of pairs according to range 1 through N-2
		if (1 <= n) & ((n+1) < N):

			# track the sum and length of P:Q to efficiently calculate new averages
			ndx2["sum"] += A[n+1]
			ndx2["length"] += 1

			# test to see whether smaller average is possible for pair of list
			if float(ndx2["sum"])/ndx2["length"] < ndx2["av.min"]:
				# set minimal average lower for current index
				ndx2["av.min"] = float(ndx2["sum"]) / ndx2["length"]

			# test whether n acheives a smaller average with 1 consecutive index
			if float(A[n] + A[n+1])/2 < ndx2["av.min"]:
				# if so, redefine i, sum, and average
				ndx2={"i":n,"sum":A[n]+A[n+1],"length":2,"av.min":float(A[n]+A[n+1])/2}

		# restrict assessment of 3-slice according to range 1 through N-3
		if (1 <= n) & ((n+2) < N):
			# track the sum and length of P:Q to efficiently calculate new averages
			ndx3["sum"] += A[n+1]
			ndx3["length"] += 1

			# test to see whether smaller average is possible for 3-slice of list
			if float(ndx3["sum"])/ndx3["length"] < ndx3["av.min"]:
				# set minimal average lower for current index
				ndx3["av.min"] = float(ndx3["sum"]) / ndx3["length"]

			# test whether n acheives a smaller average with 1 consecutive index
			if float(A[n] + A[n+1] + A[n+2])/3 < ndx3["av.min"]:
				# if so, redefine i, sum, and average
				ndx3={"i":n,"sum":A[n]+A[n+1]+A[n+2],"length":2,"av.min":float(A[n]+A[n+1]+A[n+2])/3}
	# if 3-slice produces smaller average than 2-slice,
	if ndx3["av.min"]<ndx2["av.min"]:
		# define two-slice index as 3-slice index
		ndx2["i"] = ndx3["i"]

	# return smallest index
	return(ndx2["i"])
# Console Testing:
print({"MinAvgTwoSlice([4,2,2,5,1,5,8]); expect 1": MinAvgTwoSlice([4,2,2,5,1,5,8])})
print({"MinAvgTwoSlice([8,4]); expect 0": MinAvgTwoSlice([8,4])})

# Codility Testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
## Correctness: 100%
## Performance: 100%
## Difficulty: Respectable
