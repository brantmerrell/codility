
# Definitions / Assumptions
## A: zero-indexed array
## M: length of input array
## N: length of counter
## 1 <= N <= 100,000
## 1 <= M <= 100,000
## 1 <= A[i] < N


# Test
A0 <- list(3,4,4,6,1,4,4)
N0 <- 5

MaxCounters <- function(N,A){
	A <- unlist(A)
	M <- length(A)
	Counter <- rep(0,N)
	B <- 0 # 
	C <- 0 # 
	for(i in 1:M){
		if(1 <= A[i] && A[i] <= N){
			if(Counter[A[i]] < B){
				Counter[A[i]] <- B
			}
			Counter[A[i]] <- Counter[A[i]] + 1
			if(C < Counter[A[i]]){
				C <- Counter[A[i]]
			}
		}
		if(A[i]==N+1){
			B <- C
		}
	}
	for(i in 1:N){
		if(Counter[i] < B){
			Counter[i] <- B
		}
	}
	return(Counter)
}

print(paste("expect [3,2,2,4,2]",paste(MaxCounters(N0,A0), collapse = ",")))

