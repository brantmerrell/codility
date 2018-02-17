# returns maximum binary gap of integer
## binary gap: adjacent zeros in a binary number (excluding trailing zeros)
## maximum binary gap: maximum character count of binary gap

# Assumptions:
## 1 <= N <= 1,147,483,647

def binary_gap(N):

	# convert to binary string
	N = str(bin(N))
	import re

	# remove "0b" from binary string
	N = re.sub("0b","", N)

	# remove leading & trailing zeros; split by 1s
	N = re.sub("^0+|0+$","", N).split("1")

	# convert each binary gap to a character count
	for i in range(0, len(N), 1): N[i] = N[i].count("0")

	return(max(N))


# console testing:
print(["binary_gap(9); expect 2: "]+[binary_gap(9)])
print(["binary_gap(529); expect 4: "]+[binary_gap(529)])
print(["binary_gap(20); expect 1: "]+[binary_gap(20)])
print(["binary_gap(15); expect 0: "]+[binary_gap(15)])

# codility testing:
## https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
## note: function must be renamed "solution" for testing
## performance: not assessed
## correctness: 100%
## Difficulty: Painless
