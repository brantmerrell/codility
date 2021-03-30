#!/usr/bin/env bash
echo 'count the number of equi-leaders'
echo 'The leader of an array is the value that occurs in more than half the elements'
echo 'If an array is split, and both halves have the same leader, it is an equi-leader'
myString='[4,3,4,4,4,2]'
echo 'input: '$myString' ; expect 2:'
echo 'R:'
Rscript equi_leader.R $myString
echo 'Python:'
python equi_leader.py $myString
echo 'JavaScript:'
node equi_leader.js $myString