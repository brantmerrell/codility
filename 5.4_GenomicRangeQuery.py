# find the minimal nucleotide from a range of sequence DNA 

# Assumptions:
## 1 <= N <= 100,000
## 1 <= M <= 50,000
## 0 <= P <= N-1
## 0 <= Q <= N-1
## P[k] <= Q[k], where 0 <= k < M
## string S consists only of uppercase letters A, C, G, T

def GenomicRangeQuery(S,P,Q):
	# split S string into vector of characters
	S = map(None,S)
	# convert A, C, G, T to 1, 2, 3, 4 respectively
	for n in range(0,len(S)):
		if S[n]=="A": S[n]=1
		if S[n]=="C": S[n]=2
		if S[n]=="G": S[n]=3
		if S[n]=="T": S[n]=4
	# create empty result vector
	res = []
	# loop to fill result vector 
	for k in range(0,len(P)):
		# minimum of range along S from P to Q
		res.append(min(S[P[k]:(Q[k]+1)]))
	return((res))

# console testing:
print(["GenomicRangeQuery('CAGCCTA',[2,5,0],[4,5,6]); expect [2,4,1]: "]
	+[GenomicRangeQuery('CAGCCTA',[2,5,0],[4,5,6])])

# Codility testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
## Performance:
## Correctness:

## Difficulty: Respectable
