#!/usr/bin/env bash
# A script for testing the Brackets function in R, Python, and JavaScript
echo
echo "input: {[()()]}; expect 1"
echo
echo R:
Rscript 7.1_Brackets.R '{[()()]}'
echo
echo Python:
python 7.1_Brackets.py {[()()]}
echo
echo JavaScript:
nodejs 7.1_Brackets.js '{[()()]}'
echo
echo
echo
echo "input: ([)()]; expect 0"
echo
echo R:
Rscript 7.1_Brackets.R '([)()]'
echo
echo Python:
python 7.1_Brackets.py '([)()]'
echo
echo JavaScript:
nodejs 7.1_Brackets.js '([)()]'
echo
echo
