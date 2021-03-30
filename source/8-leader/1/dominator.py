"""Find an index of an array corresponding to its dominator value"""
from __future__ import print_function
import getopt
import sys
import re
import collections
import random
def dominator(arr_a):
    """Find an index of an array corresponding to its dominator value"""
    len_n = len(arr_a)
    if len_n == 0:
        return -1
    # count the recurrences of each element in array
    counts = collections.Counter(arr_a).items()
    # obtain the highest number of recurrences in array
    max_count = max([m[1] for m in counts])
    # test whether value comprises at least half of array
    if max_count * 2 <= len(arr_a):
        # if not, return -1
        return -1
    # obtain the dominator value
    dom_val = [m[0] for m in counts if m[1] == max_count][0]
    # obtain indices associated with dominator value
    dom_ndx = [m for m in range(len(arr_a)) if arr_a[m] == dom_val]
    # return a random dominator index
    return dom_ndx[int(random.random()*len(dom_ndx))]
# Debugging:
ARR_A = [3, 4, 3, 2, 3, -1, 3, 3]
dominator(ARR_A)
# Bash Testing
ARR_A = list(getopt.getopt(sys.argv, "ho:v"))[1][1] # store string passed from command line
ARR_A = re.sub(r"^\[|\]$", "", ARR_A) # remove brackets from string
ARR_A = ARR_A.split(r",") # split string by comma into list
ARR_A = [int(x) for x in ARR_A] # convert list to class integer
print(dominator(ARR_A))
# Codility Testing
# https://app.codility.com/demo/results/trainingDSCNSW-RK9/; trainingKYFR9S-RK4/
# Performance: 100%
# Correctness: 100%
# Difficulty: Painless
