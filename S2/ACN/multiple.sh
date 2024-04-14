#!/bin/bash
read -p "Enter the Number : " a
read -p "Enter the limit : " n
for ((i=1; i<=n ; i++))
do
	echo "$a x $i = $(($a*$i))"
done
