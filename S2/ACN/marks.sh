#!/bin/bash
read -p "Enter mark of Science : " a
read -p "Enter mark of English : " b
read -p "Enter mark of Maths : " c
total=$(($a+$b+$c))
echo "Total Mark : $total"
if [ $total -gt 240 ]
then
	echo "Grade : A"
elif [ $total -gt 180 ]
then
	echo "Grade : B"
elif [ $total -gt 120 ]
then
	echo "Grade : C"
elif [ $total -gt 60 ]
then
	echo "Grade : D"
else
	echo "Failed"
fi

