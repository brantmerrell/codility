"""Determine whether a given string of parentheses (single type) is properly nested."""
from __future__ import print_function
import getopt
import sys
def nesting(str_s):
    """Determine whether a given string of parentheses (single type) is properly nested."""
    # set the balance of parentheses at zero
    balance = 0
    # iterate through the string of parentheses
    for paren in str_s:
        # test whether it's a left parenthesis
        if paren == "(":
            # add to balance for left parentheses
            balance += 1
        else:
            # subtract from balance for right parentheses
            balance -= 1
            # there should never be more right parentheses
            if balance < 0:
                # if there are, return zero
                return 0
    # a balance of zero indicates balance
    if balance == 0:
        return 1
    # any other balance score indicates imbalance
    return 0
# Debugging:
# nesting('())')
# nesting('(()(())())')
# Bash Testing:
ARGS_S = list(getopt.getopt(sys.argv, "ho:v"))
ARGS_S = ARGS_S[1][1]
print(nesting(ARGS_S))
# Codility Testing:
# https://app.codility.com/demo/results/trainingNYDRZT-QFC/
# Correctness: 100%
# Performance: 100%
# Difficulty: Painless
