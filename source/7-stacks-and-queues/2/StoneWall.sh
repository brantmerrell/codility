#!/usr/bin/env bash
# A script for testing the StoneWall function in R, Python, and JavaScript
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
# Assumptions:
## 1<=N<=100,000
## 1<=H[i]<=1,000,000,000
 
# echo
# echo "input: [8,8,5,7,9,8,7,4,8]; expect 7"
# echo
# echo R:
# Rscript StoneWall.R '[8,8,5,7,9,8,7,4,8]'
# echo
# echo Python:
# python stone_wall.py '[8,8,5,7,9,8,7,4,8]'
# echo
# echo JavaScript:
# nodejs StoneWall.js '[8,8,5,7,9,8,7,4,8]'
# echo
echo
echo
echo "input: [1,1,1]; expect 1"
myString="[1,1,1]"
echo
echo R:
Rscript StoneWall.R $myString
echo
echo Python:
python stone_wall.py $myString
echo
echo JavaScript:
nodejs StoneWall.js $myString
echo
