"""N voracious fish are moving along a river. Calculate how many fish are alive."""
from __future__ import print_function
import getopt
import sys
import re
def fish(array_a, array_b):
    """N voracious fish are moving along a river. Calculate how many fish are alive."""
    # begin with a fish_count of array lengths
    fish_count = len(array_a)
    # identify lowest index travelling up arrays
    up_max = 0 # begin at zero
    # increase until array_b[up_max] == 1
    while (array_b[up_max] != 1) & (up_max + 1 < len(array_b)):
        up_max += 1
    # identify highest index travelling down arrays
    down_max = len(array_a)-1 # begin at last index
    # decrease until array_b[downmax] == 0
    while (array_b[down_max] != 0) & (down_max >= 0):
        down_max -= 1
    # loop through indices of arrays
    for i, j in enumerate(array_a):
        # travel up the array to identify when direction 1 eats direction 0
        # only adjust up_max upwards when i-fish is direction 1 and larger than up_max
        # if up_max is smaller than up-traveling fish i,
        if (array_b[i] == 1) & (array_a[up_max] < j):
            up_max = i # adjust up_max
        # if up_max is smaller than down-traveling fish, adjust up_max to next up-travelling fish
        if (array_a[up_max] < j) & (array_b[i] == 0):
            while (array_b[up_max] != 1) & (up_max <= len(array_b)):
                up_max += 1
        # only subtract if up_max is downstream of indexFish
        # only subtract if indexFish travels down
        # only subtract if the indexFish is smaller than up_max
        if (up_max < i) & (array_b[i] == 0) & (j < array_a[up_max]):
            fish_count -= 1
        # travel down the array to identify when direction 0 eats direction 1
        # if index direction is 0 and down_max is smaller than index size,
        if (array_b[i] == 0) & (array_a[down_max] < j):
            # set new down_max
            down_max = i
        # if down_max is smaller than i-fish and i-fish is traveling direction 1, it gets eaten
        # the subtraction is handled in the other direction, but new down_max needs to be defined
        if (array_a[down_max] < j) & (array_b[i] == 1):
            while array_b[down_max] != 0 & 0 <= down_max:
                down_max -= 1
        # if down_max is upStream of indexFish, indexFish travels up,
        # and index fish is smaller than down_max,
        if (i < down_max) & (array_b[i] == 1) & (j < array_a[down_max]):
            # indexFish gets eaten
            fish_count -= 1
        # print({"program":"python", "index":i, "size":j,
        #        "direction":array_b[i], "count":fish_count})
    return fish_count
# Bash Testing:
ARGS_A = list(getopt.getopt(sys.argv, "ho:v"))
ARGS_A = ARGS_A[1][1]
ARGS_B = re.split(r"\],*\[", ARGS_A)[1]
ARGS_A = re.split(r"\],*\[", ARGS_A)[0]
ARGS_A = re.sub(r"^\[|\]$", "", ARGS_A).split(",")
ARGS_B = re.sub(r"^\[|\]$", "", ARGS_B).split(",")
ARGS_A = [int(x) for x in ARGS_A]
ARGS_B = [int(x) for x in ARGS_B]
RESULT = fish(ARGS_A, ARGS_B)
print(["result: "]+[RESULT])
# Codility Testing:
## https://app.codility.com/demo/results/trainingXVYYMB-PCH/
## Correctness: 50%
## Performance: 50%
## Difficulty: Painless
