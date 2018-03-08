"""count the number of equi-leaders"""
from __future__ import print_function
import getopt
import sys
import re
import collections
def equi_leader(arr_a):
    """count the number of equi-leaders"""
    # start equi_count at zero
    equi_count = 0
    # create object of righthand value counts (starting with full vector)
    obj_r = collections.Counter(arr_a).items()
    # convert list of tuples to dict
    obj_r = dict((x,y) for x,y in obj_r)
    # create object of lefthand value counts (starting empty)
    obj_l = obj_r.copy()
    for key in obj_l.iterkeys():
        obj_l[key]=0
    # iterate through elements of arr_a
    for ndx_i,val_j in enumerate(arr_a):
        # subtract from and add to righthand & lefthand dicts
        obj_r[val_j] -= 1
        obj_l[val_j] += 1
        # test for righthand dominator
        if max(obj_r.values()) * 2 > len(arr_a) - ndx_i - 1:
            

    return arr_a
# Debugging:
ARR_A = [4, 3, 4, 4, 4, 2]
equi_leader(ARR_A)
# Bash Testing
ARR_A = list(getopt.getopt(sys.argv, "ho:v"))[1][1] # store string passed from command line
ARR_A = re.sub(r"^\[|\]$", "", ARR_A) # remove brackets from string
ARR_A = ARR_A.split(r",") # split string by comma into list
ARR_A = [int(x) for x in ARR_A] # convert list to class integer
equi_leader(ARR_A)
