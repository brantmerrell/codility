#!/usr/bin/env bash
echo 'given a log of stock prices compute the maximum possible earning'
echo 'https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/'
echo 'Assumptions:'
echo '    0 <= N <= 400,000'
echo '    0 <= A[i] <= 200,000'
myString='[23171,21011,21123,21366,21013,21367]'
echo 'input: '$myString' ; expect 356:'
echo 'R:'
Rscript max_profit.R $myString
echo 'Python:'
python max_profit.py $myString
echo 'JavaScript:'
node max_profit.js $myString