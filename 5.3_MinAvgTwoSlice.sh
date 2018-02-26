#!/usr/bin/env bash
echo
echo "input: [4,2,2,5,1,5,8]; expect 1"
echo
echo R:
Rscript 5.3_MinAvgTwoSlice.R [4,2,2,5,1,5,8]
echo
echo Python:
python 5.3_MinAvgTwoSlice.py [4,2,2,5,1,5,8]
echo
echo JavaScript:
nodejs 5.3_MinAvgTwoSlice.js [4,2,2,5,1,5,8]
echo
echo
echo
echo "input: [8,4]; expect 0"
echo
echo R:
Rscript 5.3_MinAvgTwoSlice.R [8,4]
echo
echo Python:
python 5.3_MinAvgTwoSlice.py [8,4]
echo
echo JavaScript:
nodejs 5.3_MinAvgTwoSlice.js [8,4]
echo
echo
echo
echo "input: ~100 random numbers between 1 and 10000, in which even numbers are negative"
number=$RANDOM
let "number %= 10000"
myArray="["$number
i=1
while [ $i -lt 100 ];
do
	number=$RANDOM
	let "number %= 10000"
	if [ $(($number%2)) -eq 0 ]
	then
		let "number = number * -1"
	fi
	myArray+=","$number
	let "i = i + 1"
done
myArray+="]"
echo $myArray
echo "expect identical results"
echo
echo R:
Rscript 5.3_MinAvgTwoSlice.R $myArray
echo
echo Python: 
python 5.3_MinAvgTwoSlice.py $myArray
echo
echo JavaScript: 
nodejs 5.3_MinAvgTwoSlice.js $myArray
