#!/usr/bin/env bash
echo 'find a maximum sum of a compact subsequence of array elements'
echo 'https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/'
echo 'Assumptions:'
echo '    1 <= N <= 1,000,000'
echo '    -1,000,000 <= A[i] <= 1,000,000'
myString='[3,2,-6,4,0]'
echo 'input: '$myString' ; expect 5:'
echo 'R:'
Rscript max_slice_sum.R $myString
echo 'Python:'
python max_slice_sum.py $myString
echo 'JavaScript:'
node max_slice_sum.js $myString