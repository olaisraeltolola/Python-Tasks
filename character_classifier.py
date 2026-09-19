character = input("Enter a character: ")

try:
	if len(character) == 1:
		digit = int(character)
		print("The character is a digit")
	else: print("This is not a character")

except ValueError:
	if character.isalpha() and len(character) == 1: 
		print("This character is a letter")

	elif len(character) == 1 and not character.isalpha(): print("This character is a special symbol") 