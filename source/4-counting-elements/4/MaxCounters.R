# 
# Definitions / Assumptions
## A: zero-indexed array
## M: length of input array
## N: length of counter
## 1 <= N <= 100,000
## 1 <= M <= 100,000
## 1 <= A[i] < N
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
# Console Testing:
print(paste("MaxCounters(5,list(3,4,4,6,1,4,4)): expect [3,2,2,4,2]",paste(MaxCounters(5,list(3,4,4,6,1,4,4)), collapse = ",")))
# Codility Testing:
## https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
## R Language not assessed
## Difficulty: Respectable
