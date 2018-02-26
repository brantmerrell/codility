# returns non-replicated element of numeric array
# assumptions:
## 1 <= A.length <= 1,000,000
## 1 <= A[i] <= 1,000,000,000
## all but 1 integers occur an even number of times
def OddOccurrencesInArray(A):
	import collections
	# use collections.Counter() to count recurrences of each integer
	# only store integers in object "Odd" which are not even
	Odd = [m for m, count in collections.Counter(A).items() if not count % 2 == 0]
	# return the only integer in the "Odd" array
	return(Odd[0])
# console testing:
print(["OddOccurrencesInArray([3]); expect 3: "]+[OddOccurrencesInArray([3])])
print(["OddOccurrencesInArray([9,3,9,3,9,7,9]); expect 7: "]+[OddOccurrencesInArray([9,3,9,3,9,7,9])])
# codility testing:
## https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
## note: function must be renamed "solution" for testing
## correctness: 100%
## performance: 100%
## Difficulty: Painless
