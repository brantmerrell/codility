# find the minimal nucleotide from a range of sequence DNA 

# Assumptions:
## 1 <= N <= 100,000
## 1 <= M <= 50,000
## 0 <= P <= N-1
## 0 <= Q <= N-1
## P[k] <= Q[k], where 0 <= k < M
## string S consists only of uppercase letters A, C, G, T

def GenomicRangeQuery(S,P,Q):

# console testing:
print(["GenomicRangeQuery('CAGCCTA',[2,5,0],[4,5,6]); expect [2,4,1]: "]
	+[GenomicRangeQuery('CAGCCTA',[2,5,0],[4,5,6])])

# Codility testing:
## https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
## Performance:
## Correctness:

## Difficulty: Respectable
