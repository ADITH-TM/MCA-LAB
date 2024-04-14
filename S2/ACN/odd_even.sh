#!/bin/bash
echo "Enter the Number : "
read x
if [ $(($x%2)) == 0 ]
then
	echo "The number is even"
else
	echo "The number is odd"
fi
