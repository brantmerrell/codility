#!/usr/bin/env bash
echo 'Find an index of an array such that its value occurs at more than half of indices in the array.'
echo 'Assumptions:'
echo '    0 <= N <= 100,000'
echo '    −2,147,483,648 <= A[i] <= 2,147,483,647'
echo
myString='[3,4,3,2,3,-1,3,3]'
echo 'input: '$myString' ; expect 0, 2, 4, 6 or 7:'
echo 'R:'
Rscript dominator.R $myString
echo 'Python:'
python dominator.py $myString
echo 'JavaScript:'
node dominator.js $myString