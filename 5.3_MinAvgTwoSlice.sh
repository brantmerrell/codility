#!/usr/bin/env bash
echo
echo "input: [4,2,2,5,1,5,8]; expect 1"
echo Python:
python 5.3_MinAvgTwoSlice.py [4,2,2,5,1,5,8]
echo
echo JavaScript:
nodejs 5.3_MinAvgTwoSlice.js [4,2,2,5,1,5,8]
echo
echo R:
Rscript 5.3_MinAvgTwoSlice.R [4,2,2,5,1,5,8]
echo
echo
echo
echo "input: [8,4]; expect 0"
echo Python:
python 5.3_MinAvgTwoSlice.py [8,4]
echo
echo JavaScript:
nodejs 5.3_MinAvgTwoSlice.js [8,4]
echo
echo R:
Rscript 5.3_MinAvgTwoSlice.R [8,4]
echo
echo
echo
echo "input: ~100 random numbers between 1 and 10000"
number=$RANDOM
let "number %= 10000"
myArray="["$number
i=1
while [ $i -lt 100 ];
do
	number=$RANDOM
	let "number %= 10000"
	myArray+=","$number
	let "i = i + 1"
done
myArray+="]"
echo "input: " $myArray
echo "expect identical results"
echo Python: 
python 5.3_MinAvgTwoSlice.py $myArray
echo JavaScript: 
nodejs 5.3_MinAvgTwoSlice.js $myArray
echo R:
Rscript 5.3_MinAvgTwoSlice.R $myArray
