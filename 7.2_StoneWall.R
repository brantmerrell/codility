# Cover "Manhattan skyline" using the minimum number of rectangles. 

StoneWall <- function(H){
    # define N as length of H
    N <- length(H)
    # start block count at 1
    blocks <-length(H)
    # iterate through H to compare blocks
    for(n in 1:N){
        # create a lookback variable to crawl backwards from current loop location
        lookback <- n
        # only crawl backwards while height is high enough to share stones
        while((H[n]<=H[lookback]) & (1<lookback)){
            lookback<-lookback-1
            # if a shared height is reached, 
            if(H[lookback]==H[n]){
                # subtract from block count
                blocks <-blocks - 1
                # and stop while loop
                lookback = 1
            }
        }

    }
    # return the block count
    return(blocks)
}
# Bash Testing:
args <- commandArgs()[6]
args <- gsub("^\\[|\\]$","",args)
args <- as.numeric(unlist(strsplit(args, ",")))
# time1 <- unclass(Sys.time())
result <- StoneWall(args)
# time2 <- unclass(Sys.time())
print(paste("result:", result))#, "; milliseconds:",(time2-time1)*1000))

# Codility Testing:
## https://app.codility.com/programmers/
## R Language not assessed 
## Difficulty: Painless


