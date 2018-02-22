// builds array of length N based on inputs from array A
/// adds 1 to newArrayAk when 1<= Ak <= N
/// sets all newArray values to max(newArray) when Ak = N+1
// Assumptions
/// 1 <= N <= 100,000
/// 1 <= M <= 100,000
/// 1 <= Ai < N
function MaxCounters(N, A) {
    var newArray = [0];
    while (newArray.length < N) {
        newArray.push(0);
    }
    var B = 0; // define variable to track 
    var C = 0; // define variable to track
    for (var i = 0; i <= A.length; i++) {
        if (1 <= A[i] <= N) {
            if (newArray[A[i - 1]] < B) {
                newArray[A[i - 1]] = B;
            }
            newArray[A[i - 1]] = newArray[A[i - 1]] + 1;
            if (C < newArray[A[i - 1]]) {
                C = newArray[A[i - 1]];
            }
        }
        if (A[i] == N + 1) {
            B = C;
        }
    }
    for (var i = 0; i <= N; i++) {
        if (newArray[i] < B) {
            newArray[i] = B;
        }
    }
    newArray.pop();
    return (newArray);
}
// console testing:
console.log("MaxCounters(5,[3,4,4,6,1,4,4]); expect 3,2,2,4,2: " + MaxCounters(5, [3, 4, 4, 6, 1, 4, 4]));
console.log("MaxCounters(1,[1]); expect _: " + MaxCounters(1, [1]));
// codility testing:
/// https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
/// Correctness = 75% (got  expect one) 
/// Performance = 80% (got array of zeros with wrong length)
/// Difficulty: Respectable
