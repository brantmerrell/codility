#!/usr/bin/env bash
echo 'Determine whether a given string of parentheses (single type) is properly nested.'
echo 'Assumptions:'
echo '    0 <= N <= 1,000,000'
echo '    S[char] == "(" OR ")"'
echo
myString='(()(())())'
echo 'input: '$myString' ; expect 1:'
echo 'R:'
Rscript nesting.R $myString
echo 'Python:'
python nesting.py $myString
echo 'JavaScript:'
node nesting.js $myString
echo
myString='())'
echo 'input: '$myString' ; expect 0:'
echo 'R:'
Rscript nesting.R $myString
echo 'Python:'
python nesting.py $myString
echo 'JavaScript:'
node nesting.js $myString
myString='())'