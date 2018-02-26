# Return starting number for minimal slice

# Assumptions:
## 2 <= N <= 100,000
## -10,000 <= A[i] <= 10,000

MinAvgTwoSlice <- function(A){
	A <- unlist(A) # Convert list to vector
	N <- length(A) # Define N as defined in exercise

	# define vector to track the minimum average assocated with an index
	# include sum and length of P through Q to increase performance
	i1 <- c(i=1, sum=sum(A[1:2]), length=2, av.min=mean(A[1:2]))

	# define vector to track competing index for minimum-average
	i2 <- i1
	if(N==2){return(1)}
	for(n in seq(2, N-1)){
		# track the sum of P through Q
		i1["sum"] <- sum(i1["sum"], A[n+1])
		
		# track the length of P through Q
		i1["length"] <- i1["length"]+1
		
		# track the sum of P through Q
		i2["sum"] <- sum(i2["sum"], A[n+1])
		
		# track the length of P through Q
		i2["length"] <- i2["length"]+1
		# favor index associated with lower possible average
		# testing for i1["av.min"] < i2["av.min"] would be redundant
		if(i2["av.min"]<i1["av.min"]){
			i1 <- i2
		}

		# track the lowest possible average for i1
		if(i1["sum"]/i1["length"] < i1["av.min"]){
			i1["av.min"] <- i1["sum"] / i1["length"]
		}
		# track the lowest possible average for i2
		if(i2["sum"]/i2["length"]<i2["av.min"]){
			i1["av.min"] <- i1["sum"] / i1["length"]
			i2["av.min"] <- i2["sum"] / i1["length"]
		}

		# if a lower average is provided, redefine i1 and i2 accordingly
		if(mean(A[n+(0:1)])<i1["av.min"]){
			i1 <- c(i=n, sum=sum(A[n+(0:1)]), length = 2, av.min=mean(A[n+(0:1)]))
			i2 <- i1
		}

		# if an equal average is provided, track 2nd index using i2
		if(mean(A[n+(0:1)])==i1["av.min"] && i2["i"]==i1["i"]){
			i2 <- c(i=n, sum=sum(A[n+(0:1)]), length = 2, av.min=mean(A[n+(0:1)]))
		}
	}
	return(as.integer(i1["i"]))
}
# Bash Testing:
args <- commandArgs()[6]
args <- gsub("^\\[|\\]$","",args)
args <- as.numeric(unlist(strsplit(args, ",")))
print(MinAvgTwoSlice(args))
#print(paste("for list(4,2,2,5,1,5,8) expect 2:", MinAvgTwoSlice(list(4,2,2,5,1,5,8))))
#print(paste("for c(8,4) expect 1:", MinAvgTwoSlice(c(8,4))))

# Codility Testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
## R Language not assessed
## Difficulty: Respectable
