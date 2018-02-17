# count the number of passing cars on the road 

# Assumptions:
## 1 <= N <= 100,000
## A[i] == 1 OR 0

def PassingCars(A):

	# count west-travelling cars

	# subtract to count uncounted east-travelling cars

	# start pairs of passing cars at zero

	# loop through array of cars

		# if the car is travelling east,

			# subtract now-counted car from east

			# add west-travelling cars for this car to pairs of passing cars

			# if pairs exceeds 1B, return -1

		# if the car is travelling west, subtract now-counted car from west

	return(pairs)

# console testing:
console.log(["PassingCars([0,1,0,1,1]); expect 5: "]+[CountDiv([0,1,0,1,1])])

# Codility testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
## Performance:
## Correctness:

## Difficulty: Painless
