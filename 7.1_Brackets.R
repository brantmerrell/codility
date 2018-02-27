# Determine whether a given string of parentheses is properly nested
# Bash Testing:

Brackets <- function(S){
	# split string into array
	S = unlist(strsplit(S,''))
	# create object to match lefts and rights
	match = c("]"="[","}"="{",")"="(")
	# create stack to track bracket matches
	stack = c()
	# loop through S
	for(i in 1:length(S)){
		# test for leftness (as opposed to rightness)
		if(is.na(match[S[i]])){
			# if left, add to stack
			stack <- c(stack,S[i])
		# if right, make sure stack already has an element
		}else if(length(stack)!=0){
			# remove an element from stack
			POP = stack[length(stack)]
			stack = stack[-length(stack)]
			# removed element should equal S[i]
			if (match[S[i]]!=POP){
				# if not, return zero
				return(0)
			}
		}
	}
	# if length(stack)==0 after loop finishes, the lefts and right 'balance'
	if(length(stack)==0){
		return(1)
	# otherwise, they do not
	}else{
		return(0)
	}
}
# Bash Testing:
args <- commandArgs()[6]
#args <- gsub("^\\[|\\]$","",args)
#args <- as.numeric(unlist(strsplit(args, ",")))
time1 <- unclass(Sys.time())
result <- Brackets(args)
time2 <- unclass(Sys.time())
print(paste("result:", result, "; milliseconds:",(time2-time1)*1000))

# Codility Testing:
## https:#app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
## Correctness: 
## Performance: 
## Difficulty: Painless


