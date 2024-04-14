#!/bin/bash
echo "Enter the Number : "
read x
fact=1
for ((i=$x; i>=1 ; i--))
do
	fact=$(($fact*$i))
done
echo "Factorial = $fact"
