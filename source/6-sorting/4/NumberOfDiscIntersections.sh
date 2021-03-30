#!/usr/bin/env bash
# A script for testing the NumberOfDiscIntersections function in R, Python, and JavaScript
echo
echo "input: [1,5,2,1,4,0]; expect 11"
echo
echo R:
Rscript NumberOfDiscIntersections.R [1,5,2,1,4,0]
echo
echo Python:
python number_of_disc_intersections.py [1,5,2,1,4,0]
echo
echo JavaScript:
nodejs NumberOfDiscIntersections.js [1,5,2,1,4,0]
echo
echo
echo
echo "input: [8,4]; expect 0"
echo
echo R:
Rscript NumberOfDiscIntersections.R [8,4]
echo
echo Python:
python number_of_disc_intersections.py [8,4]
echo
echo JavaScript:
nodejs NumberOfDiscIntersections.js [8,4]
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
Rscript NumberOfDiscIntersections.R $myArray
echo
echo Python: 
python number_of_disc_intersections.py $myArray
echo
echo JavaScript: 
nodejs NumberOfDiscIntersections.js $myArray
