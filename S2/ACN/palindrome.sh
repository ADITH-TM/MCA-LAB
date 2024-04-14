#!/bin/bash
echo "Enter a String : "
read input_string
reversed_string=$(echo $input_string | rev)
echo "Reverse string is : $reversed_string"
if [ $input_string == $reversed_string ]
then
	echo "the string is palindrome"
else
	echo "the string is not palindrome"
fi
