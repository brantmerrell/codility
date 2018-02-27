"""N voracious fish are moving along a river. Calculate how many fish are alive."""
from __future__ import print_function
import getopt
import sys
import re
def fish(array_a, array_b):
    """N voracious fish are moving along a river. Calculate how many fish are alive."""
    return([array_a]+[array_b])
# Bash Testing:
ARGS_A = list(getopt.getopt(sys.argv, "ho:v"))[1][1]
ARGS_B = ARGS_A.split("],[")[1]
ARGS_A = ARGS_A.split("],[")[0]
ARGS_A = re.sub(r"^\[|\]$", "", ARGS_A).split(",")
print((ARGS_A))
ARGS_A = [int(x) for x in ARGS_A]
ARGS_B = [int(x) for x in ARGS_B]
__result__ = fish(ARGS_A, ARGS_B)
print(["result: "]+[__result__])
# Codility Testing:
## https://app.codility.com/demo/results/trainingQYZX6P-S8W/ ; trainingK59HWD-FN2
## Correctness: 
## Performance: 
## Difficulty: Painless
