#!/bin/bash
echo "Enter the Number : "
read x
num=x
sum=0
while [ $num != 0 ]
do
	sum=$(($sum+$num%10))
	num=$(($num/10))
done
echo "Sum = $sum"
