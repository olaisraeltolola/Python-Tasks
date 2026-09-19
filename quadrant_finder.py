number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))

if (number_one > 0 and number_two > 0): 
	print("Quadrant 1")
elif (number_one < 0 and number_two > 0): 
	print("Quadrant 2")
elif (number_one < 0 and number_two < 0): 
	print("Quadrant 3")
elif (number_one > 0 and number_two < 0): 
	print("Quadrant 4")
elif (number_one == 0 and number_two == 0): 
	print("Origin")
elif (number_one != 0 and number_two == 0): 
	print("X-axis")
elif (number_one == 0 and number_two != 0): 
	print("Y-axis")

