#!/bin/bash
echo "Enter the Number : "
read x
num=x
rnum=0
while [ $num != 0 ]
do
	rnum=$(($rnum*10+$num%10))
	num=$(($num/10))
done
echo $rnum
