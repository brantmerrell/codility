// returns non-replicated element of numeric array
// assumptions:
/// 1 <= A.length <= 1,000,000
/// 1 <= Ai <= 1,000,000,000
/// all but 1 integers occur an even number of times
function OddOccurrencesInArray(A) {
    // if A is just one number, return it
    if (A.length == 1) {
        return (A[0]);
    }
    // sort A	
    A = A.sort();
    // only 1 integer occurs an odd number of times
    // therefore, only every other integer in a sorted array 
    // needs to be checked for adjacent equivalence:
    for (var i = 0; i < A.length; i = i + 2) {
        if (A[i] != A[i] + 1) {
            return (A[i]);
        }
    }
}
// console testing:
console.log("OddOccurrencesInArray(3); expect 3: " + OddOccurrencesInArray([3]));
console.log("OddOccurrencesInArray(9,3,9,3,9,7,9); expect 7: " + OddOccurrencesInArray([9, 3, 9, 3, 9, 7, 9]));
// codility testing:
/// https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
/// note: function must be renamed "solution" for testing
/// performance: 50% - probably due to combined use of sort() and for()
/// correctness: 100%
/// Difficulty: Painless
