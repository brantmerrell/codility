# N voracious fish are moving along a river. Calculate how many fish are alive.
Fish <- function(A,B){
    return(c(A=A,B=B))
}
# Bash Testing:
ARGS_A <- commandArgs()[6]
ARGS_B <- strsplit(ARGS_A,"\\],\\[")[[1]][2]
ARGS_A <- strsplit(ARGS_A,"\\],\\[")[[1]][1]
ARGS_A <- gsub("^\\[|\\]$","",ARGS_A)
ARGS_B <- gsub("^\\[|\\]$","",ARGS_B)
ARGS_A <- as.numeric(unlist(strsplit(ARGS_A, ",")))
ARGS_B <- as.numeric(unlist(strsplit(ARGS_B, ",")))
RESULT <- Fish(ARGS_A,ARGS_B)
print(paste("result:", paste(RESULT,collapse=" ")))
# Codility Testing:
## R Language not assessed 
## Difficulty: Painless
