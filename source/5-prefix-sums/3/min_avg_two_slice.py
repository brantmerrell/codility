# Return starting number for minimal slice
# Assumptions:
## 2 <= N <= 100,000
## -10,000 <= A[i] <= 10,000
def MinAvgTwoSlice(A):
	# Define N as defined in exercise
	N = len(A) 
	# set minimal average at the beginning of the array
	av_min=float(A[0]+A[1])/2
	# set corresponding index at the beginning of the array
	index_min=0
	# loop through the array
	for n in range(0, N):
		# restrict 3-element assessment for indices at least 1 element from array's end
		if n+1 < N:
			# create two-element comparison for average slice
			compare = float(A[n]+A[n+1])/2
			# test whether comparison is smaller than current estimate
			if compare < av_min:
				# if so, redefine current estimate as comparison
				av_min = compare
				# and redefine current index as comparison
				index_min=n
		# restrict 3-element assessment for indices at least 2 elements from array's end
		if n+2 <N:
			# create three-element comparison for average slice
			compare = float(A[n]+A[n+1]+A[n+2])/3
			# test whether comparison is smaller than current estimate
			if compare < av_min:
				# if so, redefine current estimate as comparison
				av_min = compare
				# and redefine current index as comparison
				index_min=n
	# return smallest index
	return(index_min)
# Console Testing:
#print({"MinAvgTwoSlice([4,2,2,5,1,5,8]); expect 1": MinAvgTwoSlice([4,2,2,5,1,5,8])})
#print({"MinAvgTwoSlice([8,4]); expect 0": MinAvgTwoSlice([8,4])})
# Bash Testing:
import getopt, sys, re, datetime
args = list(getopt.getopt(sys.argv,"ho:v"))[1][1]
args = re.sub("^\[|\]$","",args).split(",")
args = [int(x) for x in args]
time1 = datetime.datetime.now()
result = MinAvgTwoSlice(args)
time2 = datetime.datetime.now()
timeChange = time2-time1
print(["result: "]+[result]+[" ; milliseconds: "]+[timeChange.total_seconds()*1000])
# Codility Testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
## Correctness: 100%
## Performance: 100%
## Difficulty: Respectable
