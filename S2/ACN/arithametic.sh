#!/bin/bash
sum(){
	return $(($1+$2))
}
prod(){
	return $(($1*$2))
}
diff(){
	return $(($1-$2))
}
div(){
	return $(($1/$2))
}
read -p "Enter First Number : " a
read -p "Enter Second Number : " b
sum $a $b
echo "Sum = $?"
prod $a $b
echo "Product = $?"
diff $a $b
echo "Difference = $?"
div $a $b
echo "Quotient = $?"

