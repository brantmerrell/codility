"""Cover "Manhattan skyline" using the minimum number of rectangles."""
import getopt
import sys
import re
def stone_wall(arr_h):
    """Cover "Manhattan skyline" using the minimum number of rectangles."""
    # define N as length of arr_h
    len_n = len(arr_h)
    # start block count at length of arr_h
    blocks = len(arr_h)
    # iterate through arr_h to compare blocks
    for ndx_n in range(len_n):
        # create a lookback variable to crawl backwards from current loop location
        lookback = ndx_n
        # only crawl backwards while height is high enough to share stones
        while (arr_h[ndx_n] <= arr_h[lookback]) & (lookback > 0):
            lookback -= 1
            # if a shared height is reached,
            if arr_h[lookback] == arr_h[ndx_n]:
                # subtract from block count
                blocks -= 1
                # and stop while loop
                lookback = 0
    # return the block count
    return blocks
# Bash Testing:
ARGS = list(getopt.getopt(sys.argv, "ho:v"))[1][1]
ARGS = re.sub(r"^\[|\]$", "", ARGS).split(", ")
ARGS = [int(x) for x in ARGS]
# time1 = datetime.datetime.now()
RESULT = stone_wall(ARGS)
# time2 = datetime.datetime.now()
# timeChange = time2-time1
print ["result: "]+[RESULT] #+[" ; milliseconds: "]+[timeChange.total_seconds()*1000])
# Codility Testing:
## https://app.codility.com/demo/results/trainingQYZX6P-S8W/ ; trainingK59HWD-FN2
## Correctness: 100%
## Performance: 77%
## Difficulty: Painless
