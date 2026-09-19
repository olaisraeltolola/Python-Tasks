while(True):

	colour = input("Enter a colour: ").casefold()
	first_colour = "green" 
	second_colour = "yellow" 
	third_colour = "red"
	repeat = True

	if (colour == first_colour):
		print("Go")
		break
	elif (colour == second_colour):
		print("Get ready")
		break
	elif (colour == third_colour):
		print("Stop")
		break
	else: print("Invalid")