# count the number of passing cars on the road 
# Assumptions:
## 1 <= N <= 100,000
## A[i] == 1 OR 0
def PassingCars(A):
    N = len(A)
    # count west-travelling cars
    west = sum(A)
    # subtract to count uncounted east-travelling cars
    east = N - west
    # start pairs of passing cars at zero
    pairs = 0
    # loop through array of cars
    for i in range(0,N): 
        # if the car is travelling east,
        if (A[i] == 0):
            # subtract now-counted car from east
            east = east - 1
            # add west-travelling cars for this car to pairs of passing cars
            pairs = pairs + west
            # if pairs exceeds 1B, return -1
            if (1000000000 < pairs):
                return (-1)
            # if the car is travelling west, subtract now-counted car from west
        else:
            west = west - 1
    return (pairs)
# Bash Testing:
import getopt, sys, re
args = list(getopt.getopt(sys.argv,"ho:v"))[1][1]
args = re.sub("^\[|\]$","",args).split(",")
args = [int(x) for x in args]
print(PassingCars(args))
# Codility testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
## Performance: 100%
## Correctness: 100%
## Difficulty: Painless
