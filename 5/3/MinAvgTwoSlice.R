# Return starting number for minimal slice
# Assumptions:
## 2 <= N <= 100,000
## -10,000 <= A[i] <= 10,000
MinAvgTwoSlice <- function(A){
	# define N as defined in exercise
	N = length(A)
	# set minimal average at the beginning of the array
	av_min=mean(A[c(1:2)])
	# define a compare iable (as anything, really)
	compare = av_min
	# set corresponding index at the beginning of the array
	index_min=1
	# loop through the array
	for(n in 1:N){
		# restrict 3-element assessment for indices at least 1 element from array's end
		if(n+1 < N){
			# create two-element comparison for average slice
			compare = mean(A[n+(0:1)])
			# test whether comparison is smaller than current estimate
			if(compare < av_min){
				# if so, redefine current estimate as comparison
				av_min = compare
				# and redefine current index as comparison
				index_min=n
			}
		# restrict 3-element assessment for indices at least 2 elements from array's end
		}
		if(n+2 < N){
			# create three-element comparison for average slice
			compare = mean(A[n+(0:2)])
			# test whether comparison is smaller than current estimate
			if(compare < av_min){
				# if so, redefine current estimate as comparison
				av_min = compare
				# and redefine current index as comparison
				index_min=n
			}
		}
	}
	# return smallest index (subtract 1 to provide zero-index results)
	return(index_min-1)
}
# Bash Testing:
args <- commandArgs()[6]
args <- gsub("^\\[|\\]$","",args)
args <- as.numeric(unlist(strsplit(args, ",")))
time1 <- unclass(Sys.time())
result <- MinAvgTwoSlice(args)
time2 <- unclass(Sys.time())
print(paste("result:", result, "; milliseconds:",(time2-time1)*1000))
#print(paste("for list(4,2,2,5,1,5,8) expect 2:", MinAvgTwoSlice(list(4,2,2,5,1,5,8))))
#print(paste("for c(8,4) expect 1:", MinAvgTwoSlice(c(8,4))))
# Codility Testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
## R Language not assessed
## Difficulty: Respectable
