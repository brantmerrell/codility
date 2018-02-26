#!/usr/bin/env bash
# A script for testing the PassingCars function in R, Python, and JavaScript
# Assumptions:
## 1 <= N <= 100,000
## A[i] == 1 OR 0
echo "input: [0,1,0,1,1]; expect 5"
echo
echo R:
Rscript 5.2_PassingCars.R [0,1,0,1,1]
echo
echo Python:
python 5.2_PassingCars.py [0,1,0,1,1]
echo
echo JavaScript:
nodejs 5.2_PassingCars.js [0,1,0,1,1]
echo
echo
echo
echo "input: ~100 random ones and zeros"
number=$RANDOM
if [ $(($number%2)) -eq 0 ]
then
	let "number=0"
else
	let "number=1"
fi
myArray="["$number
i=1
while [ $i -lt 100 ];
do
	number=$RANDOM
	if [ $(($number%2)) -eq 0 ]
	then
		let "number = 0"
	else
		let "number = 1"
	fi
	myArray+=","$number
	let "i = i + 1"
done
myArray+="]"
echo $myArray
echo "expect identical results"
echo
echo R:
Rscript 5.2_PassingCars.R $myArray
echo
echo Python: 
python 5.2_PassingCars.py $myArray
echo
echo JavaScript: 
nodejs 5.2_PassingCars.js $myArray
