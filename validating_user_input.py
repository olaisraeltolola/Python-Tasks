counter = 0
while(True):

	number_one = int(input("Enter a number: "))
	
	if number_one == 1 or number_one == 2:
		print("Correct!")
		break

	else:
		print("Wrong!")
		counter += 1

print("The number of failures you have", counter)

