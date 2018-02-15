
def PermMissingElem(A):
	N = len(A) 			# exercise refers to N as the length of A, zero not included
	if(N==0) or not min(A)==1:	# if set is missing 1 (including if empty),
		return(1)			# then 1 is the missing element
	elif max(A)==N: 	# if no skips exist in set (and it begins at 1),
		return(N+1) 	# missing element is at end of set
	else:			# otherwise missing element is within set
		A = sorted(A)		# therefore, first sort the set
		for n in xrange(0, N):	# then crawl from 0 to N (zero included, therefore N-1)
			if A[n]>n+1:		# A[n] will correspond to n+1 until skipped element
				return(n+1)		# then, retun n+1

# Empty list and single element: got 1 expected 2
#print(["Empty list - []"]+[PermMissingElem([])])
#print(["Single element - [3]"]+[PermMissingElem([3])]) 
#print(["Single element - [1]"]+[PermMissingElem([1])])
#print(["Missing first - [3,2,5,4]"]+[PermMissingElem([3,2,5,4])])
#print(["Missing last - [1,2,4,3]"]+[PermMissingElem([1,2,4,3])])
#print(["Double - [1,3]"]+[PermMissingElem([1,3])])	# got None expected 2
#print(["Practice - [2,3,1,5]"]+[PermMissingElem([2,3,1,5])])

# accuracy = 100%, performance = 100%

