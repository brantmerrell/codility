# N voracious fish are moving along a river. Calculate how many fish are alive.
# Fish <- function(A,B){
# }
# Bash Testing:
args <- commandArgs()[6]
args <- gsub("^\\[|\\]$","",args)
args <- as.numeric(unlist(strsplit(args, ",")))
print(args)
# time1 <- unclass(Sys.time())
# result <- Fish(args)
# time2 <- unclass(Sys.time())
print(paste("result:", result))#, "; milliseconds:",(time2-time1)*1000))
# Codility Testing:
## https://app.codility.com/programmers/
## R Language not assessed 
## Difficulty: Painless
