#!/usr/bin/env bash
# N voracious fish are moving along a river. Calculate how many fish are alive.
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
# Assumptions:
## 1<=N<=100,000
## 1<=A[i]<=1,000,000,000
## B[i] in [0,1]
## Elements of A are distinct
echo
echo "input: [4,3,2,1,5],[0,1,0,0,0]; expect 1"
myString="[4,3,2,1,5],[0,1,0,0,0]"
echo
echo R:
Rscript Fish.R $myString
echo
echo Python:
python fish.py $myString
echo
echo JavaScript:
nodejs Fish.js $myString
echo
