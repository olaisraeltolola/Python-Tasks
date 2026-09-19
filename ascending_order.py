number_one = float(input("Enter the first number: "))
number_two = float(input("Enter the second number: "))
number_three = float(input("Enter the third number: "))

largest = 0
smaller = 0
smallest = 0
if (number_one < number_two < number_three):
	largest = number_three
	smaller = number_two
	smallest = number_one
	
elif (number_one < number_three < number_two):
	largest = number_two
	smaller = number_three
	smallest = number_one

elif (number_two < number_one < number_three):
	largest = number_three
	smaller = number_one
	smallest = number_two

elif (number_two < number_three < number_one):
	largest = number_one
	smaller = number_three
	smallest = number_two

elif (number_three < number_one < number_two):
	largest = number_two
	smaller = number_one
	smallest = number_three

elif (number_three < number_two < number_one):
	largest = number_one
	smaller = number_two
	smallest = number_three

print(smallest,"<",smaller,"<",largest)



