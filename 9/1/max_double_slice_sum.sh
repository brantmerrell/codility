#!/usr/bin/env bash
echo 'find the maximal sum of any double slice'
echo 'https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/'
echo 'Assumptions:'
echo '    3 <= N <= 100,000'
echo '    -10,000 <= A[i] <= 10,000'
myString='[3,2,6,-1,4,5,-1,2]'
echo 'input: '$myString' ; expect 17:'
echo 'R:'
Rscript max_double_slice_sum.R $myString
echo 'Python:'
python max_double_slice_sum.py $myString
echo 'JavaScript:'
node max_double_slice_sum.js $myString