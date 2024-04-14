#!/bin/bash
echo -p "Enter a 7 digit number : " num
n=1
while [ $n -le 7 ]
do
	a=`echo $num | cut -c $n`
	echo $a
	n=$(($n + 2))
done
