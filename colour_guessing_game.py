favourite_colour = "blue"

for guesses in range (3):
	colour = input("Enter a colour: ").lower()

	if colour == favourite_colour:
		print("Correct!")
		break

	elif colour == "green":
		print("Close!")

	else:
		print("Wrong!")


		