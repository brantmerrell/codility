#!/usr/bin/env bash
# N voracious fish are moving along a river. Calculate how many fish are alive.
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
echo "Assumptions:"
echo "    1<=N<=100,000"
echo "    1<=A[i]<=1,000,000,000"
echo "    B[i] in [0,1]"
echo "    Elements of A are distinct"
myString="[4,3,2,1,5],[0,1,0,0,0]"
echo "input: "$myString" ; expect 2"
# echo
# echo R:
# Rscript Fish.R $myString
echo
echo Python:
python fish.py $myString
echo
echo JavaScript:
nodejs Fish.js $myString
echo
echo
echo
echo "input: length=10, A[i]=random, B[i]=(1 OR 0)"
number=$RANDOM
let "number %= 10000"
ArrayA="["$number
if [ $(($number%2)) -eq 0 ]
then
	ArrayB="["0
else
    ArrayB="["1
fi
i=1
while [ $i -lt 10 ];
do
	number=$RANDOM
	ArrayA+=","$number
    if [ $(($number%2)) -eq 0 ]
    then
        ArrayB+=","0
    else
        ArrayB+=","1
    fi
	let "i = i + 1"
done
ArrayA+="]"
ArrayB+="]"
echo
echo $ArrayA
echo
echo $ArrayB
echo
echo JavaScript: 
nodejs Fish.js $ArrayA,$ArrayB
echo
echo Python:
python fish.py $ArrayA,$ArrayB
