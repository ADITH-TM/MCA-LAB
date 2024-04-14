#!/bin/bash
echo "Enter the Number : "
read a
if [ $a == 2 ]
then
	echo "The num is prime"
else
	for ((i=2; i<=a/2 ; i++))
	do
		if [ $(($a%$i)) == 0 ]
		then
			echo "The num is not prime"
			exit
		fi
	done
	echo "The num is prime"
fi
