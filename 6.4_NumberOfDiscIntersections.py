# compute the number of disk intersections in a sequence of disks
# Assumptions:
## 0 <= N <= 100,000
## 0 <= A[i] <= 2,147,483,647
def NumberOfDiscIntersections(A):
	N = len(A)
	# begin with zero intersections
	intersections = 0
	# crawl along array A
	for i in range(0,N):
#		print("i: "+i+", A[i]: "+A[i]:
		# crawl distance "counter" from index, where counter = A[i]
		counter = 0
		while (counter < A[i]*2) and ((0<=i-counter) or (i+counter<=N)):
			counter = counter + 1
#			print("    counter: "+counter+
#				", A[i+counter]: "+A[i+counter]+
#				", A[i-counter]: "+A[i-counter]:
			# look ahead of index by distance counter (but not farther than length of A:
			# to avoid double-counting intersections, only count those < A[i]
			if i+counter < N: 
				if A[i+counter]<A[i] and counter<=A[i]+A[i+counter]:
					# add to intersections count
					intersections+=1
#					print("        intersections: ",intersections:
			
			# look behind index by distance counter (but not lower than zero:
			# to avoid double-counting intersections, only count those <= A[i]
			if 0 <= i-counter: 
				if A[i-counter]<=A[i] and counter<=A[i]+A[i-counter]:
					# add to intersections count
					intersections+=1
#					print("        intersections: ",intersections:
			
		
	
	return(intersections)

## Console Testing
print(["NumberOfDiscIntersections([1,5,2,1,4,0]); expect 11: "] + [NumberOfDiscIntersections([1,5,2,1,4,0])])
print(["NumberOfDiscIntersections([1,1,1]); expect 3: "] + [NumberOfDiscIntersections([1,1,1])])
print(["NumberOfDiscIntersections([1,2147483647,0]); expect 2: "] + [NumberOfDiscIntersections([1,2147483647,0])])
# Codility Testing
## https:#app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
## performance: 12%
## correctness: 100%
## Difficulty: Respectable
