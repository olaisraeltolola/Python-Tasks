number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))

largest = number_one

if (number_two > largest):
	largest = number_two

if (number_three > largest):
	largest = number_three
print("The largest number is", largest)