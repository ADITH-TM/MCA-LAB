#!/bin/bash
echo "Hello, World!"
name="Akash"
echo "My name is $name"
read -p "Enter Your age: " age
echo "Your age $age Years old. "
if [ $age -ge 18 ]; then
	echo "You are an adult."
else
	echo "You are a minor."
fi
