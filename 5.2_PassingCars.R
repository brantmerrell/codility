# count the number of passing cars on the road 
# Assumptions:
## 1 <= N <= 100,000
## A[i] == 1 OR 0
PassingCars <- function(A){
	# define N as defined in exercise
	N = length(A)
	# count west-travelling cars
	west = sum(A)
	# subtract to count uncounted east-travelling cars
	east = N - west
	# start pairs of passing cars at zero
	pairs = 0
	# loop through array of cars
	for (i in 1:N) {
		# if the car is travelling east,
		if (A[i] == 0) {
			# subtract now-counted car from east
			east = east - 1
			# add west-travelling cars for this car to pairs of passing cars
			pairs = pairs + west
			# if pairs exceeds 1B, return -1
			if (1000000000 < pairs) {
				return (-1)
			}
		}
		# if the car is travelling west, 
		else {
			# subtract now-counted car from west
			west = west - 1
		}
	}
	return (pairs)
}
# Bash Testing:
args <- commandArgs()[6]
args <- gsub("^\\[|\\]$","",args)
args <- as.numeric(unlist(strsplit(args, ",")))
print(PassingCars(args))
# Codility testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
## Difficulty: Painless
