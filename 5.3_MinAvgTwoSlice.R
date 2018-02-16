# Return starting number for minimal slice

MinAvgTwoSlice <- function(A){
	A <- unlist(A) # Convert list to vector
	N <- length(A) # Define N as defined in exercise

	# define vector to track the minimum average assocated with an index
	# include sum and length of P through Q to increase performance
	i1 <- c(i=1, sum=sum(A[1:2]), length=2, av.min=mean(A[1:2]))

	# define vector to track competing index for minimum-average
	i2 <- i1
	print(rbind(i1,i2))
	if(N==2){return(1)}
	for(n in seq(2, N-1)){
		print(n)
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
			print(paste("i2[\"av.min\"] (",i2["av.min"],") < i1[\"av.min\"] (", i1["av.min"],") thus i1<-i2"))
			i1 <- i2
		}

		# track the lowest possible average for i1
		if(i1["sum"]/i1["length"] < i1["av.min"]){
			print(paste("i1[\"sum\"]/i1[\"length\"]<i1[\"av.min\"] thus i1[\"av.min\"]=",i1["sum"]/i1["length"]))
			i1["av.min"] <- i1["sum"] / i1["length"]
		}
		# track the lowest possible average for i2
		if(i2["sum"]/i2["length"]<i2["av.min"]){
			print(paste("i12\"sum\"]/i2[\"length\"]<i2[\"av.min\"] thus i2[\"av.min\"]=",i2["sum"]/i2["length"]))
			i1["av.min"] <- i1["sum"] / i1["length"]
			i2["av.min"] <- i2["sum"] / i1["length"]
		}

		# if a lower average is provided, redefine i1 and i2 accordingly
		if(mean(A[n+(0:1)])<i1["av.min"]){
			i1 <- c(i=n, sum=sum(A[n+(0:1)]), length = 2, av.min=mean(A[n+(0:1)]))
			i2 <- i1
			print(paste("mean(A[n+(0:1)])<i1[\"av.min\"] thus i1 & i2 <- ",paste(i1,collapse=" ")))
		}

		# if an equal average is provided, track 2nd index using i2
		if(mean(A[n+(0:1)])==i1["av.min"] && i2["i"]==i1["i"]){
			i2 <- c(i=n, sum=sum(A[n+(0:1)]), length = 2, av.min=mean(A[n+(0:1)]))
			print(paste("mean(A[n+(0:1)])==i1[\"av.min\"] thus i2 <- ",paste(i2,collapse=" ")))
		}
	}
	return(as.integer(i1["i"]))
}
# Console Testing:
print(paste("for list(4,2,2,5,1,5,8) expect 2:", MinAvgTwoSlice(list(4,2,2,5,1,5,8))))
print(paste("for c(8,4) expect 1:", MinAvgTwoSlice(c(8,4))))

# Codility Testing:
## https://app.codility.com/programmers/lessons/
## Correctness: 40%
	## "the best slice has length 3"? Got 2 expected 5
	## "the best slice has length 3"? Got 3 expected 2
	## increasing, decreasing, and small functional. Got 0 expected 3

## Performance: 60%
	## Numbers from -1 to 1, N= ~100,000. Got 0, expected 40,002
	## Many sequences, N = 100,000. Got 1 expected 4.
