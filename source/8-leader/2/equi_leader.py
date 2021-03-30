"""count the number of equi-leaders"""
from __future__ import print_function
import getopt
import sys
import re
import collections
def equi_leader(arr_a):
    """count the number of equi-leaders"""
    # define length of arr_a
    len_n = len(arr_a)
    # start equi_count at zero
    equi_count = 0
    # create object of righthand value counts (starting with full vector)
    dct_r = collections.Counter(arr_a).items()
    # convert list of tuples to dict
    dct_r = dict((x, y) for x, y in dct_r)
    # create object of lefthand value counts (starting empty)
    dct_l = dct_r.copy()
    for key in dct_l.iterkeys(): # in python three, replace iterkeys with keys
        dct_l[key] = 0
    # iterate through elements of arr_a
    for ndx_i, val_j in enumerate(arr_a):
        # subtract from and add to righthand & lefthand dicts
        dct_r[val_j] -= 1
        dct_l[val_j] += 1
        # define strongest candidates for left and right dominators
        dom_l = dct_l.keys()[dct_l.values().index(max(dct_l.values()))]
        dom_r = dct_r.keys()[dct_r.values().index(max(dct_r.values()))]
        # in python 3, use list function: list(dct__keys())...
        # in python 3, use list function: list(dct__values()).index(...)
        # test for equivalence
        test = dom_l == dom_r
        # test that left leader comprises more than 50% of left slice
        test = test & (dct_l[dom_l] * 2 > ndx_i + 1)
        # test that right leader comprises more than 50% of right slice
        test = test & (dct_r[dom_r] * 2 > len_n - 1 - ndx_i)
        # if all tests are true, add to equi_count
        if test:
            equi_count += 1
    return equi_count
# Debugging:
# ARR_A = [4, 3, 4, 4, 4, 2]
# equi_leader(ARR_A)
# Bash Testing
ARR_A = list(getopt.getopt(sys.argv, "ho:v"))[1][1] # store string passed from command line
ARR_A = re.sub(r"^\[|\]$", "", ARR_A) # remove brackets from string
ARR_A = ARR_A.split(r",") # split string by comma into list
ARR_A = [int(x) for x in ARR_A] # convert list to class integer
print(equi_leader(ARR_A))
# Codility Testing:
# https://app.codility.com/demo/results/trainingYE389C-8P3/
# Correctness: 100%
# Performance: 75%
