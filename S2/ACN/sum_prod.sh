#!/bin/bash
echo "Enter 4 numbers : "
read a
read b
read c
read d
s=$(($a+$b+$c+$d))
prod=$(($a*$b*$c*$d))
avg=$(echo "scale=2; $s/4" | bc)
echo "Sum = $s"
echo "Product = $prod"
echo "Average = $avg"

