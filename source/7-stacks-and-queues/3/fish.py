"""N voracious fish are moving along a river. Calculate how many fish are alive."""
from __future__ import print_function
import getopt
import sys
import re
def fish(array_a, array_b):
    """N voracious fish are moving along a river. Calculate how many fish are alive."""
    # define length of arrays
    len_n = len(array_a)
    # begin with a fish_count of zero
    fish_count = 0
    # keep track of fish traveling downstream
    fish_down = []
    len_d = len(fish_down)
    # loop through indices of arrays
    for ndx_i in range(len_n):
        # test whether fish is traveling downstream
        if array_b[ndx_i] == 1:
            # if so, append to fish_down
            fish_down.append(array_a[ndx_i])
            len_d = len(fish_down)
        # if it's traveling upstream,
        else:
            # test whether there are any fish it will meet
            while len_d != 0:
                # if so, test whether it will eat the nearest downstream fish
                if fish_down[-1] < array_a[ndx_i]:
                    # if so, remove downstream fish from downstream list
                    fish_down.pop()
                    len_d = len(fish_down)
                # if the downstream fish will eat the index fish,
                else:
                    break
            else:
                # add index fish to survival count
                fish_count += 1
    # fish_down array have not been 'popped' or counted, so add to fish_count
    fish_count += len_d
    return fish_count
# Bash Testing:
ARGS_A = list(getopt.getopt(sys.argv, "ho:v"))
ARGS_A = ARGS_A[1][1]
ARGS_B = re.split(r"\], * *\[", ARGS_A)[1]
ARGS_A = re.split(r"\], * *\[", ARGS_A)[0]
ARGS_A = re.sub(r"^\[|\]$", "", ARGS_A).split(", ")
ARGS_B = re.sub(r"^\[|\]$", "", ARGS_B).split(", ")
ARGS_A = [int(x) for x in ARGS_A]
ARGS_B = [int(x) for x in ARGS_B]
# ARGS_A = [7947, 21515, 15142, 25406, 4233, 14639, 21604, 4975, 23853, 26088]
# ARGS_B = [1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
RESULT = fish(ARGS_A, ARGS_B)
print(["result: "]+[RESULT])
# Codility Testing:
## https://app.codility.com/demo/results/trainingAHFWU3-BTM/
## trainingXVYYMB-PCH/
## Correctness: 100%
## Performance: 100%
## Difficulty: Painless
