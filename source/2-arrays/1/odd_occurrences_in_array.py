# returns non-replicated element of numeric array
# assumptions:
## 1 <= A.length <= 1,000,000
## 1 <= A[i] <= 1,000,000,000
## all but 1 integers occur an even number of times
def OddOccurrencesInArray(A):
    # initialize hash or dict
    result = {}
    # iterate through A
    for ndx_i, val_j in enumerate(A):
        # add to hash if not in hash
        if(result.__contains__(val_j)):
            result.pop(val_j)
        # remove from hash if in hash
        else:
            result[val_j] = None
    return list(result.keys())[0]
# console testing:
print(["OddOccurrencesInArray([3]); expect 3: "]+[OddOccurrencesInArray([3])])
print(["OddOccurrencesInArray([9,3,9,3,9,7,9]); expect 7: "]+[OddOccurrencesInArray([9,3,9,3,9,7,9])])
# codility testing:
## https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
## note: function must be renamed "solution" for testing
## correctness: 100%
## performance: 100%
## Difficulty: Painless
