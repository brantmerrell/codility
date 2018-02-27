# Cover "Manhattan skyline" using the minimum number of rectangles. 
def StoneWall(H):
    # start block count at length of H
    blocks = len(H)
    # iterate through H to compare blocks
    for n in range(len(H)):
        # create a lookback variable to crawl backwards from current loop location
        lookback = n
        # only crawl backwards while height is high enough to share stones
        while((H[n]<=H[lookback]) & (0<lookback)):
            lookback-=1
            # if a shared height is reached, 
            if(H[lookback]==H[n]):
                # subtract from block count
                blocks -= 1
                # and stop while loop
                lookback = 0
    # return the block count
    return(blocks)
# Bash Testing:
import getopt, sys, re, datetime
args = list(getopt.getopt(sys.argv,"ho:v"))[1][1]
args = re.sub("^\[|\]$","",args).split(",")
args = [int(x) for x in args]
# time1 = datetime.datetime.now()
result = StoneWall(args)
# time2 = datetime.datetime.now()
# timeChange = time2-time1
print(["result: "]+[result])#+[" ; milliseconds: "]+[timeChange.total_seconds()*1000])
# Codility Testing:
## https://app.codility.com/demo/results/trainingQYZX6P-S8W/ ; trainingK59HWD-FN2
## Correctness: 100%
## Performance: 77%
## Difficulty: Painless
