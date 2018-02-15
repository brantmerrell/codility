
# see also https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

def OddOccurrencesInArray(A):
	import collections
	Odd = [m for m, count in collections.Counter(A).items() if not count % 2 == 0]
	return(Odd[0])
# correctness: 100%
# performance: 100%

