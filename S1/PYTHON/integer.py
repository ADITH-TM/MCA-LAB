numbers=input("Enter a list of integers,seprated by commas:")
numbers=[int(x) for x in numbers.split(",")]
for number in numbers:
      if number>100:
            print("over")
      else:
            print(number)
